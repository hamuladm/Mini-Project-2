'''
Program finds and deletes line from file\
           & writes or prints the result\
         Made by Dmytro Khamula 18.11.22
'''


    #Importing neccessary modules
import argparse
import re


    #Making a parser
parser = argparse.ArgumentParser(description = 'Finds & deletes the line')
parser.add_argument(
                    'line',
                    help = 'Finds specified line'
                    )
parser.add_argument(
                    'filename',
                    help = 'File'
                    )
parser.add_argument(
                    '-in',
                    '--inplace',
                    help = 'Optional argumnet',
                    action = 'store_true'
                    )
args = parser.parse_args()


    #Main function
def line_del(filename: str, line: str) -> str:
    '''
    (str, str) -> str

    Function finds and deletes line from file & writes or prints the result

    '''
    try:
        with open (filename, 'r', encoding = 'utf-8') as file:
            listfile = file.read()
        listfile = re.sub(line, '', listfile)
        if args.inplace:       #Checking If there's an optional argument
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
    line_del(args.filename, args.line)
