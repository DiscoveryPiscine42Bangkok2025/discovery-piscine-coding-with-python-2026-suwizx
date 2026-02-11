#!/usr/bin/env python3

import sys
if len(sys.argv) > 1:
    if sys.argv[1] == "yolo":
        print("none")
        sys.exit()

for i in range(11):
    print(f"Table de {i}:", end="")
    for j in range(11):
        print(f"{i * j:2}", end=" ")
    print()