#!/usr/bin/env python

import sys
import osint_runner


def run(ip):
    osint_runner.run("ip", "ip", ip)


if __name__ == "__main__":
    ip = sys.argv[1]
    run(ip)
