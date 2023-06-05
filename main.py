from tkinter import *
import math

root = Tk()
root.geometry("800x600")
root.title("Calculate CGPA/SGPA")
semester = [1, 2, 3, 4, 5, 6, 7, 8]
subcheck=[]
subcheck.append(1)
subclick = IntVar()
subjects = [1, 2, 3, 4, 5, 6]
subselect = OptionMenu(root, subclick, *subjects)
subselect.grid(row=2, column=2)
sgpalist={}
clicked1 = IntVar()
clicked1.set(1)
credits = [1, 2, 3, 4, 5]

txttitle = Label(root, text="                                        CGPA CALCULATOR", fg="blue")
txttitle.grid(row=0, column=1, pady=7)

txtsem = Label(root, text="                                           Choose the semester:")
txtsem.grid(row=1, column=1)
txtsubs = Label(root, text="                                           Select no of subjects:")
txtsubs.grid(row=2, column=1)
semdrop = OptionMenu(root, clicked1, *semester)
semdrop.grid(row=1, column=2)
subs = subclick.get()
subclick.set(1)
startofprog = 0

def clear():
    for i in range(subcheck[1]+1,subcheck[0]+1):
        globals()["ent" + str(i)].grid_remove()
        globals()["crd" + str(i)].grid_remove()
        globals()["sub" + str(i)].grid_remove()
        globals()["crd" + str(i) + "drop"].grid_remove()
def subsfun():
    global startofprog
    if (startofprog == 0):
        startofprog = 1
        subcheck.append(subclick.get())
        for i in range(1, subclick.get() + 1):
            globals()["sub" + str(i)] = Label(root, text=("Subject{0}(out of 100)").format(i))
            globals()["sub" + str(i)].grid(row=2 + i, column=0)
            globals()["ent" + str(i)] = Entry(root, width=35, borderwidth=5)
            globals()["ent" + str(i)].grid(row=2 + i, column=1)
            globals()["crd" + str(i)] = Label(root, text="No of credits:")
            globals()["crd" + str(i)].grid(row=2 + i, column=2,padx=8)
            globals()["clicked" + str(i+1)] = IntVar()
            globals()["clicked" + str(i + 1)].set(1)
            globals()["crd" + str(i) + "drop"] = OptionMenu(root, globals()["clicked" + str(i+1)], *credits)
            globals()["crd" + str(i) + "drop"].grid(row=2 + i, column=3)
    else:
        subcheck.reverse()
        subcheck.pop(1)
        subcheck.append(subclick.get())
        clear()
        if (subcheck[1] < subcheck[0]):
            clear()
        else:
            for i in range(subcheck[0]+1, subcheck[1]+1):
                globals()["sub" + str(i)] = Label(root, text=("Subject{0}(out of 100)").format(i))
                globals()["sub" + str(i)].grid(row=2 + i, column=0)
                globals()["ent" + str(i)] = Entry(root, width=35, borderwidth=5)
                globals()["ent" + str(i)].grid(row=2 + i, column=1)
                globals()["crd" + str(i)] = Label(root, text="No of credits:")
                globals()["crd" + str(i)].grid(row=2 + i, column=2)
                globals()["clicked" + str(i+1)] = IntVar()
                globals()["clicked" + str(i+1)].set(1)
                globals()["crd" + str(i) + "drop"] = OptionMenu(root, globals()["clicked" + str(i+1)], *credits)
                globals()["crd" + str(i) + "drop"].grid(row=2 + i, column=3)


but = Button(root, text="Enter", command=subsfun)
but.grid(row=2, column=2, columnspan=3)





def sgpac(a):
    global marksvals
    sem = clicked1.get()
    gradeptlist = []
    totalcredits = 0
    for x in range(subclick.get()):
        gradeptlist.append((math.ceil(marksvals[sem][x] / 10.0)) * crdsvals[sem][x])
    totalcredits = sum(crdsvals[sem])
    numerator = float(sum(gradeptlist))
    sgpaval = numerator / totalcredits
    sgpaval = round(sgpaval, 3)
    sgpalist[sem]=sgpaval
    print(sgpalist)
    if(a==1):
        outsgpa.config(text=sgpaval)


def cgpac():
    cgpaval=0
    for x in semsentered:
        cgpaval=cgpaval+sgpalist[x]
    cgpaval/=len(semsentered)
    cgpaval=round(cgpaval,3)
    outcgpa.config(text=cgpaval)


error = Label(root, text="")
error.grid(row=6, column=1)


def save():
    flag=True
    for i in range (1,subclick.get()+1):
        if(float(globals()["ent"+str(i)].get())<0 or float(globals()["ent"+str(i)].get())>100):
            flag=False
    if(not flag):
        error.config(text='Enter Marks between 0 and 100!!!',fg='red')
    else:
        error.config(text='')
        sem = clicked1.get()
        semsentered.add(sem)
        marksvals[sem]=[float(globals()["ent" + str(i)].get()) for i in range(1, subclick.get() + 1)]
        crdsvals[sem] = [int(globals()["clicked" + str(i)].get()) for i in range(2, subclick.get() + 2)]
        sgpac(0)
        print("\nMarks:\n", marksvals)
        print("\nCredits:\n", crdsvals)
        print("Sems marks entered:", semsentered)


save = Button(root, text="Save", padx=40, pady=20, command=save, fg='blue')

sgpa = Button(root, text="Calculate SGPA", padx=40, pady=20, command=lambda: sgpac(1), fg='blue')
cgpa = Button(root, text="Calculate CGPA", padx=40, pady=20, command=cgpac, fg='blue')

save.grid(row=10, column=3, pady=3)
sgpa.grid(row=11, column=3, pady=3)
cgpa.grid(row=12, column=3)

outsgpa = Label(root, text=" ")
outcgpa = Label(root, text=" ")

outsgpa.grid(row=11, column=4)
outcgpa.grid(row=12, column=4)

semsentered = set()
sem1, sem2, sem3, sem4, sem5, sem6, sem7, sem8 = [], [], [], [], [], [], [], []
crds1, crds2, crds3, crds4, crds5, crds6, crds7, crds8 = [], [], [], [], [], [], [], []
marksvals = {1: sem1, 2: sem2, 3: sem3, 4: sem4, 5: sem5, 6: sem6, 7: sem7, 8: sem8}
crdsvals = {1: crds1, 2: crds2, 3: crds3, 4: crds4, 5: crds5, 6: crds6, 7: crds7, 8: crds8}

root.mainloop()