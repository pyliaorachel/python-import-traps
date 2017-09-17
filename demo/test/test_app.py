# At the same level of `demo` package,
# run `python3 -m demo.test.test_app`

# Note: here we don't use popular python testing packages
# as this is a light-weight demo

'''Incorrect'''
# from src.app import hello
# import ..const

'''Correct (absolute import)'''
from demo.src.app import hello
from demo import const

'''Also correct (relative import)'''
# from ..src.app import hello
# from .. import const

def test_hello():
    hello_msg = hello()
    if not hello_msg.startswith('Hello!'):
        print('{}: hello message incorrect'.format(const.TEST_FAIL_MSG))
    else:
        print(const.TEST_PASS_MSG)

if __name__ == '__main__':
    test_hello()
