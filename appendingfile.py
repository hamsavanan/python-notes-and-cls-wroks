
import os

def appending_file(lol_file):
    if(not os.path.exists(lol_file)):
        print('File dont exist:',lol_file)
    else:
        append = input('Enter the content to append: ')
        f = open(lol_file,'a')
        f.write(append + '\n')
        print('Success -> file is appended',lol_file)

def main():
    lol_file = input('Enter the name of the file to append: ')
    appending_file(lol_file)

if __name__ == "__main__":
    main()
