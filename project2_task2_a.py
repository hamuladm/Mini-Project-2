'''
Program makes a tree from path\
Made by Dmytro Khamula 27.11.22
'''


# Importing neccessary modules
import os
import argparse

# Making a parser
parser = argparse.ArgumentParser(
    description = 'Makes a tree'
)
parser.add_argument(
    'path',
    help = 'A path'
)
args = parser.parse_args()


# Main function
def tree (path: str):
    '''
    (str)

    Function makes a tree from path

    '''
    try:
        for dirpath, dirnames, filenames in os.walk(path):
            dirnames = dirnames.copy
            count = dirpath.count('/')
            print ('└──', '──'*count, '├─', dirpath.split('/')[-1]+'/')
            for filename in filenames:
                print('│', '  ', '  '*count, '└──', filename)
    except argparse.ArgumentError:
        print(
              'Print proper argument.\
              For information use [-h] or [--help]'
              )
    except NotADirectoryError:
        print(
            f'There is no {path} directory'
            )


if __name__ == '__main__':
    tree(args.path)
