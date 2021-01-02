#Importing Modules
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.tix import  *
import json


mainwindow = Tk()
mainwindow.title('Student Database')
mainwindow.config(bg='#4d4d4d')


#This will always open the Main Window in fullscreen
mainwindow.state('zoomed')


#This function will create a message box and if 'Yes' is clicked data will save
def confirm():
	msg = tkinter.messagebox.askquestion("SAVE", "Are sure you want to Save?")
	if msg == 'yes':
		save()


#This function will Save the data in our json file of Student data
def save():

	studentname = str(studentnameentry.get())
	rollno = int(rollnoentry.get())
	if gendervariable.get() == 1:
		gender = 'Male'
	else:
		gender = 'Female'
	address = addressentry.get()
	phoneno = phoneentry.get()
	batch = batchentry.get()
	if checkboxvalue.get() == 0:
		hostel = 'No'
	else:
		hostel= 'Yes'

	data = {"Student Name": studentname, "Rollno": rollno, "Gender": gender, "Address Of Correspondence": address, "Phone Number": phoneno, "Batch Name": batch, "Hostel Facility": hostel}

	jsonfile = open('Students.json')
	jsonobject = json.load(jsonfile)
	temp = jsonobject['STUDENTS']
	temp.append(data)
	jsonfile.close()
	with open('Students.json', 'w') as databse:
		json.dump(jsonobject, databse, indent=4)


#just like before a message will show if click 'Yes'
def confirm1():
	msg = tkinter.messagebox.askquestion("SAVE", "Are sure you want to Save?")
	if msg == 'yes':
		savecourse()

#This function is save Course data in JSON file
def savecourse():

	courseid = int(courseentry.get())
	coursename = str(couursenameentry.get())

	coursedata = {"Couse ID": courseid, "Course Name": coursename}
	jsonfile1 = open('Course.json')
	jsonobject1 = json.load(jsonfile1)
	temp1 = jsonobject1['COURSES']
	temp1.append(coursedata)
	jsonfile1.close()
	with open('Course.json', 'w') as databse1:
		json.dump(jsonobject1, databse1, indent=4)


#Similar Function like previously for messagbox on clicking button
def confirm2():
	msg = tkinter.messagebox.askquestion("SAVE", "Are sure you want to Save?")
	if msg == 'yes':
		allocate()

#Function to put Allocated data in the JSON file
def allocate():

	rollnov = int(rollnoentry1.get())
	cousename = str(couursenameentry.get())

	allocatedata = {"Rollno": rollnov, "Course ID": cousename}
	jsonfile2 = open('Allocation.json')
	jsonobject2 = json.load(jsonfile2)
	temp2 = jsonobject2['STU_COURSE']
	temp2.append(allocatedata)
	jsonfile2.close()
	with open('Allocation.json', 'w') as databse2:
		json.dump(jsonobject2, databse2, indent=4)





#This function is to clear the entries on cllicking the button
def clear():
	studentnameentry.delete(0, END)
	rollnoentry.delete(0, END)
	phoneentry.delete(0, END)
	gendervariable.set(False)
	addressentry.delete(0, END)
	phoneentry.delete(0, END)
	batchentry.delete(0, END)
	checkboxvalue.set(None)
	courseentry.delete(0, END)
	rollnoentry1.delete(0, END)
	coursenameentry.delete(0, END)


#Creating Main Frame of our GUI (where everything will be displayed)
mainframe = Frame(width= 500, height= 350, bg= '#d9d9d9', bd= 0.3, relief= SOLID)
mainframe.pack(pady=150, padx= 250, fill='both', expand=True)


#Creating Tab Control here
tabcontrol = ttk.Notebook(mainframe)




#Tab1 is the frame for Regiratation of "new students"
tab1 = ttk.Frame(tabcontrol)
tabcontrol.add(tab1, text='New Student')


studentnamelabel = Label(tab1, text='Enter Student Name:', font=('Open Sans Semibold', 12))
studentnamelabel.grid(row=0, column=0, padx= 50, pady= 10, sticky='e')
studentnameentry = Entry(tab1, width=64)
studentnameentry.grid(row=0, column=1, padx=300, pady= 10)

rollnolabel = Label(tab1, text='Enter Rollno:', font=('Open Sans Semibold', 12))
rollnolabel.grid(row=1, column=0, padx= 50, pady= 10, sticky='e')
rollnoentry = Entry(tab1, width= 64)
rollnoentry.grid(row=1, column=1, padx=300, pady= 10)

gendervariable = IntVar()
genderlabel = Label(tab1, text='Select Gender:', font=('Open Sans Semibold', 12))
genderlabel.grid(row=2, column=0, padx= 50, pady= 10, sticky='e')
genderradio1 = Radiobutton(tab1, text='Male', variable= gendervariable, value= 1)
genderradio1.place(x=632, y=105)
genderradio2 = Radiobutton(tab1, text='Female', variable= gendervariable, value= 2)
genderradio2.place(x=900, y=105)

