import os
import filecmp

def Comparefiles(filename1,filename2):
    if(not os.path.exists(filename1)):
        print('File not exists:',filename1)
    elif(not os.path.exists(filename2)):
        print('File not exists:',filename2)
    else:
        compare = filecmp.cmp(filename1,filename2)
        if compare == True:
            print('Success-> The files are same')
        else:
            print('Failure -> The files are different')    



def main():
    file_01 = input('Enter the first file name')
    file_02 = input('Enter the second file name')
    Comparefiles(file_01,file_02)



if __name__=="__main__":
    main()
