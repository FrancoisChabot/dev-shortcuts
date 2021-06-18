import argparse
import logging
import os
import sys

class LogFormatter(logging.Formatter):
    """COLORS Formatter wrapper that adds color"""
    COLORS = {
        logging.DEBUG: "\x1b[38;21m",
        logging.INFO: "\x1b[38;21m",
        logging.WARNING: "\x1b[33;21m",
        logging.ERROR: "\x1b[31;21m",
        logging.CRITICAL: "\x1b[31;1m"
    }

    COLOR_RESET = '\x1b[0m'

    def __init__(self, child, colored):
        super().__init__()
        self.child = child
        self.colored = colored

    def format(self, record):
        if self.colored:
            prefix = f'[{self.COLORS.get(record.levelno)}'
            postfix = f'{self.COLOR_RESET}] '
        else:
            prefix = '['
            postfix = '] '

        return prefix + logging.getLevelName(record.levelno) + postfix + self.child.format(record)

console_log_formatter = LogFormatter(logging.Formatter('%(name)s: %(message)s'), True)
console_log_handler = logging.StreamHandler(sys.stderr)
console_log_handler.setFormatter(console_log_formatter)

class App:
    def __init__(self, arg_parser, version):
        self.arg_parser = arg_parser
        self.version = version

    def add_argument_group(self, name):
        return self.arg_parser.add_argument_group(name)

    def parse_args(self):
        misc_grp = self.add_argument_group('Misc options')
        misc_grp.add_argument('--version', action=PrintVersion(self.version), nargs=0, help='Output version information and exit')
        verbosity = misc_grp.add_mutually_exclusive_group(required=False)
        verbosity.add_argument('-v', '--verbosity', action=SetVerbosity(logging.INFO), nargs=0, help='Produce more logs')
        verbosity.add_argument('--nocolor', action=SetColoredLogs(False), nargs=0, help='Stop coloring stderr logs')
        verbosity.add_argument('-q', '--quiet', action=SetVerbosity(logging.CRITICAL), nargs=0, help='Do not produce any non-critical logs')
        misc_grp.add_argument("-h", "--help", action="help", help="show this help message and exit")

        return self.arg_parser.parse_args()

def prepare(description, usage, help_epilog, version):
    logging.addLevelName(logging.DEBUG, ' DBG')
    logging.addLevelName(logging.INFO, 'INFO')
    logging.addLevelName(logging.WARNING, 'WARN')
    logging.addLevelName(logging.ERROR, ' ERR')
    logging.addLevelName(logging.CRITICAL, 'CRIT')
    
    logger = logging.getLogger()

    logger.setLevel(logging.WARNING)
    logger.addHandler(console_log_handler)

    arg_parser = argparse.ArgumentParser(
        description=description,
        usage=usage,
        add_help=False,
        formatter_class=help_formatter(),
        epilog=help_epilog
    )

    return App(arg_parser, version)


def help_formatter():
    try:
        width, _ = os.get_terminal_size(0)
        return lambda prog: argparse.RawDescriptionHelpFormatter(prog, width=width, max_help_position=int(width/3))
    except Exception:
        return argparse.RawDescriptionHelpFormatter

# ACTIONS
def PrintVersion(version):
    class Action(argparse.Action):
        def __call__(self, parser, namespace, values, option_string=None):
            print(version)
            exit(0)

    return Action

def SetVerbosity(value):
    class Action(argparse.Action):
        def __call__(self, parser, namespace, values, option_string=None):
            logging.getLogger().setLevel(level=value)

    return Action

def SetColoredLogs(value):
    class Action(argparse.Action):
        def __call__(self, parser, namespace, values, option_string=None):
            console_log_formatter.colored = value
    return Action

