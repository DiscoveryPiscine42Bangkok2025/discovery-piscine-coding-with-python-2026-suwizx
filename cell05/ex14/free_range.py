#!/usr/bin/env python3

import sys

if len(sys.argv) != 3:
    print("none")
else:
    start = int(sys.argv[1])
    end = int(sys.argv[2])

    step = 1

    if start > end:
        step = -1

    result = list(range(start, end + step, step))

    print(result)
