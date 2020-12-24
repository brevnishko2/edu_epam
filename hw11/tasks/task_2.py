from typing import Callable, Union


class Order:
    """Class for calculation final price of item."""

    def __init__(self, price: int, discount: Callable[[], Union[float, int]] = None):
        """
        Args:
            price: standard price of item
            discount: function that return percentage of discount.
            Function's return must be int/float.

        """
        self.price = price
        if discount:
            self.discount = discount()
        else:
            self.discount = 0

    def final_price(self):
        return self.price - self.price * self.discount
