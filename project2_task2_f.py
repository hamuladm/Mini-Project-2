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
def find_sublines(rex: str, path: str, filename: str) -> 1:
    '''

    (str, str, str)

    Function find rex in filename in path

    '''
    count = 0
    for dirpath, dirnames, filenames in os.walk(path):
        dirnames = dirnames.copy
        os.chdir(dirpath)
        for file in filenames:
            match1 = re.findall(filename, file)
            if len(match1) > 0:
                with open (file, 'r', encoding = 'utf_8') as fyle:
                    content = fyle.read()
                match = re.findall(rex, content)
                content = content.split('\n')
                for i in content:
                    if rex in i:
                        line_num = content.index(rex)
                    if len(match) > 0:
                        count += 1
                        if args.show_lines:
                            print (file + '\n')
                            for mat1 in match:
                                print(f'№: {line_num}, reqular expression: {mat1}')
                        for mat in match:
                            print(mat + '\n')
    if args.only_show_counts:
        print(count)
    return 1


if __name__ == '__main__':
    find_sublines(args.rex, args.path, args.filename)
