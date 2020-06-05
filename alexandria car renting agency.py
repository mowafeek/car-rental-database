import tkinter as tk 
from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import *
from tkinter import messagebox
import mysql.connector
import csv


db_connection = mysql.connector.connect(host="localhost", user="root", password="root",  database="wafek")
db_cursor = db_connection.cursor()
def view_all_users():
    db_cursor.execute('SELECT * FROM car_agency')
    data = db_cursor.fetchall()
    for row in data:
        tree.insert("",tk.END,values=row)

def get_single_user(firstname):
    db_cursor.execute('SELECT * FROM car_agency WHERE firstname="{}"'.format(firstname))
    data = db_cursor.fetchall()
    return data 
 
# Other Functions

# functions
def clear_text():
    entry_fname.delete('0',END)
    entry_lname.delete('0',END)
    entry_email.delete('0',END)
    entry_age.delete('0',END)
    cal.delete('0',END)
    entry_address.delete('0',END)
    entry_phone.delete('0',END)

def add_details():
    firstname = str(entry_fname.get())
    lastname = str(entry_lname.get())
    email = str(entry_email.get())
    age = str(entry_age.get())
    carmodel = str(cal.get())
    phone_number = str(entry_phone.get())
    address = str(entry_address.get())
    if entry_fname.get()=='':
        messagebox.showerror("error",'first name is required !')
    if entry_lname.get()=='':
        messagebox.showerror("error",'last name is required !')
    if entry_email.get()=='':
        messagebox.showerror("error",'email is required !')
    if entry_age.get()=='0':
        messagebox.showerror("error",'age is required !')
    if cal.get()=='':
        messagebox.showerror("error",'car model is required !')
    if entry_phone.get()=='':
        messagebox.showerror("error",'phone number is required !')
    if entry_address.get()=='':
        messagebox.showerror("error",'address is required !')
    else: 
        student_sql_query = ("INSERT INTO car_agency VALUES('" +firstname + "','" + lastname + "', '" + email + "','" + age + "','" + carmodel + "', '" + address + "', '" + phone_number + "')")
        # Execute cursor and pass query as well as student data
        show=f" {firstname} ,  {lastname}  ,  {email} ,{age} ,{carmodel} ,  {address} , {phone_number}  "
        db_cursor.execute(student_sql_query)
        db_connection.commit()
        tab1_display.insert(tk.END,show)
        messagebox.showinfo('ACRA',f'congarulations Mr/Mrs {firstname}! , your car request has been submitted')
        
    
        

def check():
    if entry_fname.get()=='':
        messagebox.showerror("error",'first name is required !')
    if entry_lname.get()=='':
        messagebox.showerror("error",'last name is required !')
    if entry_email.get()=='':
        messagebox.showerror("error",'email is required !')
    if entry_age.get()=='0':
        messagebox.showerror("error",'age is required !')
    if cal.get()=='':
        messagebox.showerror("error",'car model is required !')
    if entry_phone.get()=='':
        messagebox.showerror("error",'phone number is required !')
    if entry_address.get()=='':
        messagebox.showerror("error",'address is required !')
    else:
        messagebox.showinfo('ACRA','all is good!')

def clear_display_result():
    tab1_display.delete('1.0',END)


def search_user_by_name():
    firstname = str(entry_search.get())
    result = get_single_user(firstname)
    # c.execute('SELECT * FROM ahmed WHERE firstname="{}"'.format(firstname))
    # data = c.fetchall()
    # print(result)
    tab2_display.insert(tk.END,result)
 

def clear_display_view():
    tab2_display.delete('1.0',END)


def clear_entered_search():
    entry_search.delete('0',END)

def export_as_csv():
    filename = str(entry_filename.get())
    myfilename = filename + '.csv'
    with open(myfilename, 'w') as f:
        writer = csv.writer(f)
        db_cursor .execute('SELECT * FROM car_agency')
        data = db_cursor.fetchall()
        writer.writerow (['firstname','lastname','email','age','car model','address','phonenumber'])
        writer.writerows(data)
        messagebox.showinfo(title = "ACRA", message = '"Exported As {}"'.format(myfilename))





# Structure and Layout
window = Tk()
window.title("Alex Renting Agency")
window.geometry("750x450")


style = ttk.Style(window)
style.configure("leftab.TNotebook",tabposition='wn')

# Tab Layout
tab_control = ttk.Notebook(window,style='lefttab.TNotebook')

tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab4 = ttk.Frame(tab_control)


# Add Tabs to Notebook
tab_control.add(tab1,text=f'{"Home":^20s}')
tab_control.add(tab2,text=f'{"View":^20s}')
tab_control.add(tab3,text=f'{"Search":^20s}')
tab_control.add(tab4,text=f'{"Export":^20s}')


tab_control.pack(expand=1,fill="both")

""" create_table() """

label1 = Label(tab1,text="fill this form to order your car",padx=5,pady=5)
label1.grid(column=1,row=0,)
label1.config(font='bold')

label2 = Label(tab2,text="View",padx=5,pady=5)
label2.grid(column=0,row=0)

label3 = Label(tab3,text="Search",padx=5,pady=5)
label3.grid(column=0,row=0)

label4 = Label(tab4,text="Export",padx=5,pady=5)
label4.grid(column=0,row=0)



