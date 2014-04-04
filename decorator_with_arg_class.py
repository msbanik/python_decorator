class logger:
    def __init__(self, *args, **kwargs):
        print args
        # ('DEBUG', 'TriBug')
        self.args = args
        self.kwargs = kwargs

    def __call__(self, func):
        def outer(*args, **kwargs):
            print args
            # (2, 3)
            func(*args, **kwargs)

        return outer


@logger('DEBUG', 'TriBug')
def sum(x, y):
    print 'Sum of {0} and {1} is: {2}'.format(x, y, x + y)


sum(2, 3)