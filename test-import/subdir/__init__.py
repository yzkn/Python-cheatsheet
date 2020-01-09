from glob import glob
from importlib import import_module
import os
import re
import sys

def main():
    myself = sys.modules[__name__]
    mod_paths = glob(os.path.join(os.path.dirname(os.path.abspath(__file__)), '*.py'))
    for py_file in mod_paths:
        mod_name = os.path.splitext(os.path.basename(py_file))[0]
        if re.search('.*__init__.*',mod_name) is None:
            mod = import_module(__name__+ '.' + mod_name)
            for m in mod.__dict__.keys():
                if not m in ['__builtins__', '__doc__', '__file__', '__name__', '__package__']:
                    myself.__dict__[m] = mod.__dict__[m]
main()