# Main Home
l1 = Label(tab1,text="First Name",padx=5,pady=5)
l1.grid(column=0,row=1)
fname_raw_entry = StringVar()
entry_fname = Entry(tab1,textvariable=fname_raw_entry,width=50)
entry_fname.grid(row=1,column=1)

l2 = Label(tab1,text="Last Name",padx=5,pady=5)
l2.grid(column=0,row=2)
lname_raw_entry = StringVar()
entry_lname = Entry(tab1,textvariable=lname_raw_entry,width=50)
entry_lname.grid(row=2,column=1)

l3 = Label(tab1,text="Email",padx=5,pady=5)
l3.grid(column=0,row=3)
email_raw_entry = StringVar()
entry_email = Entry(tab1,textvariable=email_raw_entry,width=50)
entry_email.grid(row=3,column=1)

l4 = Label(tab1,text="Age",padx=5,pady=5)
l4.grid(column=0,row=4)
raw_entry = IntVar()
entry_age = Entry(tab1,textvariable=raw_entry,width=50)
entry_age.grid(row=4,column=1)

l5=Label(tab1,text='car model',padx=5,pady=5)
l5.grid(column=0,row=5)
dob_raw_entry=StringVar()
cal=Entry(tab1,textvariable=dob_raw_entry,width=50)
cal.grid(row=5,column=1,padx=10,pady=10)

l6 = Label(tab1,text="Address",padx=5,pady=5)
l6.grid(column=0,row=6)
#address_raw_entry = StringVar()
#entry_address = Entry(tab1,textvariable=address_raw_entry,width=50)
#entry_address.grid(row=6,column=1)
adres = ["sidi beshr", "sidi gaber", "smouha ","mansheyaa","miami","sporting","ibrahemiya","mandara","stanley","other"]
entry_address = ttk.Combobox(tab1, values=adres, width=20)
entry_address.place(x=155, y=195)
entry_address.current(0)


l7 = Label(tab1,text="Phone Number",padx=5,pady=5)
l7.grid(column=0,row=7)
phone_raw_entry = StringVar()
entry_phone = Entry(tab1,textvariable=phone_raw_entry,width=50)
entry_phone.grid(row=7,column=1)

button1 = Button(tab1,text="Add",width=12,bg="#003A63",fg="#fff",command=add_details)
button1.grid(row=8,column=0,padx=5,pady=5)

button2 = Button(tab1,text="Clear",width=12,bg="#003A63",fg="#fff",command=clear_text)
button2.grid(row=8,column=2,padx=5,pady=5)
button3 = Button(tab1,text="quit",width=12,bg="#839CCD",fg="#fff",command=quit)
button3.grid(row=12,column=1,padx=10,pady=10)

# Display Screen 

tab1_display = ScrolledText(tab1,height=5)
tab1_display.grid(row=10,column=1,padx=5,pady=5,columnspan=3)

button3 = Button(tab1,text="Clear Result",width=12,bg="#003A63",fg="#fff",command=clear_display_result)
button3.grid(row=8,column=1,padx=5,pady=5)

button4 = Button(tab1,text="check form",width=12,bg="#003A63",fg="#fff",command=check)
button4.grid(row=12,column=2,padx=5,pady=5)

# View
button_view2 = Button(tab2,text="View All",width=12,bg='#2450A2',fg="#fff",command=view_all_users)
button_view2.grid(column=0,row=1,padx=0,pady=10)
tree= ttk.Treeview(tab2, column=("column1", "column2","column3", "column4", "column5", "column6", "column7"), show='headings')
tree.heading("#1", text="First Name")
tree.heading("#2", text="Last Name")
tree.heading("#4", text="Age")
tree.heading("#5", text="car model")
tree.heading("#6", text="address")
tree.heading("#3", text="email")
tree.heading("#7",text="Phone Number")
tree.grid(row=10,column=0, columnspan=3,padx=5,pady=5)


# Search
label_search1 = Label(tab3,text="Search Name",padx=5,pady=5)
label_search1.grid(column=0,row=1)
search_raw_entry = StringVar()
entry_search = Entry(tab3,textvariable=search_raw_entry,width=30)
entry_search.grid(row=1,column=1)


button_view3 = Button(tab3,text="Clear Search",width=12,bg='#003A63',fg='#fff',command=clear_entered_search)
button_view3.grid(row=2,column=1,padx=10,pady=10)

button_view4 = Button(tab3,text="Clear Result",width=12,bg='#003A63',fg='#fff',command=clear_display_view)
button_view4.grid(row=2,column=2,padx=10,pady=10)

button_view5 = Button(tab3,text="Search",width=12,bg='#003A63',fg='#fff',command=search_user_by_name)
button_view5.grid(row=1,column=2,padx=10,pady=10)

tab2_display = ScrolledText(tab3,height=5)
# tab2_display = Listbox(tab2,height=5,width=60)
tab2_display.grid(row=10,column=0, columnspan=3,padx=5,pady=5)


# Export
# Export Database
label_export1 = Label(tab4,text="File Name",padx=5,pady=5)
label_export1.grid(column=0,row=2)
filename_raw_entry = StringVar()
entry_filename = Entry(tab4,textvariable=filename_raw_entry,width=30)
entry_filename.grid(row=2,column=1)

button_export3 = Button(tab4,text="export ",width=12,bg='#003A63',fg='#fff',command=export_as_csv)
button_export3.grid(row=3,column=1,padx=10,pady=10)








window.mainloop()


