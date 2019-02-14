import datetime
import os

def login(u,p):
    username = u
    password = p
    print("**********LOGIN RESULT**********")
    f=open("users.txt","a")
    f.close()
    f=open("users.txt","r")
    line = f.readlines()
    for x in line:
        list = x.split(',')
        if list[1]==username:
            if list[2]== password:
                print("Hello "+list[0]+"!! Welcome back !!")
                return list[0]
            else:
                print("Wrong username or password")
                return

def reg(fn,un,pw,cpw):
    print("**********REGISTRATION RESULT**********")
    fullname = fn
    username = un
    password = pw
    con_pwd = cpw
    string = fullname + "," + username + "," + password + ",\n"
    if password == con_pwd:
        f = open("users.txt", "a")
        f.close()
        count=0
        f = open("users.txt", "r")
        line = f.readlines()
        f.close()
        for x in line:
            list = x.split(',')
            if username in list:
                count+=1
                print("user present")
                break
        if count == 0:
            f = open("users.txt", "a")
            f.write(string)
            f.close()
            print("Successfully created account.")

    else:
        print("Password not same!")
        return


def userfile(selection,fname,uname):
    sel = selection
    name = uname
    fullname=fname
    cd = os.getcwd()
    fd = os.path.join(cd, r'new_folder')
    if sel == 1:
        print("**********UPLOAD FILE**********")
        #id = input("Id:")
        filepath = input("Enter file name(with fullpath):")
        l=filepath.rfind("\\")
        #print(l)
        filename=filepath[l+1:]
        # type=input("Enter the type of file:")
        desc = input("About the file:")
        upload_date = datetime.date.today()
        date = str(upload_date)
        time = datetime.datetime.now().time()
        time = str(time)
        upload_by = name
        # os.mkdir("D:\\Python\\copy\\" + name)
        if os.path.exists(filepath):
            cd = os.getcwd()
            fd = os.path.join(cd, r'userfiles',name)
            #dest = "D:\\Python\\copy\\" + name
            if not os.path.exists(fd):
                os.makedirs(fd)
                string2 = 'copy ' + filepath + " " + fd
                os.system(string2)
                print("\nSuccessfully Uploaded a file")
            else:
                string2 = 'copy ' + filepath + " " + fd
                os.system(string2)
                print("\nSuccessfully Uploaded a file")
                '''os.mkdir("D:\\Python\\copy\\" + name)
                dest = "D:\\Python\\copy\\" + name
                string2 = 'copy ' + filepath + " " + dest
                os.system(string2)'''
            f=open("files.txt","a")
            f.close()
            f = open("files.txt", "r")
            line=f.readlines()
            f.close()
            count=0
            for x in line:
                count+=1
            id=count+1
            id=str(id)
            dest=fd+"\\"+filename
            f=open("files.txt","a")
            string = id + "," + dest + "," + desc + "," + date + "," + time + "," + upload_by +","+filename+ ",\n"
            f.write(string)
            f.close()
            return
        else:
            print("This file doesn't exist")
            return

    if sel == 2:
        print("**********VIEW FILES**********")
        count=0
        f=open("files.txt","a")
        f.close()
        f = open("files.txt", "r")
        line = f.readlines()
        f.close()
        print("Hi " + fullname + " Your files are here:")
        for x in line:
            list = x.split(',')
            if list[5] == name:
                print("\t\t-->" + list[6] +"\nFile ID:"+list[0]+ "\nAbout:\n" + list[2] + "\nDate:\n" + list[3] + "\nTime:\n" + list[4]+"\n\n")
                count+=1

        if count==0:
            print("No file here")
        else:
            count=str(count)
            print("You have "+count+" files")
            id=input("Enter the id of the file:")
            f=open("files.txt","r")
            lines=f.readlines()
            #count=0
            for y in lines:
                list = y.split(',')
                if id==list[0]:
                    dest=list[1]
                    os.system(dest)
                    break
                #else:
                    #print("Id not found")


    if sel == 3:
        print("**********VIEW SHARED FILES WITH ME*********")
        count=0
        f=open("share.txt","a")
        f.close()
        f = open("share.txt", "r")
        line = f.readlines()
        f.close()
        for x in line:
            list = x.split(',')
            if list[-3] == uname:
                print("\t\t-->" + list[5] +"\nFile ID:"+list[0]+ "\nAbout:\n" + list[2] + "\nShared by:\n" + list[3]+"\n\n")
                count+=1

        if count==0:
            print("No Shared files")
        else:
            id = input("Enter the id of the file:")
            f = open("share.txt", "r")
            lines = f.readlines()
            for y in lines:
                if id == list[0]:
                    dest = list[1]
                    os.system(dest)
                    break

    if sel == 4:
        print("**********SHARE FILES**********")
        count=0
        name = uname
        f=open("files.txt","a")
        f.close()
        f = open("files.txt", "r")
        line = f.readlines()
        f.close()
        for x in line:
            list = x.split(',')
            #print(list[1])
            if list[5] == name:
                #print(list[2])
                count+=1
        if count==0:
            print("No files")
        else:
            id = input("Enter file ID you want to share:")
            whom = input("Enter the username of the person whom you want to share:")
            f=open("users.txt","r")
            c=0
            lines=f.readlines()
            for x in lines:
                list=x.split(',')
                if whom==list[1]:
                    c+=1
            if c==0:
                print("User not present")
            else:
                f = open("files.txt", "r")
                line = f.readlines()
                for y in line:
                    list = y.split(',')
                    # print(list[1])
                    if name==list[5]:
                        if id==list[0]:
                            # print(list[2])
                            string = list[0] + "," + list[1] + "," + list[2] + "," + name + "," + whom +","+list[6]+ ",\n"
                            f = open("share.txt", "a")
                            f.write(string)
                            f.close()
                            print("Shared with " + whom)
                            break

    if sel==5:
        return 5




def mainpage():
    print("**********FILE HOSTING**********")
    print("1.Already have an account?? Want to Login")
    print("2.New User?? Want to Registration")
    choice = int(input("Enter your choice:"))
    return choice

def mainpage2(choice):
    if choice == 1:
        print("**********LOGIN**********")
        username = input("ENTER YOUR USERNAME:")
        password = input("ENTER YOUR PASSWORD:")
        u = login(username, password)
        u = str(u)
        if u == "None":
            print("Invalid login")
            c=mainpage()
            mainpage2(c)
        else:
            def con():
                print("\n1.UPLOAD A NEW FILE\n2.VIEW YOUR FILES\n3.VIEW SHARED FILES TO YOU\n4.SHARE FILE\n5.LOGOUT")
                sel = int(input("ENTER YOUR CHOICE:"))
                a=userfile(sel, u, username)
                if a==5:
                    os.system("cls")
                    print("\nSuccessfully Logout\n")
                    c = mainpage()
                    mainpage2(c)
                else:
                    con()
            con()
    elif choice==2:
        print("**********REGISTRATION**********")
        fullname = input("ENTER YOUR FULLNAME:")
        username = input("ENTER YOUR USERNAME:")
        password = input("ENTER YOUR PASSWORD:")
        con_pwd = input("ENTER YOUR PASSWORD AGAIN:")
        reg(fullname, username, password, con_pwd)
        choice = mainpage()
        mainpage2(choice)
    else:
        print("invalid input")


choice=mainpage()
mainpage2(choice)