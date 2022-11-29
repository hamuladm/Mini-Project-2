'''
Program moves file or directory to another directory \
                     Made by Dmytro Khamula 19.11.22
'''


    #Importing neccessary modules
import os
import argparse


    #Making a parser
parser = argparse.ArgumentParser(
        description =
        'Moves file or directory to another directory'
        )
parser.add_argument(
                    'src',
                    help = 'Current directory'
                    )
parser.add_argument(
                    'dst',
                    help = 'New diretory'
                    )
args = parser.parse_args()


    #Main function
def move_file(src: str, dst: str):
    '''
    (str, str)

    Function moves file or directory to another directory
    '''
    try:
        os.replace(src, dst)
        print(f'File moved succesfully from {src} to {dst}')
    except TypeError as err:
        print(err)
    except argparse.ArgumentError:
        print(
              'Print proper argument.\
              For information use [-h] or [--help]'
              )
    except FileNotFoundError:
        os.replace(src, src)
        print(
              f'There is no {src} directory \
                or new path: {dst} is typed incorrectly'
             )
    except FileExistsError:
        print(
              f'There is no {src} directory \
                or new path: {dst} is typed incorrectly'
             )
    except NotADirectoryError:
        print(
              f'There is no {src} directory \
                or new path: {dst} is typed incorrectly'
             )


if __name__ == '__main__':
    move_file(args.src, args.dst)
