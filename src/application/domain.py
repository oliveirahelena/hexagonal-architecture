from __future__ import annotations

import uuid
from typing import Optional, Tuple

from application.common import CustomError

DISABLED: str = "disabled"
ENABLED: str = "enabled"


class PriceError(CustomError):
    pass


class StatusError(CustomError):
    pass


class NewProduct:
    @staticmethod
    def get_product(name: str, price: float = 0.0) -> Product:
        product = Product(id=str(uuid.uuid4()), name=name, price=price)
        return product


class Product:
    def __init__(self, id: str, name: str, price: float) -> None:
        self.id: str = id
        self.name: str = name
        self.price: float = price
        self.status = DISABLED

    def is_valid(self) -> Tuple[bool, Optional[Exception]]:
        if self.status == "":
            self.status = DISABLED

        if self.status != ENABLED and self.status != DISABLED:
            return False, StatusError("The status must be enabled or disabled.")

        if self.price < 0:
            return False, PriceError("The price must be greater or equal zero.")

        return True, None

    def enable(self) -> Optional[Exception]:
        if self.price > 0:
            self.status = ENABLED
            return None
        return PriceError("The price must be greater than zero to enable the product.")

    def disable(self) -> Optional[Exception]:
        if self.price == 0:
            self.status = DISABLED
            return None
        return PriceError("The price must be zero to disable the product.")

    @property
    def get_id(self) -> str:
        return self.id

    @property
    def get_name(self) -> str:
        return self.name

    @property
    def get_price(self) -> float:
        return self.price

    @property
    def get_status(self) -> str:
        return self.status
