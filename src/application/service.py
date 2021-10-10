from typing import Optional, Tuple

from application.domain import Product
from application.repository import ProductPersistenceInterface


class ProductService:
    def __init__(self, persistence: ProductPersistenceInterface):
        self.persistence = persistence

    def get(self, id: str) -> Tuple[Optional[Product], Optional[Exception]]:
        product, error = self.persistence.get(id)
        if error is not None:
            return None, error
        return product, None

    def create(
        self, name: str, price: float
    ) -> Tuple[Optional[Product], Optional[Exception]]:
        pass

    def enable(self, product: Product) -> Tuple[Optional[Product], Optional[Exception]]:
        pass

    def disable(
        self, product: Product
    ) -> Tuple[Optional[Product], Optional[Exception]]:
        pass
