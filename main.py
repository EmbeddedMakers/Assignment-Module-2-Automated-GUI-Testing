"""
Starting point for the test suite.
"""
import sys
from src.AmazonCartTest import AmazonCartTest
from src.AmazonSearchTest import AmazonSearchTest
from src.AmazonCheckoutTest import AmazonCheckoutTest


def _report_test_results(failed_tests: int) -> None:
    print("\n### SUMMARY ###")
    if failed_tests == 0:
        print("All tests passed!")
    else:
        print("One or more tests failed. Please see above output for more information.")
        sys.exit(1)


def run_all_tests() -> None:

    test_obj = AmazonCheckoutTest()
    test_obj.run_test()
    test_obj = AmazonCartTest()
    test_obj.run_test()
    test_obj = AmazonSearchTest()
    test_obj.run_test()

def main() -> None:
    run_all_tests()

if __name__ == "__main__":
    main()