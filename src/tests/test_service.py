from unittest import mock

from application.domain import PriceError, Product
from application.repository import ProductPersistenceInterface
from application.service import ProductService


def test_product_service_get():
    product = mock.Mock(spec=Product)
    persistence = mock.Mock(spec=ProductPersistenceInterface)
    persistence.get.return_value = (product, None)

    service = ProductService(persistence)
    result, error = service.get("abc")

    assert result == product
    assert error == None


def test_product_service_get_with_error():
    persistence = mock.Mock(spec=ProductPersistenceInterface)
    persistence.get.return_value = (None, Exception)

    service = ProductService(persistence)
    result, error = service.get("abc")

    assert result == None
    assert error == Exception


def test_product_service_create():
    product = mock.Mock(spec=Product)
    persistence = mock.Mock(spec=ProductPersistenceInterface)
    persistence.save.return_value = (product, None)

    service = ProductService(persistence)
    result, error = service.create(name="Product 1", price=10)

    assert result == product
    assert error == None


def test_product_service_create_with_validation_error():
    persistence = mock.Mock(spec=ProductPersistenceInterface)
    persistence.save.return_value = (None, PriceError)

    service = ProductService(persistence)
    result, error = service.create(name="Product 1", price=-10)

    assert result == None
    assert error.message == "The price must be greater or equal zero."


def test_product_service_enable():
    product = mock.Mock(spec=Product)
    product.enable.return_value = None
    persistence = mock.Mock(spec=ProductPersistenceInterface)
    persistence.save.return_value = (product, None)

    service = ProductService(persistence)
    result, error = service.enable(product)

    assert result == product
    assert error == None


def test_product_service_disable():
    product = mock.Mock(spec=Product)
    product.disable.return_value = None
    persistence = mock.Mock(spec=ProductPersistenceInterface)
    persistence.save.return_value = (product, None)

    service = ProductService(persistence)
    result, error = service.disable(product)

    assert result == product
    assert error == None
