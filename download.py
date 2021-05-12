import argparse
import os
import sys
import time

parser = argparse.ArgumentParser()
parser.add_argument("--queries", type=str, help='path to queries text file')
parser.add_argument("--directories", type=str, help='path to directories text file')
parser.add_argument("--run_headless", action="store_true", help='run the script without launching the chromium browser')
args = parser.parse_args()

# Read the text files
with open(os.path.join(args.queries)) as f:
    queries = f.readlines()
with open(os.path.join(args.directories)) as f:
    dirnames = f.readlines()

# start crawling the search engines
for line, dirs in zip(queries, dirnames):
    queries = (line.rstrip()).split(',')  # get list of queries
    for i, query in enumerate(queries):
        dirs = dirs.rstrip()
        query = query.lstrip(' ')
        print(f"Downloading {query}: ")
        run_headless = "--run_headless" if args.run_headless else ""
        os.system(f"python ./Download/bingget.py --query '{query}' --save_image_dir {dirs} --index {str(i)} {run_headless}")
        os.system(f"python ./Download/googleget.py --query '{query}' --save_image_dir {dirs} --index {str(i)} {run_headless}")
        os.system(f"python ./Download/yahooget.py --query '{query}' --save_image_dir {dirs} --index {str(i)} {run_headless}")
        time.sleep(2)
