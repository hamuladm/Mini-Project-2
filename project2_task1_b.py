'''
Program replaces one line with another\
         & writes or print the result\
      Made by Dmytro Khamula 18.11.22
'''


    #Importing neccessary modules
import argparse
import re


    #Making a parser
parser = argparse.ArgumentParser(description = 'Replaces one line with another')
parser.add_argument(
                    'line1',
                    help = 'Line 1'
                    )
parser.add_argument(
                    'line2',
                    help = 'Line 2'
                    )
parser.add_argument(
                    'filename',
                    help = 'Name of file'
                    )
parser.add_argument(
                    '-in',
                    '--inplace',
                    help = 'Optional argument',
                    action = 'store_true'
                    )
args = parser.parse_args()


    #Main function 1
def line_replace(line1: str, line2: str, filename: str):
    '''
    (str, str, str)

    Function replaces one line with another & writes the result

    '''
    try:
        with open (filename, 'r', encoding = 'utf-8') as file:
            listfile = file.read()
        listfile = re.sub(line1, line2, listfile)
        if args.inplace:        #Checking If there's an optional argument
            with open (filename, 'w', encoding = 'utf-8') as file1:
                file1.write(listfile)
        else:
            print(listfile)
    except TypeError as err:
        print(err)
    except FileNotFoundError:
        print(
            f'There is no {filename} file or directory path is wrong'
            )
    except argparse.ArgumentError:
        print(
              'Print proper argument.\
              For information use [-h] or [--help]'
              )

if __name__ == '__main__':
    line_replace(args.line1, args.line2, args.filename)
