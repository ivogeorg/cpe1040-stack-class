# An example of how to raise an exception on getting bad input

sample = 6

def expect_int(i):
    if not isinstance(i, type(sample)):
        raise ValueError('Expected integer but got {}'.format(type(i)))
    else:
        print('Got an integer value {}'.format(i))


expect_int(5)
expect_int(5.13)

