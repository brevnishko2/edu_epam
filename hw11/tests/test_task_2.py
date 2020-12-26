from hw11.tasks.task_2 import Order


def morning_discount(order):
    return order.price - order.price * 0.15


def evening_discount(order):
    return order.price - order.price * 0.05


def test_different_discount_is_working():
    order_1 = Order(100, morning_discount)
    assert order_1.final_price() == 85

    order_1.strategy = evening_discount
    assert order_1.final_price() == 95
