#!/usr/bin/env python3
# coding:utf-8
import sys
hostname=sys.argv[1]
with open ('helloworld.txt', 'a') as f:
    f.write(hostname)
