from tests.hello.hello_selenium import AmazonCartTest

def test_hello_selenium() -> None:
    sut = AmazonCartTest()
    sut.setUp()
    sut.test_add_item_to_cart()
    sut.tearDown()

