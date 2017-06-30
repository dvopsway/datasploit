#!/usr/bin/env python

import sys
import osint_runner


def run(domain):
    osint_runner.run("domain", "domain", domain)


if __name__ == "__main__":
    domain = sys.argv[1]
    run(domain)