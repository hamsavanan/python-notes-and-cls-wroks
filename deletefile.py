import os

def delete_file(file):
    if (not os.path.exists(file)):
        print('File not exists:',file)
    else:
        os.remove(file)
        print('File deleted:', file)

def main():
    file = input('Enter the name of the file to delete: ')
    delete_file(file)

if __name__ == "__main__":
    main()
