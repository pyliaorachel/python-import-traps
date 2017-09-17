print('A started importing')

from .B import B_greet_back

print('A finished importing')


def A_say_hello():
    print('A says hello!')
    B_greet_back()

print('A finished defining A_say_hello')

def A_greet_back():
    print('A says hello back!')

print('A finished defining A_greet_back')

if __name__ == '__main__':
    A_say_hello()
