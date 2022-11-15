import argparse
from calculate import calculate


parser = argparse.ArgumentParser(description="arguments")

parser.add_argument(
    "--url",
    type=str
)
parser.add_argument(
    "--ndviValue",
    type=float,
    default=1
)
args = parser.parse_args()


calculate(args.url, args.ndviValue)