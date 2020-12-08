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

        __list_key_value = [item.split("=") for item in content.split()]
        __custom_chars = (string.punctuation + string.digits).replace("_", "")

        for key_value in __list_key_value:
            # check for correct name
            if key_value[0][0] in __custom_chars:
                raise ValueError("incorrect name for attribute name: " + key_value[0])
            # append value if it isnt rewriting value in dict
            if key_value[0] not in self.__dir__():
                try:
                    self.__dict__[key_value[0]] = int(key_value[1])
                except ValueError:
                    self.__dict__[key_value[0]] = str(key_value[1])

    def __getitem__(self, item):
        if item in self.__dict__:
            return self.__dict__[item]
