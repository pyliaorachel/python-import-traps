# At the same level of `demo` package,
# run `python3 -m demo.src.app`

'''Incorrect'''
# from util import get_random_emoji
# from src.util import get_random_emoji

'''Correct (relative import)'''
from .util import get_random_emoji

'''Also correct (absolute import)'''
# from demo.src.util import get_random_emoji


def hello():
    emoji = get_random_emoji()
    return 'Hello!{}'.format(emoji)

if __name__ == '__main__':
    print(hello())
