'''Run under sample_package, which is usually not the case'''
# from sample_module import sample_func

'''Run outside sample_package'''
from .sample_module import sample_func
'''or'''
# from sample_package.sample_module import sample_func


if __name__ == '__main__':
    sample_func()
