#!/usr/bin/python3

# Author: z3r0day :: https://github.com/SxNade

RED = '\033[1;31;48m'
WHITE = "\33[0m"
GREEN = '\033[1;32;48m'

import re
import sys

def js_search(data_to_search_through):
    js = re.findall(r"src=\"(.*\.js)", data_to_search_through)
    js_files = list(set(js))
    return js_files
