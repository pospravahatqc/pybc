# 4. Use CLI config for your two programs
#
# Create a Python's module, which allows you to run numbers and fibonacci programs.
# The module has to be in the repo root. The program will be selected based on provided arguments.
# For instance, python app.py --fib ... will run the fibonacci program.
# Please don't forget about additinal agruments which may be required by selected program. Use if __name__ == '__main__': to configure app.py.

from app_code import arnums
from app_code import fibn

import sys

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print "Enter sub-program to run / '--fib' or '--numbers'"
    param_name = sys.argv[1]
    if len(sys.argv) == 2:
        print "Enter input params as next param after program to run. Ex. '7'"
    else:
        param_value = sys.argv[2]
        if param_name == "--fib":
            print(fibn(int(param_value)))
        elif param_name == "--numbers":
            print(arnums(tuple(param_value)))
    print("Entered param name " + param_name)
    print("Entered param value " + param_value)

# some issue with numbers exist