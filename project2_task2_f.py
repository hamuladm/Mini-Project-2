'''
Program finds a specified regular expression \
                          in specified files \
             Made by Dmytro Khamula 03.12.22
'''


# Importing neccessary modules
import argparse
import os
import re


# Making a parser
parser = argparse.ArgumentParser(
                                 description = 'A parser'
                                 )
parser.add_argument(
                    '--show_lines',
                    help = 'Shows № of line and the line itself',
                    action = 'store_true'
                    )
parser.add_argument(
                    '--only_show_counts',
                    help = 'Shows only amount of matches',
                    action = 'store_true'
                    )
parser.add_argument(
                    'rex',
                    help = 'Regular expression',
                    )
parser.add_argument(
                    'filename',
                    help = 'RE where you should find'
                    )
parser.add_argument(
                    'path',
                    help = 'A path'
                    )
args = parser.parse_args()


# Main function
def find_sublines(rex: str, path: str, filename: str, count = 0) -> 1:
    '''

    (str, str, str) -> 1

    Function find rex in filename in path

    '''
    for dirpath, _, filenames in os.walk(path):
        os.chdir(dirpath)
        for file in filenames:
            if re.match(filename, file):
                with open (file, 'r', encoding = 'utf-8') as file1:
                    content = file1.read().splitlines()
                    count += len(re.findall(rex, file1.read()))
                if args.show_lines:
                    for line in content:
                        if len(re.findall(rex, line)) > 0:
                            print (file)
                            for match in content:
                                if rex in match:
                                    for rexeg in re.findall(rex, line):
                                        print (f'{content.index(match)}:{rexeg}')
                else:
                    if args.only_show_counts:
                        print(count)
                    else:
                        for line in content:
                            if len(re.findall(rex, line)) > 0:
                                print (file)
                                for match in re.findall(rex, line):
                                    print (match)
    return 1


if __name__ == '__main__':
    find_sublines(args.rex, args.path, args.filename)
