from application.domain import ENABLED, NewProduct


def test_enable_product_with_price_greater_than_zero():
    product = NewProduct.get_product(name="Hello", price=10)
    result = product.enable()
    assert result is None


def test_enable_product_with_price_equal_or_less_than_zero():
    product = NewProduct.get_product(name="Hello")
    result = product.enable()
    assert (
        result.message == "The price must be greater than zero to enable the product."
    )


def test_disable_product_with_price_greater_than_zero():
    product = NewProduct.get_product(name="Hello", price=10)
    product.status = ENABLED
    result = product.disable()
    assert result.message == "The price must be zero to disable the product."


def test_enable_product_with_price_equal_zero():
    product = NewProduct.get_product(name="Hello")
    product.status = ENABLED
    result = product.disable()
    assert result is None


def test_is_valid_product_with_valid_attributes():
    product = NewProduct.get_product(name="Hello", price=10)
    result = product.is_valid()
    assert result[0] is True
    assert result[1] is None


def test_is_valid_product_with_not_valid_status():
    product = NewProduct.get_product(name="Hello", price=10)
    product.status = "INVALID"
    result = product.is_valid()
    assert result[0] is False
    assert result[1].message == "The status must be enabled or disabled."


def test_is_valid_product_with_not_valid_price():
    product = NewProduct.get_product(name="Hello", price=-10)
    result = product.is_valid()
    assert result[0] is False
    assert result[1].message == "The price must be greater or equal zero."
