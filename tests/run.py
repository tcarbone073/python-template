import argparse
import os
import sys
import unittest

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
group.add_argument("-v", "--verbosity", help="Specify output verbosity", type=int, choices=[0, 1, 2], default=1)
group.add_argument("-s", "--silent", help="Suppress all output", action="store_true", default=False)
parser.add_argument(
    "--testcase",
    help="Run specific module.TestCase from tests/",
)
parser.add_argument(
    "-f", "--failfast", help="Exit immediately after any test failure.", action="store_true", default=False
)

args = parser.parse_args()

tests = [
    "tests.test_module.ExampleTestCase",
    "tests.test_module.AnotherExampleTestCase",
]

if args.silent:
    stream = open(os.devnull, "w")
else:
    stream = None

if args.testcase:
    tests = [args.testcase]

runner = unittest.TextTestRunner(stream=stream, verbosity=args.verbosity, failfast=args.failfast)
suite = unittest.defaultTestLoader.loadTestsFromNames(tests)
ret = not runner.run(suite).wasSuccessful()
sys.exit(ret)
