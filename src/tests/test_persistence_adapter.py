from adapters.persistence_adapter import NewSqLitePersistence
from application.domain import NewProduct


def test_persistence_get(setup_database):
    conn = setup_database
    persistence = NewSqLitePersistence.get_persistence(conn)
    product, error = persistence.get(id="abc")
    assert error is None
    assert product.get_name == "Product Test"
    assert product.get_price == 0.0
    assert product.get_status == "disabled"


def test_persistence_save(setup_database):
    conn = setup_database
    persistence = NewSqLitePersistence.get_persistence(conn)

    product = NewProduct.get_product(name="Product Test", price=25)

    product_result, error = persistence.save(product)

    assert error is None
    assert product.get_name == product_result.get_name
    assert product.get_price == product_result.get_price
    assert product.get_status == product_result.get_status

    product.status = "enabled"

    product_result, error = persistence.save(product)

    assert error is None
    assert product.get_name == product_result.get_name
    assert product.get_price == product_result.get_price
    assert product.get_status == product_result.get_status
