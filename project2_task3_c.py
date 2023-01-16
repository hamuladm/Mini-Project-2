'''
Program makes an archive from src files to dst \
               Made by Dmytro Khamula 25.11.22
'''


# Importing neccessary modules
import zipfile
import argparse
import os


# Making a parser
parser = argparse.ArgumentParser(
                        description =\
        'Archives a file or a directory'
        )
parser.add_argument(
                    'src',
                     help = 'Starting directory or file'
                    )
parser.add_argument(
                    'dst',
                    help = 'Finishing directory'
                    )
args = parser.parse_args()


# Main function
def make_zip(src: str, dst: str):
    '''

    (str, str)

    Function makes an archive from src files to dst

    '''
    try:
        with zipfile.ZipFile (dst, 'w', zipfile.ZIP_DEFLATED) as myzip:
            if os.path.isfile(src):
                myzip.write(src)
            else:
                for root, _, files in os.walk(src):
                    for file in files:
                        myzip.write(os.path.join(root, file))
    except argparse.ArgumentError:
        print(
        'Print proper argument.\
        For information use [-h] or [--help]'
        )
    except TypeError as err:
        print(err)
    except NotADirectoryError as _err:
        print(_err)



if __name__ == '__main__':
    make_zip(args.src, args.dst)
