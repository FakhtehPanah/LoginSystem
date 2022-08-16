#SigningUp
def register():
    db = open('database.txt', 'r')
    username = input("Create your Username ... ")
    password = input("Create your Password ... ")
    confirmpass = input("Enter your your password once again")
    u = []
    p = []
      
    for i in db:
        a,b = i.split(", ")
        b = b.strip()
        u.append(a)
        p.append(b)
    data = dict(zip(u,p))
    
    if password != confirmpass:
        print("these passwords don`t match ! ")
        register()
    else:
        if len(password) <= 6:
            print("Password too short... ")
            register()
        elif username in u:
            print("Username already exists...")
            register()
        else:
            db = open('database.txt', 'a')
            db.write(username + ", " + password)
            print("done successfuly")



#SingingIn
def enter():
    db = open('database.txt', 'r')
    username = input("Enter your Username ... ")
    password = input("Enter your Password ... ")
    u = []
    p = []

    for i in db:
        a,b = i.split(", ")
        b = b.strip()
        u.append(a)
        p.append(b)
    data = dict(zip(u,p))

    try:
        if data[username]:
            if password == data[username]:           
                print("Hi, "+ username)
            else:
                print("Username or Password incorrect !")
        else:
            print("Username dosen`t exist !")
    except:
        print("Login Error Function")

#Check...
def home():
    options = input("singing OR singup ")
    if options == "singing":
        enter()
    else:
        register()

home()


    
    
    
    
    
    
    

