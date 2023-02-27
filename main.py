"""
Starting point for the test suite.
"""
import sys
from src.amazon_cart_test import AmazonCartTest
from src.amazon_search_test import AmazonSearchTest
from src.amazon_signin_test import AmazonSignInTest
from src.amazon_checkout_test import AmazonCheckoutTest
from src.amazon_addtolist_test import AmazonAddToListTest
from src.amazon_sort_by_price_test import AmazonSortByPriceTest
from src.amazon_filter_by_customer_review_test import AmazonFilterByCustomerReview

def _report_test_results(failed_tests: int) -> None:
    print("\n### SUMMARY ###")
    if failed_tests == 0:
        print("All tests passed!")
    else:
        print("One or more tests failed. Please see above output for more information.")
        sys.exit(1)


def test_run_test_amazon_filterby_customerreview() -> None:
    test_obj = AmazonFilterByCustomerReview()
    test_obj.announce_test()
    passed_test = test_obj.run_test()
    assert passed_test == True

def test_run_test_amazon_search() -> None:
    test_obj = AmazonSearchTest()
    test_obj.announce_test()
    passed_test = test_obj.run_test()
    assert passed_test == True


def test_run_test_amazon_cart() -> None:
    test_obj = AmazonCartTest()
    test_obj.announce_test()
    passed_test = test_obj.run_test()
    assert passed_test == True


def test_run_test_amazon_checkout() -> None:
    test_obj = AmazonCheckoutTest()
    test_obj.announce_test()
    passed_test = test_obj.run_test()
    assert passed_test == True


def test_run_test_amazon_signin() -> None:
    test_obj = AmazonSignInTest()
    test_obj.announce_test()
    passed_test = test_obj.run_test()
    assert passed_test == True

def test_run_test_amazon_addtolist() -> None:
    test_obj = AmazonAddToListTest()
    test_obj.announce_test()
    passed_test = test_obj.run_test()
    assert passed_test == True

def test_run_test_amazon_sortbyprice() -> None:
    test_obj = AmazonSortByPriceTest()
    test_obj.announce_test()
    passed_test = test_obj.run_test()
    assert passed_test == True

def _report_test_results(failed_tests: int) -> None:
    print("\n### SUMMARY ###")
    if failed_tests == 0:
        print("All tests passed!")
    else:
        print("One or more tests failed. Please see above output for more information.")
        sys.exit(1)

def run_all_tests() -> None:
    test_objects = [
        AmazonSearchTest(),
        AmazonCartTest(),
        AmazonCheckoutTest(),
        AmazonSignInTest(),
        AmazonAddToListTest(),
        AmazonFilterByCustomerReview(),
        AmazonSortByPriceTest(),
    ]

    failed_tests = 0
    for test_obj in test_objects:
        test_obj.announce_test()
        if not test_obj.run_test():
            failed_tests += 1
    _report_test_results(failed_tests)


def main() -> None:
    run_all_tests()


if __name__ == "__main__":
    main()
