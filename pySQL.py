import mysql.connector
import getpass

db = mysql.connector.connect(
      host = "localhost",
      user = "root",
      password = "root",
      database = "pysql")

print("you need to login to see further information")

# while True:
#     userName = input("username : ")
#     emailid = input("enter email : ")
#     password = input("password : ")


#     cursor = db.cursor()
#     query = ("select exists(select username from user_db where username = %s and password = %s)")
#     data = (userName, password, )
#     cursor.execute(query, data)
#     db.commit()


while True:
    print("")
    print("HELLO, WELCOME TO PYSHOP")
    print("")
    print("buy stuff from our newly optimized pyShop CLI")
    print("just login")
    print("")
    print("[USER]   usage : [-sc] [-sp] [-b] [-v]")
    print("[ADMIN]  usage : [-a] [-r] [-c]")
    print("")

    userAdmin = input("you are a  (user / admin) : ") 

    #USER

    if userAdmin == "user":
        print("optional arguements: ")        
        print("     -sc, --searchCat     search by category")
        print("     -sp, --searchPro     search by product name")
        print("     -b, --buy            buy stuff")
        print("     -v, --view           browse products") 

        userInput = input("what you wanna do : ")

        #SEARCHCAT
        if userInput == "-sc" or userInput == "--searchCat":
            cat = input("category : [type -cat to see the categories] : ")
            if cat != "-cat":
                cursor = db.cursor
                query = 
            


    #ADMIN

    elif userAdmin == "admin":
        adminPass = getpass.getpass(prompt='enter admin password : ')
        if adminPass != "shubhro" and adminPass != "anand":
            print("please don't hack us :3 🙂🙂🙂")

        elif adminPass == "shubhro" or adminPass == "anand":
            print("")
            print("optional arguements")
            print("     -a, --add           to add products")
            print("     -r, --remove        to remove products")
            print("     -c, --check         to check the stocks")

            while True:
                print("")
                adminInput = input("[ADMIN] pyshop ")
                print("")

                #ADD
                if adminInput == "--add" or adminInput == '-a':
                    a = int(input("object id :      "))
                    b = input("item name :      ")
                    c = input("category :       ")
                    d = input("amount of stock: ")
                    e = input("company :        ")
                    print("")

                    cursor = db.cursor()
                    query = ("insert into pyshop(obj_id, item_name, category, stock, company) values(%s, %s, %s, %s, %s)")
                    data = (a, b, c, d, e)
                    cursor.execute(query, data)
                    db.commit()
                    cursor.execute("select * from pyshop")
                    results = cursor.fetchall()
                    for x in results:
                        print(x)
                    cursor.close()

                #REMOVE
                elif adminInput == "--remove" or adminInput == "-r":
                    rmvObj = input("object name that need to be removed : ")

                    cursor = db.cursor()
                    query = ("delete from pyshop where item_name = %s")
                    data = (rmvObj, )
                    cursor.execute(query, data)
                    db.commit()
                    cursor.execute("select * from pyshop")
                    results = cursor.fetchall()
                    for x in results:
                        print(x)
                    cursor.close()

                #SEE
                elif adminInput == "--check" or adminInput == "-c":
                    cursor = db.cursor()
                    cursor.execute("select * from pyshop")
                    results = cursor.fetchall()
                    for x in results:
                        print(x)
                    cursor.close()

                #LOGOUT                 
                elif adminInput == "logout()":
                    break

                #HELP
                else:
                    print("-------------------------") 
                    print("")               
                    print("-a, --add    to add products")
                    print("-r, --remove to remove products")
                    print("-c, --check  to check stock") 
                    print("--help       to see the command")
                    print("logout()     to log out")
                    print("")
                    print("-------------------------")                       