#------------------------
#program: PJ1V2.0
#------------------------
from tkinter import *
from tkinter import messagebox
import sqlite3
#---------------Functions--------------------
def connectionDB():
    myConnection = sqlite3.connect("CSC-T_105-161")
    myCursor = myConnection.cursor()

    try:
        myCursor.execute('''
            CREATE TABLE Space_Facts(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Planet VARCHAR(50),
            Diameter_km VARCHAR (50),
            Distance_km VARCHAR (50),
            Year_Length VARCHAR (50))
        ''')
        messagebox.showinfo("DB", "Database and Table created successfully!")
    except:
        messagebox.showwarning("Attention!", "Database already exists.")

def exitApplication():
    value = messagebox.askquestion("Exit", "Would you like to exit the application?")
    if value == "yes":
        root.destroy()

def clearFields():
    myid.set("")
    myplanet.set("")
    mydiameter.set("")
    mydistance.set("")
    myyear.set("")
#36    

def create():
    myConnection = sqlite3.connect("CSC-T_105-161")
    myCursor = myConnection.cursor()

    data=myplanet.get(),mydiameter.get(),mydistance.get(),myyear.get()
    myCursor.execute("INSERT INTO Space_Facts VALUES(NULL,?,?,?,?)", (data))

       
    myConnection.commit()
    messagebox.showinfo("DB", "Record inserted successfully!")

def read():
    myConnection=sqlite3.connect("CSC-T_105-161")
    myCursor = myConnection.cursor()
    myCursor.execute("SELECT * FROM Space_Facts WHERE ID="+myid.get())
    all_planets=myCursor.fetchall()
    for planet in all_planets:
        myid.set(planet[0])
        myplanet.set(planet[1])
        mydiameter.set(planet[2])
        mydistance.set(planet[3])
        myyear.set(planet[4])
    myConnection.commit()

def update():
    myConnection = sqlite3.connect("CSC-T_105-161")
    myCursor = myConnection.cursor()
    data=(myplanet.get(), mydiameter.get(), mydistance.get(), myyear.get())

    myCursor.execute(
        "UPDATE Space_Facts SET Planet=?, Diameter_km=?, Distance_km=?, Year_Length=? WHERE ID=" + myid.get(),(data))
    
    myConnection.commit()
    messagebox.showinfo("DB", "Updated successfully")
   
    
####### COME BACK TO THIS 

def delete():
    myConnection=sqlite3.connect("CSC-T_105-161")
    myCursor=myConnection.cursor()
    myCursor.execute("DELETE FROM Space_Facts WHERE ID="+ myid.get())
    myConnection.commit()
    messagebox.showinfo("DB","Deleted Successfully!")

#------------ Tkinter GUI Setup ------------
root = Tk()
barMenu = Menu(root)
root.config(menu=barMenu, width=300, height=300)

dbMenu = Menu(barMenu, tearoff=0)
dbMenu.add_command(label="Connect", command=connectionDB)
dbMenu.add_command(label="Exit", command=exitApplication)

deleteMenu=Menu(barMenu,tearoff=0)
deleteMenu.add_command(label="Delete Field(s)",command=clearFields)

crudMenu = Menu(barMenu, tearoff=0)
crudMenu.add_command(label="Create", command=create)
crudMenu.add_command(label="Read", command=read)
crudMenu.add_command(label="Update", command=update)
crudMenu.add_command(label="Delete", command=delete)

helpMenu=Menu(barMenu,tearoff=0)
helpMenu.add_command(label="Project Space_Facts")

barMenu.add_cascade(label="Database", menu=dbMenu)
barMenu.add_cascade(label="Delete_DB",menu=deleteMenu)
barMenu.add_cascade(label="CRUD", menu=crudMenu)
barMenu.add_cascade(label="Help", menu=helpMenu)

#--------Creating Objects----------------
myFrame = Frame(root)
myFrame.pack()

myid = StringVar()
myplanet = StringVar()
mydiameter = StringVar()
mydistance = StringVar()
myyear = StringVar()

textfield_id = Entry(myFrame, textvariable=myid)
textfield_id.grid(row=0, column=1, padx=10, pady=10)

textfield_planet = Entry(myFrame, textvariable=myplanet)
textfield_planet.grid(row=1, column=1, padx=10, pady=10)

textfield_diameter = Entry(myFrame, textvariable=mydiameter)
textfield_diameter.grid(row=2, column=1, padx=10, pady=10)

textfield_distance = Entry(myFrame, textvariable=mydistance)
textfield_distance.grid(row=3, column=1, padx=10, pady=10)

textfield_year = Entry(myFrame, textvariable=myyear)
textfield_year.grid(row=4, column=1, padx=10, pady=10)

#----------------------Labels---------------
idlabel = Label(myFrame, text="ID:")
idlabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)

planetlabel = Label(myFrame, text="Planet:")
planetlabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)

diameterlabel = Label(myFrame, text="Diameter (km):")
diameterlabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)

distancelabel = Label(myFrame, text="Distance (km):")
distancelabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)

yearlabel = Label(myFrame, text="Year Length:")
yearlabel.grid(row=4, column=0, sticky="e", padx=10, pady=10)

#------------------ Frame-2------------------
myFrame2 = Frame(root)
myFrame2.pack()

buttonCreate = Button(myFrame2, text="Create", command=create) 
buttonCreate.grid(row=1, column=0, sticky="e", padx=10, pady=10)

buttonRead = Button(myFrame2, text="Read", command=read)
buttonRead.grid(row=1, column=1, sticky="e", padx=10, pady=10)

buttonUpdate = Button(myFrame2, text="Update", command=update)
buttonUpdate.grid(row=1, column=2, sticky="e", padx=10, pady=10)

buttonDelete = Button(myFrame2, text="Delete", command=delete)
buttonDelete.grid(row=1, column=3, sticky="e", padx=10, pady=10)

root.mainloop()
