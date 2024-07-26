import os
import filecmp

def copy_file(file1, file2):
    if not os.path.exists(file1):
        print('File not exists:',file1)
    else:
        f1 = open(file1, 'r')
        lol = f1.read()
        
        f2 = open(file2, 'w')
        f2.write(lol)
        print(f'Success -> Content copied from {file1} to {file2}')


def compare_files(file1,file2):
    if(not os.path.exists(file1)):
        print('File not exists:',file1)
    elif(not os.path.exists(file2)):
        print('File not exists:',file2)
    else:
        compare = filecmp.cmp(file1, file2)
        if compare:
            print('Success -> The files are the same')
        else:
            print('Failure -> The files are different')


def main():
    file1 = input('Enter the name of the file1: ')
    file2 = input('Enter the name of the file2 to be created: ')
    copy_file(file1, file2)



if __name__ == "__main__":
    main()
