import sys
import os
import glob

sys.path.append("../")
import pkgutil

def get_examples(module):
    dir = os.path.dirname(module.__file__)
    print dir
    def is_module(d):
        return d.endswith('py') and not d.startswith('__')

    return filter(is_module, os.listdir(dir))


import examples
"""
def run_main_test():
    exs = get_examples(examples)

    for ex in exs:
        ex_module = "examples." + ex.replace(".py", '')
        print ex_module
        p = __import__(ex_module)
        m = getattr(p, 'run_main', None)
        print m
        
        
if __name__ == '__main__':
    run_main_test()
"""