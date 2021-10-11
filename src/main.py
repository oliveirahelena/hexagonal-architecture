import sqlite3

from adapters.persistence_adapter import NewSqLitePersistence
from application.service import NewProductService

conn = sqlite3.connect("db.sqlite")

conn.execute(
    """CREATE TABLE IF NOT EXISTS products (
        "id" string,
        "name" string,
        "price" float,
        "status" string
    );"""
)

persistence = NewSqLitePersistence.get_persistence(conn)
service = NewProductService.get_service(persistence)
product, error = service.create(name="Product Exemple", price=30)

service.enable(product)

conn.close()
