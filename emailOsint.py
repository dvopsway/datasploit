#!/usr/bin/env python

import sys
import osint_runner


def run(email):
    osint_runner.run("email", "emails", email)


if __name__ == "__main__":
    email = sys.argv[1]
    run(email)
