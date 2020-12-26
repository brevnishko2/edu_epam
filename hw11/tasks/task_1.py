class SimplifiedEnum(type):
    """Metaclass that simplify access to parameters by setting them
    into class.__dict__[variable] = variable. Variables are taken from
    class.__key parameter.
    """

    def __new__(mcs, name, bases, args):
        new_dict = {f"{arg}": arg for arg in args[f"_{name}__keys"]}
        mcs.obj = super().__new__(mcs, name, bases, new_dict)
        mcs.obj.__iter__ = SimplifiedEnum.__iter__
        mcs.obj.__next__ = SimplifiedEnum.__next__
        mcs.obj.__len__ = SimplifiedEnum.__len__

        return mcs.obj

    def __iter__(self):
        self._iteration_list__ = [
            item for item in self.__dir__() if not item.endswith("__")
        ]
        self._iter_counter__ = 0
        return self

    def __next__(self):
        if self._iter_counter__ < len(self._iteration_list__):
            result = self._iteration_list__[self._iter_counter__]
            self._iter_counter__ += 1
            return result
        else:
            raise StopIteration

    def __len__(self):
        counter = [item for item in self]
        return len(counter)
