"""We have a file that works as key-value storage, each like is
 represented as key and value separated by = symbol, example:

name=kek last_name=top song_name=shadilay power=9001

Values can be strings or integer numbers. If a value can be
treated both as a number and a string, it is treated as number.

Write a wrapper class for this key value storage that works like this:

storage = KeyValueStorage('path_to_file.txt') that has its keys and
values accessible as collection items and as attributes.
Example: storage['name'] # will be string
'kek' storage.song # will be 'shadilay'
storage.power # will be integer 9001

In case of attribute clash existing built-in attributes take precedence
 In case when value cannot be assigned to an attribute (for example
 when there's a line 1=something) ValueError should be raised.
 File size is expected to be small, you are permitted to
 read it entirely into memory."""
import string


class WrapperForStorage:
    """Wrapper class for storage. Takes path to file with key=value and
    append it to self.args. Provide access to attr as
    class_instance.key and class_instance['key'].
    Args:
        path: path to file

    Raises:
        ValueError: if key in key=value have incorrect name for attr.
        Example: 1key=value, %key=value

    """

    def __init__(self, path: str):
        with open(path) as inf:
            content = inf.read()
            items = [item.split("=") for item in content.strip().split("\n")]

        available_chars = string.ascii_letters + string.digits + "_" + " "

        for key, value in items:
            # check for correct name
            if not all(char in available_chars for char in key) or key[0].isdigit():
                raise ValueError("incorrect name for attribute name: " + key)
            # append value if it isn't rewriting value in dict
            if key not in self.__dir__():
                if value.isdigit():
                    self.__dict__[key.strip()] = int(value.strip())
                else:
                    self.__dict__[key.strip()] = value.strip()

    def __getitem__(self, item):
        if not isinstance(item, str):
            raise TypeError("Key must be str")
        if item in self.__dict__:
            return self.__dict__[item]
        raise KeyError("This key isn't exist")

    def __setitem__(self, key, value):
        self.__dict__[key] = value
