from __future__ import print_function

import argparse

# 5. Decorator
# Decorate your programs with a decorator which prints the function arguments in the func_name(args) format (for instance fib(6).

def decofull(function_to_decorate):
    def wrapper(*args, **kwargs):
        print(function_to_decorate.func_name +": "),
        print(args) if args is not None else (print(kwargs))
        function_to_decorate(*args, **kwargs)
    return wrapper

# decofull(321)
#
# fib_decorated = decofull(fibn)
# fib_decorated(7)
#
# arnums_decorated = decofull(arnums)
# arnums_decorated(1,2,3,8,9)
