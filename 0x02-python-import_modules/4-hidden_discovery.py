#!/usr/bin/python3

import importlib.util
import sys

def print_hidden_names(pyc_file):
    spec = importlib.util.spec_from_file_location("module_name", pyc_file)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    names = sorted(dir(module))
    for name in names:
        if not name.startswith('__'):
            print(name)

if __name__ == "__main__":
    if sys.version_info.major == 3 and sys.version_info.minor >= 8:
        print_hidden_names("hidden_4.pyc")
    else:
        print("Please make sure you are running Python 3.8.x.")
