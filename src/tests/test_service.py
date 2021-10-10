from application.domain import Product
from unittest import mock

from application.service import ProductService
from application.repository import ProductPersistenceInterface


def test_product_service_get():
    product = mock.Mock(spec=Product)
    persistence = mock.Mock(spec=ProductPersistenceInterface)
    persistence.get.return_value = (product, None)

    service = ProductService(persistence)
    result, error = service.get("abc")

    assert result == product
    assert error == None


def test_product_service_get_with_no_product():
    persistence = mock.Mock(spec=ProductPersistenceInterface)
    persistence.get.return_value = (None, Exception)

    service = ProductService(persistence)
    result, error = service.get("abc")

    assert result == None
    assert error == Exception
