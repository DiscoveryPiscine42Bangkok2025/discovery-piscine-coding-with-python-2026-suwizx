#!/usr/bin/env python3

import sys

if len(sys.argv) < 2:
    print("none")
else:
    for param in range(1, len(sys.argv)):
        if sys.argv[param].endswith("ism"):
            continue
        print(sys.argv[param] + "ism")