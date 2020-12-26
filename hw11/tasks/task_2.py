from __future__ import annotations
from typing import Callable, Union


class Order:
    """Class for calculation final price of item."""

    def __init__(
        self, price: int, strategy: Callable[[Order], Union[float, int]] = None
    ):
        """
        Args:
            price: standard price of item
            strategy: function that return percentage of strategy.
            Function's return must be int/float.

        """
        self.price = price
        self._strategy = strategy

    @property
    def strategy(self):
        return self._strategy

    @strategy.setter
    def strategy(self, strategy):
        self._strategy = strategy

    def final_price(self):
        return self.strategy(self)
