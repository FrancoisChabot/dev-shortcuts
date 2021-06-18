import <module>.__version__ as version

import argparse
import logging
import os

# Adapted from: https://stackoverflow.com/a/5464440/4442671
def help_formatter():
    try:
        width, _ = os.get_terminal_size(0)
        return lambda prog: argparse.RawDescriptionHelpFormatter(prog, width=width, max_help_position=int(width/3))
    except OSException:
        return argparse.RawDescriptionHelpFormatter

EXAMPLES = '''
Examples:
  insert_some_example
  insert_other_example
'''

parser = argparse.ArgumentParser(
    description='General description of the command',
    usage='%(prog)s [--version] [--help] [options]',
    add_help=False,
    formatter_class=help_formatter(),
    epilog=EXAMPLES
)

# ... insert arguments here ...
# ref: https://docs.python.org/3/library/argparse.html

misc_grp = parser.add_argument_group('Misc options')
misc_grp.add_argument('--version', action='store_true', default=False, help='Output version information')
misc_grp.add_argument("-h", "--help", action="help", help="show this help message and exit")
verbosity = misc_grp.add_mutually_exclusive_group(required=False)
verbosity.add_argument('-v', '--verbose', action='store_true', default=False, help='Produce more logs')
verbosity.add_argument('-q', '--quiet', action='store_true', default=False, help='Do not produce any logs')

if args.verbose:
    logging.basicConfig(level=logging.INFO)
elif args.quiet:
    logging.basicConfig(level=logging.CRITICAL)
else:
    logging.basicConfig(level=logging.INFO)

if args.version:
    print(version.STRING, args.verbose)
    exit(0)
