class SimplifiedEnum(type):
    """Metaclass that simplify access to parameters by setting them
    into class.__dict__[variable] = variable. Variables are taken from
    class.__key parameter.
    """

    def __new__(mcs, name, bases, args):
        obj = super().__new__(mcs, name, bases, args)
        for item in args[f"_{name}__keys"]:
            setattr(obj, item, item)
        obj._content_list__ = [item for item in args[f"_{name}__keys"]]

        return obj

    def __iter__(self):
        self._iteration_list__ = iter(self._content_list__)
        return self

    def __next__(self):
        return next(self._iteration_list__)

    def __len__(self):
        return len(self._content_list__)
