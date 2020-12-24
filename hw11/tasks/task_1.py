class SimplifiedEnum(type):
    """Metaclass that simplify access to parameters by setting them
    into class.__dict__[variable] = variable. Variables are taken from
    class.__key parameter.
    """

    def __new__(mcs, name, bases, args):
        obj = super().__new__(mcs, name, bases, args)
        for arg in args["_%s__keys" % name]:
            exec('%s = "%s"\nobj.%s = %s' % (arg, arg, arg, arg))
        return obj
