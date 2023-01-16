'''
Program makes an archive with all files that have common re \
                           Made by Dmytro Khamula 25.11.22
'''


# Importing neccessary modules
from zipfile import ZipFile
import argparse
import re
import os


# Making a parser
parser = argparse.ArgumentParser(
                        description =\
            'Makes an archive with common re'
            )
parser.add_argument(
                    'rex',
                    help = 'Regular expression'
                    )
parser.add_argument(
                    'zipfile',
                    help = 'Zipfile from whicn should read'
                    )
parser.add_argument(
                    'new_zipfile',
                    help = 'Zipfile in which should write'
                    )
args = parser.parse_args()


# Main function
def find_re(zipfile: str, rex: str, new_zipfile: str):
    '''

    (str, str, str)

    Function makes an archive (new_zipfile) from zipfile \
        if file has a rex in it

    '''
    try:
        with ZipFile (zipfile, 'r') as myzip:
            nameslist = myzip.namelist()
            myzip.extractall()
        with ZipFile (new_zipfile, 'w') as myzip2:
            for file in nameslist:
                if os.path.isfile(file):
                    with open (file, 'r', encoding = 'utf-8') as file1:
                        if len(re.findall(rex, file1.read())) > 0:
                            myzip2.write(file)
    except argparse.ArgumentError:
        print(
        'Print proper argument.\
        For information use [-h] or [--help]'
        )
    except TypeError as err:
        print(err)


if __name__ == '__main__':
    find_re(args.zipfile, args.rex, args.new_zipfile)
