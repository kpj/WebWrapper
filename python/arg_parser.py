import argparse


parser = argparse.ArgumentParser(description="PyQt wrapper for web applications")

parser.add_argument(
	"file",
	help="Entry point to web application (e.g. index.html)"
)
parser.add_argument(
	"-v",
	"--verbose",
	help="Enable javascript console in webview",
	action="store_true"
)

def get_args():
	return vars(parser.parse_args())