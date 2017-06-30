#!/usr/bin/env python

import sys
import osint_runner


def run(username):
    osint_runner.run("username", "username", username)


if __name__ == "__main__":
    username = sys.argv[1]
    run(username)
