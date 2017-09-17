print('B started importing')

'''Incorrect'''
# from .A import A_greet_back       # circular import
# from ..sample_package import A    # above top-level package

'''Correct'''
from . import A

print('B finished importing')


def B_say_hello():
    '''Correct (deferred import, ugly)'''
    # from .A import A_greet_back

    print('B says hello!')
    # A_greet_back()
    A.A_greet_back()

print('B finished defining B_say_hello')

def B_greet_back():
    print('B says hello back!')

print('B finished defining B_greet_back')

if __name__ == '__main__':
    B_say_hello()
