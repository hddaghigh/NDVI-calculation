import argparse



parser = argparse.ArgumentParser(description="arguments")

parser.add_argument(
    "--url",
    type=str
)
parser.add_argument(
    "--constant",
    type=int,
    default=3
)
args = parser.parse_args()

for i in range(args.constant):
    print(i, args.url)