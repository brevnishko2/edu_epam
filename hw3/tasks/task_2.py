"""Calculate total sum of slow_calculate() of all numbers starting from 0 to 500.
 Calculation time should not take more than a minute. Use functional capabilities
 of multiprocessing module. You are not allowed to modify slow_calculate function."""
import time
import struct
import random
import hashlib
from multiprocessing import Pool


def slow_calculate(value):
    """Some weird voodoo magic calculations"""
    time.sleep(random.randint(1, 3))
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack("<" + "B" * len(data), data))


def fast_calculate(value):
    pool = Pool(60)
    return sum(pool.map(slow_calculate, range(value)))


print(fast_calculate(500))
