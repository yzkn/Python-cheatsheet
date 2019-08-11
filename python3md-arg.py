import sys

args = sys.argv
print(args)

for i, arg in enumerate(args):
    print('第{}引数: {}'.format(i, args[i]))