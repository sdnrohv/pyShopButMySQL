import mysql.connector
import getpass
import time

def prRed(skk): print("\033[91m {}\033[00m" .format(skk)) 
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk)) 
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk)) 
def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk)) 
def prPurple(skk): print("\033[95m {}\033[00m" .format(skk)) 
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk)) 
def prLightGray(skk): print("\033[97m {}\033[00m" .format(skk)) 
def prBlack(skk): print("\033[98m {}\033[00m" .format(skk)) 

db = mysql.connector.connect(
      host = "localhost",
      user = "root",
      password = "root",
      database = "pysql")

def catFun():
    cursor = db.cursor()                
    query = ("select * from pyshop where category = %s")
    data = (cat, )
    cursor.execute(query, data)
    
    results = cursor.fetchall()
    for x in results:
        print(x)
    cursor.close() 

def queryThing():
    cursor = db.cursor()
    query = ("insert into feedback(name, type, feedback) values(%s, %s, %s)")
    data = (feedbackName, type, feedback)
    cursor.execute(query, data)
    
    db.commit()
    cursor.close()

while True:
    userNameO = input("username : ")
    emailidO = input("enter email : ")
    passwordO = getpass.getpass(prompt = 'password please : ')

    if userNameO == "shubhro" and passwordO == "shubhro":
        while True:
            print("")
            prYellow("HELLO, WELCOME TO PYSHOP")
            print("")
            prRed("buy stuff from our newly optimized pyShop CLI")
            print("")
            print("[USER]   usage : [-v] [-sc] [-sp] [-b] [-q]")
            print("[ADMIN]  usage : [-a] [-r] [-c]")
            print("")

            userAdmin = input("you are a : [USER] / [ADMIN] ").lower()

            #USER

            if userAdmin == "user":        
                print("")
                print("optional arguements: ")
                print("     -v, --view           browse products and view everything")     
                print("     -sc, --searchCat     search by category")
                print("     -sp, --searchPro     search by product name")
                print("     -b, --buy            buy stuff")
                print("     -q, --query          ask us to add some stuff into our database / feedback")

                while True:

                    print("")
                    userInput = input("[USER] pyshop ").lower()
                    print("")    

                    #VIEW
                    if userInput == "-v" or userInput == "--view":
                        cursor = db.cursor()
                        cursor.execute("select * from pyshop")
                        results = cursor.fetchall()
                        for x in results:
                            print(x)
                        cursor.close()            

                    #SEARCH CATEGORY
                    elif userInput == "-sc" or userInput == "--searchcat":    
                        cat = input("category [type [-cat] to see the categories] : ").lower()
                        if cat in ["food", "med", "phone", "laptop", "shoes", "apparel", "books", "appliance"]:                    
                            catFun()

                        elif cat == "-cat":
                            print("search from : [food] [med] [phone] [laptop] [shoes] [apparel] [books] [appliance]")
                            cat = input("select one from above : ")
                            catFun()                        

                        elif cat not in ["food", "med", "phone", "laptop", "shoes", "apparel", "books", "appliance"]:
                            print(f"sorry, the category {cat} hasn't been added on our database yet. Ask us to add stuff through the [-q] or [--query].")                    
                        
                        else:
                            print("bruh.")
                    
                    #SEARCH PRODUCT
                    elif userInput == "-sp" or userInput == "--searchpro":
                        pro = input("what stuff you want : ")

                        cursor = db.cursor()                
                        query = ("select * from pyshop where category = %s")
                        data = (pro, )
                        cursor.execute(query, data)
                        
                        results = cursor.fetchall()
                        for x in results:
                            print(x)
                        cursor.close()                 
                        
                    #BUY

                    #QUERYs
                    elif userInput == "-q" or userInput == "--query":
                        type = input("Type of query \n[AP] add products  [F] feedback    [C] complaint [Q] query : ").lower()
                        print("")
                        if type == "ap":
                            feedbackName = input("username : ")
                            feedback = input("product that should be added : ").capitalize()
                            queryThing()
                            print(f"thank you for making our platform better! {feedback} will be added soon.")

                        elif type == "f":
                            feedbackName = input("username : ")
                            feedback = input("feedback : ")
                            queryThing()
                            print(f'feedback "{feedback}" has been submitted. Thank you for helping us making pyShop better!')

                        elif type == "c":
                            feedbackName = input("username : ")
                            feedback = input("complaint : ")
                            queryThing()
                            print(f'your complaint "{feedback}" has been submitted. Thank you for helping us making pyShop better!')
                
                        elif type == "q":
                            feedbackName = input("email-id : ")
                            feedback = input("query : ")
                            queryThing()
                            print(f"thanks for reaching out to us! check {feedbackName} in a couple of days and we'll get right back @You.")

                        else:
                            print("what bRuh? are you retarded?")                           
                            
                    #LOGOUT
                    elif userInput == "logout()" or userInput == "exit()":
                        print("sure boss!")
                        time.sleep(2)
                        break

                    #HELP
                    else:
                        print("-------------------------") 
                        print("")  
                        print("-v, --view           to view the catalogue")              
                        print("-sc, --searchCat     to add products")
                        print("-sp, --searchPro     to remove products")
                        print("-b, -buy             to buy stuff") 
                        print("-q, --query          to ask us to add stuff") 
                        print("--help               to see the commands")
                        print("exit(), logout()     to log out")
                        print("")
                        print("-------------------------")    
                                


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
                            b = input("item name :      ").lower()
                            c = input("category :       ").lower()
                            d = input("amount of stock: ").lower()
                            e = input("company :        ").lower()
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
                            rmvObj = input("object name that need to be removed : ").lower()

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

            elif userAdmin == "i love you":
                print("i love you too")  
                time.sleep(1)
                break
            
            else:
                print("bruh")
                time.sleep(1)
                break
