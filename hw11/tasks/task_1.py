class SimplifiedEnum(type):
    """Metaclass that simplify access to parameters by setting them
    into class.__dict__[variable] = variable. Variables are taken from
    class.__key parameter.
    """

    def __new__(mcs, name, bases, args):
        obj = super().__new__(mcs, name, bases, args)
        obj._content_list__ = args[f"_{name}__keys"]
        for item in args[f"_{name}__keys"]:
            setattr(obj, item, item)

        return obj

    def __iter__(cls):
        return iter(cls._content_list__)

    def __len__(cls):
        return len(cls._content_list__)
