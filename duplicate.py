import os
import filecmp

def copy_file(file1, file2):
    if not os.path.exists(file1):
        print('File does not exist:', file1)
        return

    f1 = open(file1,'r')
    content = f1.read()
    
    f2 = open(file2,'w')
    f2.write(content)
    
    print(f'Success -> Content copied from {file1} to {file2}')
    compare_files(file1,file2)

def compare_files(file1,file2):
    if (not os.path.exists(file1)):
        print('File does not exist:',file1)
        return
    elif (not os.path.exists(file2)):
        print('File does not exist:',file2)
        return

    if filecmp.cmp(file1,file2):
        print('Success -> The files are the same')
        delete_file_choice = input(f'Do you want to delete {file2}? (yes/no): ')
        if delete_file_choice.lower() == 'yes':
            os.remove(file2)
            print(f'{file2} has been deleted')
    else:
        print('The files are different')

def main():
    file1 = input('Enter the name of the first file: ')
    file2 = input('Enter the name of the second file: ')
    copy_file(file1, file2)

if __name__ == "__main__":
    main()