addresslabel = Label(tab1, text='Address For Correspondence:', font=('Open Sans Semibold', 12))
addresslabel.grid(row=3, column=0, padx= 50, pady= 10, sticky='e')
addressentry = Entry(tab1, width= 64)
addressentry.grid(row=3, column=1, padx=300, pady= 10)

phonelabel = Label(tab1, text='Phone Number:', font=('Open Sans Semibold', 12))
phonelabel.grid(row=4, column=0, padx= 50, pady= 10, sticky='e')
phoneentry = Entry(tab1, width= 64)
phoneentry.grid(row=4, column=1, padx=300, pady= 10)

batchlabel = Label(tab1,text="Enter Batch Name:", font=('Open Sans Semibold', 12))
batchlabel.grid(row=5, column=0, padx=50, pady=10, sticky='e')
batchentry = ttk.Combobox(tab1, width= 61, value=('Batch-1', 'Batch-2'))
batchentry.place(x= 635, y=255)

checkboxvalue = IntVar()
hostellabel = Label(tab1, text='Hotel Facility [Y/N]:', font=('Open Sans Semibold', 12))
hostellabel.grid(row=6, column=0, padx= 50, pady= 10, sticky='e')
hostelentry = Checkbutton(tab1, text= 'Check the button if need Hostel Facility', variable= checkboxvalue )
hostelentry.grid(row=6, column=1, padx= 300, sticky='w')

sumitbutton = Button(tab1, text='SAVE', width= 35, height= 1, bg= 'brown', font=('Open Sans Semibold', 10), command=confirm)
sumitbutton.place(x= 200, y= 390)

clearbutton = Button(tab1, text='CLEAR', width= 35, height= 1, bg= 'brown', font=('Open Sans Semibold', 10), command=clear)
clearbutton.place(x= 500, y= 390)

#Display a message when we move cursor over buttons
tip = Balloon(tab1)
tip.subwidget('label').forget()
tip.bind_widget(sumitbutton, balloonmsg='Click to Save')
tip.bind_widget(clearbutton, balloonmsg='Click to Clear')







#Tab no 2 for displaying Students data (json file)
tab2 = ttk.Frame(tabcontrol)
tabcontrol.add(tab2, text='Display Student Data')


#creating and placing treeview table display
table = ttk.Treeview(tab2)
table.place(x=40, y=25, width=950, height=300)


#table creation here
style = ttk.Style()
style.configure('mystyle.Treeview.Heading', font= ('Arial Bold', 10), background= '#e1e1e1')

table['column'] = ['Rollno', 'Student Name', 'Gender', 'Address', 'Phone no.', 'Batch', "Hostel"]
table['show'] = 'headings'

table.heading('Rollno', text= 'Rollno')
table.heading('Student Name', text= 'Student Name')
table.heading('Gender', text= 'Gender')
table.heading('Address', text= 'Address')
table.heading('Phone no.', text='Phone no.')
table.heading('Batch', text= 'Batch')
table.heading('Hostel', text= 'Hostel')

table.column('0', anchor= 'c', width=75)
table.column('1', anchor= 'c', width=150)
table.column('2', anchor= 'c', width=75)
table.column('3', anchor= 'w', width=250)
table.column('4', anchor= 'c', width=150)
table.column('5', anchor= 'c', width=100)
table.column('6', anchor= 'w', width=75)

#Getting data from json file and storing data in lists
studentfile = open('Students.json')
studentrecord = json.load(studentfile)

rollnolist = []
for items in studentrecord['STUDENTS']:
	rollnolist.append(items['Rollno'])

studentnamelist = []
for items in studentrecord['STUDENTS']:
	studentnamelist.append(items['Student Name'])

genderlist = []
for items in studentrecord['STUDENTS']:
	genderlist.append(items['Gender'])

addresslist = []
for items in studentrecord['STUDENTS']:
	addresslist.append(items['Address Of Correspondence'])

phonenolist = []
for items in studentrecord['STUDENTS']:
	phonenolist.append(items['Phone Number'])

batchlist = []
for items in studentrecord['STUDENTS']:
	batchlist.append(items['Batch Name'])

hostellist = []
for items in studentrecord['STUDENTS']:
	hostellist.append(items['Hostel Facility'])


for a, b, c, d, e, f, g in zip(rollnolist, studentnamelist, genderlist, addresslist, phonenolist, batchlist, hostellist):
	table.insert("", 'end', values=(a ,b, c, d, e, f, g))

a = table.get_children()
def hide():

	global a

	if not table.get_children():
		for  x, child in enumerate(a):
			table.reattach(item=child, parent=table.parent(a[0]), index=x)

