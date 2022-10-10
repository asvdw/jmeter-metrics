import os
import argparse
from jmetermetrics import generate_report
from version import __version__


def parse_options():
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    general = parser.add_argument_group("General")
    parser.add_argument(
        '-v', '--version',
        action='store_true',
        dest='version',
        help='Display application version information'
    )
    general.add_argument(
        '--logo',
        dest='logo',
        default='http://www.blairlancaster.ca/wp-content/uploads/2016/12/212._SUN-S10581_-_Suncor_-_Roads__Grounds_-_Maximum_40_KM_H_Sign_-_May_2014.png',
        help="User logo (default: dummy image )"
    )

    general.add_argument(
        '-I', '--inputpath',
        dest='path',
        default=os.path.curdir,
        help="Path of result files"
    )

    general.add_argument(
        '-M', '--metrics-report-name',
        dest='metrics_report_name',
        help="Output name of the generate metrics report"
    )

    general.add_argument(
        '-O', '--output',
        dest='output',
        default="result.jtl",
        help="Name of *.jtl or *.csv file"
    )

    general.add_argument(
        '-K', '--ignoretableresult',
        dest='ignoretableresult',
        default="False",
        help="Ignore table report in metrics report"
    )

    general.add_argument(
        '-S', '--seperator',
        dest='seperator',
        default=",",
        help="Seperator of columns"
    )

    args = parser.parse_args()
    return args


def main():
    args = parse_options()

    if args.version:
        print(__version__)
        exit(0)
    args.output = "input/VALID_FULL_22-10-07_18-09_subresults.jtl"
    # args.output = "input/main.jtl"
    args.metrics_report_name="metrics.html"
    args.ignoretableresult = "True"
    generate_report(args)

main()