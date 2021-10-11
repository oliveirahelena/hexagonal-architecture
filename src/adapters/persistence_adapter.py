from __future__ import annotations

import sqlite3
from typing import Optional, Tuple

from application.domain import NewProduct, Product
from application.repository import ProductPersistenceInterface


class NewSqLitePersistence:
    @staticmethod
    def get_persistence(conn: sqlite3.Connection) -> SqLitePersistence:
        return SqLitePersistence(conn)


class SqLitePersistence(ProductPersistenceInterface):
    def __init__(self, conn: sqlite3.Connection) -> None:
        self.conn = conn

    def get(self, id: str) -> Tuple[Optional[Product], Optional[Exception]]:
        try:
            stmt = self.conn.execute(
                "SELECT id, name, price, status FROM products WHERE id=?", (id,)
            )

            result = stmt.fetchone()
            product = NewProduct.get_product(result[1], result[2])
            product.id = result[0]
            product.status = result[3]
            return product, None
        except Exception as error:
            return None, error

    def _create(
        self, product: Product
    ) -> Tuple[Optional[Product], Optional[Exception]]:
        try:
            self.conn.execute(
                "INSERT INTO products(id, name, price, status) VALUES(?,?,?,?)",
                (
                    product.get_id,
                    product.get_name,
                    product.get_price,
                    product.get_status,
                ),
            )
            self.conn.commit()
            return product, None
        except Exception as error:
            return None, error

    def _update(
        self, product: Product
    ) -> Tuple[Optional[Product], Optional[Exception]]:
        try:
            self.conn.execute(
                "UPDATE products SET name=?, price=?, status=? WHERE id=?",
                (
                    product.get_name,
                    product.get_price,
                    product.get_status,
                    product.get_id,
                ),
            )
            self.conn.commit()
            return product, None
        except Exception as error:
            return None, error

    def save(self, product: Product) -> Tuple[Optional[Product], Optional[Exception]]:
        stmt = self.conn.execute(
            "SELECT id FROM products WHERE id=?", (product.get_id,)
        )
        result = stmt.fetchone()
        if result is None:
            _, error = self._create(product)
            if error is not None:
                return None, error
        else:
            _, error = self._update(product)
            if error is not None:
                return None, error
        return product, None