for child in a:
	table.detach(child)


displaybutton = Button(tab2, text='Display Data', width=35, height=1, bg='brown', font=('Open Sans Semibold', 10), command=hide)
displaybutton.pack(side=BOTTOM , pady=55)

#Create a message when we move cursor over buttons just like before
tip = Balloon(tab2)
tip.subwidget('label').forget()
tip.bind_widget(displaybutton, balloonmsg='Click to Display Data')






#Tab no.3 for adding/creating new courses
tab3 = ttk.Frame(tabcontrol)
tabcontrol.add(tab3, text='Course Creation')


courselabel = Label(tab3, text='Course ID:', font=('Open Sans Semibold', 12))
courselabel.grid(row=0, column=0, padx=175, pady= 75, sticky='e')
courseentry = Entry(tab3, width= 69)
courseentry.grid(row=0, column=1, sticky='w')

coursenamelabel = Label(tab3, text='Course Name:', font=('Open Sans Semibold', 12))
coursenamelabel.grid(row=1, column=0, padx=175, sticky='e')
couursenameentry = Entry(tab3, width= 69)
couursenameentry.grid(row=1, column=1, sticky='w')

sumitbutton1 = Button(tab3, text='SAVE', width= 35, height= 1, bg= 'brown', font=('Open Sans Semibold', 10), command=confirm1)
sumitbutton1.place(x= 200, y= 390)

clearbutton1 = Button(tab3, text='CLEAR', width= 35, height= 1, bg= 'brown', font=('Open Sans Semibold', 10), command=clear)
clearbutton1.place(x= 500, y= 390)

#Create a hovering message when we move cursor over buttons
tip = Balloon(tab3)
tip.subwidget('label').forget()
tip.bind_widget(sumitbutton1, balloonmsg='Click to Save')
tip.bind_widget(clearbutton1, balloonmsg='Click to Clear')





#tab no. 4 displaying courses we created
tab4 = ttk.Frame(tabcontrol)
tabcontrol.add(tab4, text='Display Courses')


#creating table view
table1 = ttk.Treeview(tab4)
table1.place(x=160, y=35, width=700, height=300)



table1['column'] = ['Course ID', 'Course Name']
table1['show'] = 'headings'

table1.heading('Course ID', text='Course ID')
table1.heading('Course Name', text='Course Name')

table1.column('0', anchor='c', width= 250)
table1.column('1', anchor='c', width= 250 )

coursefile = open('Course.json')
courserecord = json.load(coursefile)

courseidlist = []
for items in courserecord['COURSES']:
	courseidlist.append(items['Course ID'])

coursenamerecord = []
for items in courserecord['COURSES']:
	coursenamerecord.append(items['Course Name'])

for a, b in zip(courseidlist, coursenamerecord):
	table1.insert("", 'end', values=(a, b))


displaybutton1 = Button(tab4, text='Display Courses', width=35, height=1, bg='brown', font=('Open Sans Semibold', 10))
displaybutton1.pack(side=BOTTOM , pady=55)

#message on hovering over button
tip = Balloon(tab4)
tip.subwidget('label').forget()
tip.bind_widget(displaybutton1, balloonmsg='Click to Display Courses')






#Tab no. 5 for Course Allocations
tab5 = ttk.Frame(tabcontrol)
tabcontrol.add(tab5, text='Course Allocations')

rollnolabel1 = Label(tab5, text='Student Rollno:', font=('Open Sans Semibold', 12))
rollnolabel1.grid(row=0, column=0, padx=175, pady= 75, sticky='e')
rollnoentry1 = Entry(tab5, width= 69)
rollnoentry1.grid(row=0, column=1, sticky='w')

coursenamelabel = Label(tab5, text='Course Name:', font=('Open Sans Semibold', 12))
coursenamelabel.grid(row=1, column=0, padx=175, sticky='e')
coursenameentry = ttk.Combobox(tab5, width= 66, value=('Course 1', 'Course 2'))
coursenameentry.place(x= 475, y= 183)


sumitbutton2 = Button(tab5, text='Allocate', width= 35, height= 1, bg= 'brown', font=('Open Sans Semibold', 10), command=confirm2)
sumitbutton2.place(x= 200, y= 390)

clearbutton2 = Button(tab5, text='CLEAR', width= 35, height= 1, bg= 'brown', font=('Open Sans Semibold', 10), command=clear)
clearbutton2.place(x= 500, y= 390)


#message on hovering buttons
tip = Balloon(tab5)
tip.subwidget('label').forget()
tip.bind_widget(clearbutton2, balloonmsg='Click to Clear')
tip.bind_widget(sumitbutton2, balloonmsg='Click to Allocate')












tabcontrol.pack(expand=1, fill='both')
mainwindow.mainloop()