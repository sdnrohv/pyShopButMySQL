import mysql.connector
import getpass
import time

db = mysql.connector.connect(
      host = "localhost",
      user = "root",
      password = "root",
      database = "pysql")

# while True:
#     userName = input("username : ")
#     emailid = input("enter email : ")
#     password = input("password : ")


#     cursor = db.cursor()
#     query = ("select exists(select username from user_db where username = %s and password = %s)")
#     data = (userName, password, )
#     cursor.execute(query, data)
#     db.commit()

def catFun():
    cursor = db.cursor()                
    query = ("select * from pyshop where category = %s")
    data = (cat, )
    cursor.execute(query, data)
    results = cursor.fetchall()
    for x in results:
        print(x)
    cursor.close() 


while True:
    print("")
    print("HELLO, WELCOME TO PYSHOP")
    print("")
    print("buy stuff from our newly optimized pyShop CLI")
    print("")
    print("[USER]   usage : [-sc] [-sp] [-b] [-v] [-q]")
    print("[ADMIN]  usage : [-a] [-r] [-c]")
    print("")

    userAdmin = input("you are a : [USER] / [ADMIN] ") 

    #USER

    if userAdmin == "user":        
        print("")
        print("optional arguements: ")        
        print("     -sc, --searchCat     search by category")
        print("     -sp, --searchPro     search by product name")
        print("     -b, --buy            buy stuff")
        print("     -v, --view           browse products and view everything")
        print("     -q, --query          ask us to add some stuff into our database / feedback")

        while True:

            print("")
            userInput = input("[USER] pyshop ") 
            print("")               

            #SEARCHCAT
            if userInput == "-sc" or userInput == "--searchCat":    
                cat = input("category [type [-cat] to see the categories] : ")
                if cat != "-cat":                    
                    catFun()

                elif cat == "-cat":
                    print("search from : [food] [med] [phone] [laptop] [shoes] [apparel] [books] [appliance]")
                    cat = input("select one from above : ")
                    catFun()                        

                elif cat not in ["food", "med", "phone", "laptop", "shoes", "apparel", "books", "appliance"]:
                    print("sorry, the category hasn't been added on our database yet. Ask us to add stuff through the [-q] or [--query].")                    
                
                else:
                    print("bruh.")
            
            #SEARCH PRODUCT
            if userInput == "-sp" or userInput == "--searchPro":    
                pro = input("product name : ")
                if pro != "-cat":                    
                    catFun()

                elif cat == "-cat":
                    print("search from : [food] [med] [phone] [laptop] [shoes] [apparel] [books] [appliance]")
                    cat = input("select one from above : ")
                    catFun()                        

                elif cat not in ["food", "med", "phone", "laptop", "shoes", "apparel", "books", "appliance"]:
                    print("sorry, the category hasn't been added on our database yet. Ask us to add stuff through the [-q] or [--query].")                    
                
                else:
                    print("bruh.")
            #BUY
            #QUERY
            #VIEW
                    
            #LOGOUT
            if userInput == "logout()" or userInput == "exit()":
                break


    #ADMIN

    elif userAdmin == "admin":
        adminPass = getpass.getpass(prompt='enter admin password ')
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

    else:
        print("what the fuck did you just type you fcking uneducated bitchass hoe i am kicking you out")  
        time.sleep(10)
        break
