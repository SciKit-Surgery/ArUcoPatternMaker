# coding=utf-8

"""Command line processing"""


import argparse
from arucopatternmaker import __version__
from arucopatternmaker.ui.arucopatternmaker_demo import run_demo


def main(args=None):
    """Entry point for ArUcoPatternMaker application"""

    parser = argparse.ArgumentParser(description='ArUcoPatternMaker')

    parser.add_argument('--page', default="A4", help='page size: A4 or A3')
    parser.add_argument('--landscape', dest='landscape', action='store_const',
            const=True,default=False,help="set landscape")
    parser.add_argument('--portrait', dest='landscape', action='store_const',
            const=False,default=False,help="set landscape")
    parser.add_argument('--markersize', type=float,default=20,
            help="marker size (mm)")
    parser.add_argument('--bordersize', type=float, default=1,
            help="border around marker (mm)")
    parser.add_argument('--spacing', type=float,default=2,
            help="marker spacing in vertical and horizontal (mm)")
    parser.add_argument('--pagemargin', type=float,default=15,
            help="spacing default around (mm)")
    parser.add_argument('--fill', action="store_true",
            help="fills the page, overrides rows, and cols")
    parser.add_argument('--rows', type=int,default=5,help="fill rows")
    parser.add_argument('--cols', type=int,default=3,help="fill cols")
    parser.add_argument('--first', type=int,default=360,help="first id")
    parser.add_argument('--last', type=int,default=410,help="last id")
    parser.add_argument('--repeat', type=bool,default=False,
            help="repeat mode (ends at last)")
    parser.add_argument('--count', type=int,default=0,
            help="count (alternative to last)")
    parser.add_argument('--border', action='store_true',
            help="draws black border around")
    parser.add_argument('--pageborder', action='store_true',
            help="draws black border around")
    parser.add_argument('--axis', action='store_true',help="highlights axis")
    parser.add_argument('--random', action='store_true',
            help="randomize markers for board (and produces the randomization)")
    parser.add_argument('--output',default="output.pdf",help="outputfilename")
    parser.add_argument("-v", "--verbose",
                        action="store_true",
                        help="Enable verbose output",
                        )

    version_string = __version__
    friendly_version_string = version_string if version_string else 'unknown'
    parser.add_argument(
        "--version",
        action='version',
        version='ArUcoPatternMaker version ' + friendly_version_string)

    args = parser.parse_args(args)

    run_demo(args.page, args.landscape, args.fill, args.pagemargin,
            args.markersize, args.bordersize, args.spacing, args.cols,
            args.rows, args.output, args.first, args.last, args.count,
            args.random, args.pageborder, args.verbose)
