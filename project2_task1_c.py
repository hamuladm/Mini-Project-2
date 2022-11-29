'''
Program encrypts a text from file\
  Made by Dmytro Khamula 18.11.22
'''


    #Importing neccessary modules
import argparse
import string

    #Making a parser
parser = argparse.ArgumentParser(description = 'Caesar encryption')
parser.add_argument(
                    '-off',
                    '--offset',
                    help = 'How do you want to encrypt',
                    type = int
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
parser.add_argument(
                    '--decrypt',
                    help= 'Decrypting file'
                    )
args = parser.parse_args()


    #Main function
def caesar(filename: str):
    '''
    (str) -> str

    Function encrypts a text from file

    '''
    try:
        small_let_eng = string.ascii_lowercase
        big_let_eng = string.ascii_uppercase
        small_let_ukr = 'абвгдеєжзиіїйклмнопрстуфхчшщьюя'
        big_let_ukr = small_let_ukr.upper()
        encrypted = ''
        with open (filename, 'r', encoding = 'utf-8') as file:
            content = file.read()
        if args.decrypt:
            with open (filename, 'w', encoding = 'utf-8') as file1:
                file1.write(content)
        for crypt in content:
            if crypt.isalpha():
                if args.offset:     #Checking If there's a specified offset
                    if crypt.islower():
                        if crypt in small_let_eng:
                            encrypted +=\
                                small_let_eng[(small_let_eng.index(crypt) + args.offset) % 26]
                        elif crypt in small_let_ukr:
                            encrypted +=\
                                 small_let_ukr[(small_let_ukr.index(crypt) + args.offset) % 31]
                    if crypt.isupper():
                        if crypt in big_let_eng:
                            encrypted += big_let_eng[(big_let_eng.index(crypt) + args.offset) % 26]
                        elif crypt in big_let_ukr:
                            encrypted +=\
                                 big_let_ukr[(big_let_ukr.index(crypt) + args.offset) % 31]
                else:
                    if crypt.islower():
                        if crypt in small_let_eng:
                            encrypted += small_let_eng[(small_let_eng.index(crypt) + 13) % 26]
                        elif crypt in small_let_ukr:
                            encrypted +=\
                                 small_let_ukr[(small_let_ukr.index(crypt) + 13) % 31]
                    if crypt.isupper():
                        if crypt in big_let_eng:
                            encrypted += big_let_eng[(big_let_eng.index(crypt) + 13) % 26]
                        elif crypt in big_let_ukr:
                            encrypted += big_let_ukr[(big_let_ukr.index(crypt) + 13) % 31]
            else:
                encrypted += crypt
        if args.inplace:        #Checking If there's an optional argument
            with open (filename, 'w', encoding = 'utf-8') as file1:
                file1.write(encrypted)
        else:
            print(encrypted)
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
    caesar(args.filename)
