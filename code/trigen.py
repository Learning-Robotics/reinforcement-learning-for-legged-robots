#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import random

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("size", type=int)
    args = parser.parse_args()
    print(f"{args.size}")
    for i in range(args.size):
        print(" ".join(str(random.randint(10, 99)) for _ in range(i + 1)))
