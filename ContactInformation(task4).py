Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def AddContact():
...     if Name.get()!="" and Number.get()!="":
...         contactlist.append([Name.get() ,Number.get()])
...         print(contactlist)
...         Select_set()
...         EntryReset()
...         messagebox.showinfo("Confirmation", "Successfully Add New Contact")
...  
...     else:
...         messagebox.showerror("Error","Please fill the information")
...  
... def UpdateDetail():
...     if Name.get() and Number.get():
...         contactlist[Selected()] = [Name.get(), Number.get()]
...    
...         messagebox.showinfo("Confirmation", "Successfully Update Contact")
...         EntryReset()
...         Select_set()
...  
...     elif not(Name.get()) and not(Number.get()) and not(len(select.curselection())==0):
...         messagebox.showerror("Error", "Please fill the information")
...  
...     else:
...         if len(select.curselection())==0:
...             messagebox.showerror("Error", "Please Select the Name and \n press Load button")
...         else:
...             message1 = """To Load the all information of \n
...                           selected row press Load button\n.
...                           """
