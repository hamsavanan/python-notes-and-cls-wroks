def StaffDetails(**kwargs):
    for key, value in kwargs.items():
        print(f'{key} is {value}')
def main():
    changepond = {'Name':'Hamsa','Age':23,'MobileNo':6374748871}
    StaffDetails(**changepond)

if __name__ == "__main__":
    main()



