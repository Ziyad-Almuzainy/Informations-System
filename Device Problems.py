# Used Libraries of Programming

import tempfile
import os
import sys
from tkinter import *
from tkinter import ttk 
from tkinter import filedialog
import tkinter.messagebox
from tkmacosx import Button
import pymysql
import random
import time
from time import strftime
import subprocess

# Creating Class
 
class malfunctionDevices():

    def __init__(self, root):
        self.root = root
        self.root.title('Reporting Management System')
        self.root.resizable(False, False)
        self.root.geometry('1438x760+0+0')
        self.root.configure(bg='#585858')


# Variabels 

        sn = StringVar()
        Devicename = StringVar()
        ClinicNumber = StringVar()
        Date1 = StringVar()
        TrobStatus = StringVar()
        NameWritter = StringVar()
        TrobReasons = StringVar()
        Date2 = StringVar()
        ActionTaken = StringVar()
        BranchHosp = StringVar() 
        Searching = StringVar()
        Search_by = StringVar()
        time_Var = StringVar()




# To Make Auto In Date Labels 

        Date1.set(time.strftime('%d/%m/%Y'))
        Date2.set(time.strftime('%d/%m/%Y'))
        time_Var = strftime('%H:%M:%S %p \n %A \n %x')


# Functions

        def ExitProgram():
            ToExit= tkinter.messagebox.askyesno('Reporting Management System', 'confirm if you want to close')
            if ToExit > 0:
                root.destroy()
                return





        
        def AddTransicript():
        
            self.textReport.insert(END,f'\t\t\t{time_Var}\n')
            self.textReport.insert(END,'=#=#=#=#=#=#=#=#=#=#=Report Day=#=#=#=#=#=#=#=#=#=\n\n')
            self.textReport.insert(END,'\nSerial Numper:\t\t\t\t\t' + sn.get() + '\n')
            self.textReport.insert(END,'**************************************************' + '\n')
            self.textReport.insert(END,'Device Name:\t\t\t\t\t'+ Devicename.get() + '\n')
            self.textReport.insert(END,'**************************************************' + '\n')
            self.textReport.insert(END,'Clinic Number:\t\t\t\t\t' + ClinicNumber.get() +'\n')
            self.textReport.insert(END,'**************************************************' + '\n')
            self.textReport.insert(END,'Status:\t\t\t\t\t\t' + TrobStatus.get() + '\n')
            self.textReport.insert(END,'**************************************************' + '\n')
            self.textReport.insert(END,'Reasons:\t\t\t\t\t\t'+ TrobReasons.get() + '\n')
            self.textReport.insert(END,'**************************************************' + '\n')
            self.textReport.insert(END,'Branch:\t\t\t\t\t\t' + BranchHosp.get()+ '\n')
            self.textReport.insert(END,'**************************************************' + '\n')
            self.textReport.insert(END,'By:\t\t\t\t\t\t' + NameWritter.get() + '\n\n')
            self.textReport.insert(END,'=#=#=#=#=#=#=#=#=#==#=#=#=#=#=#=#=#=#==#=#=#=#=#=#=#=' +'\n')
            
        def Save():
            url= filedialog.asksaveasfile(mode='w', defaultextension='.doc')

            bill_data = self.textReport.get(1.0, END)


            url.write(bill_data)
            url.close()
            tkinter.messagebox.showinfo('Malfunction Reporting System', 'Report Save is successfully')




        def Reset():

            
            sn.set('')
            Devicename.set('')
            ClinicNumber.set('')
            Date1.set('')
            TrobStatus.set('')
            NameWritter.set('')
            TrobReasons.set('') 
            Date2.set('')
            ActionTaken.set('')
            BranchHosp.set('') 
            Searching.set('')
            Search_by.set('')
            self.textReport.delete(1.0, END)
            ShowReport()
            Date1.set(time.strftime('%d/%m/%Y'))
            Date2.set(time.strftime('%d/%m/%Y'))
            


        def AddReport():
            AddTransicript()
            if sn.get() =='' or Devicename.get() =='' or ClinicNumber.get() =='':
                tkinter.messagebox.showerror('Malfunction Reporting System', 'Enter All Data Details')
        
            else:

                con = pymysql.connect(host = 'localhost', user = 'root', password = '', database ='ziyad')
                cur = con.cursor()
                cur.execute("insert into ABD values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                            sn.get(),
                            Devicename.get(),
                            ClinicNumber.get(),
                            Date1.get(),
                            TrobStatus.get(),
                            NameWritter.get(),
                            TrobReasons.get(),
                            Date2.get(),
                            ActionTaken.get(),
                            BranchHosp.get()                                                            
                            ))
                con.commit()
                ShowReport()
                con.close()
                tkinter.messagebox.showinfo('Malfunction Reporting System', 'Data entered successfully')




        def ShowReport():
            con = pymysql.connect(host = 'localhost', user = 'root', password = '', database ='ziyad')
            cur = con.cursor()
            cur.execute("select * from ABD")
            info = cur.fetchall()
            if len(info) != 0 :
                self.ReportingData.delete(*self.ReportingData.get_children())
                for row in info:
                    self.ReportingData.insert('',END, values=row)
                con.commit()
            con.close()



        def GetReport(ev):
            AddTransicript()
            getInfo = self.ReportingData.focus()
            contents = self.ReportingData.item(getInfo)
            info = contents['values']

            sn.set(info[0])
            Devicename.set(info[1])
            ClinicNumber.set(info[2])
            Date1.set(info[3])
            TrobStatus.set(info[4])
            NameWritter.set(info[5])
            TrobReasons.set(info[6])
            Date2.set(info[7])
            ActionTaken.set(info[8])
            BranchHosp.set(info[9])



        def Delete():
                con = pymysql.connect(host = 'localhost', user = 'root', password = '', database ='ziyad')
                cur = con.cursor()
                cur.execute("delete from ABD where SN=%s", sn.get())

                con.commit()
                ShowReport()
                con.close()
                tkinter.messagebox.showinfo('Malfunction Reporting System', 'Deleteed Data Successfully')
                Reset()



        def Update():
                con = pymysql.connect(host = 'localhost', user = 'root', password = '', database ='ziyad')
                cur = con.cursor()
                cur.execute("update ABD set name=%s ,location=%s, date1=%s, status=%s,nameWriter=%s,reasons=%s,"
                            " date2=%s, action=%s, branch=%s where SN=%s", (  
                                Devicename.get(),
                                ClinicNumber.get(),
                                Date1.get(),
                                TrobStatus.get(),
                                NameWritter.get(),
                                TrobReasons.get(),
                                Date2.get(),
                                ActionTaken.get(),
                                BranchHosp.get(),
                                sn.get()                                                            
                                ))

                con.commit()
                ShowReport()
                con.close()
                tkinter.messagebox.showinfo('Malfunction Reporting System', 'Data Update Successfully')




        def Search():
            con = pymysql.connect(host = 'localhost',user = 'root',password = '',database = 'ziyad')
            cur = con.cursor()
            cur.execute("select * from ABD where "+
            str(Search_by.get())+" LIKE '%"+ str(Searching.get())+"%'")
        
            infos = cur.fetchall()
            if len(infos) != 0 :
                self.ReportingData.delete(*self.ReportingData.get_children())
                for info in infos :
                    self.ReportingData.insert("",END ,values=info)
                con.commit()
            
            con.close()
            
#[Frames]

# Frame One in Window
        General_Frame = Frame(self.root, bd=2, padx=2, pady=2, width=1438, height=100, bg='#D8D8D8')
        General_Frame.grid()

    # Title Frame One in Window
        Title_Frames = Frame(General_Frame, bd=10, width=1427, height=100,padx=0, relief=RIDGE, bg='#d4e6f1')
        Title_Frames.pack(side=TOP)

        Title_Frames1 = Frame(Title_Frames, bd=0, width=50, height=50,padx=0, relief=RIDGE, bg='#d4e6f1')
        Title_Frames1.grid(row=0, column=0, padx=0)

        Title_Frames2 = Frame(Title_Frames, bd=0, width=50, height=50,padx=0, relief=RIDGE, bg='#d4e6f1')
        Title_Frames2.grid(row=0, column=1,padx=0)


    # Labels and Entry [===LEFT====]
        DataFrame = Frame(General_Frame, bd=10, width=1425, height=400, padx=0, relief=RIDGE, bg='#d4e6f1')
        DataFrame.pack(side=BOTTOM)

        LeftFrame = LabelFrame(DataFrame, bd=7, width=900, height=370, padx=5, relief=RIDGE, bg='#d4e6f1',
        font=('arial', 18, 'bold'), text='Information Input')
        LeftFrame.pack(side=LEFT)

        LeftFrameupp = Frame(LeftFrame, bd=7, width=800, height=205, padx=5, relief=RIDGE, bg='#d4e6f1')
        LeftFrameupp.grid(row=0, column=0)

        LeftFrameDowne = Frame(LeftFrame, bd=12, width=100, height=65, padx=3,pady=7, relief=RIDGE, bg='#d4e6f1')
        LeftFrameDowne.grid(row=1, column=0)

        RightFrame = LabelFrame(DataFrame, bd=7, width=421, height=386, padx=3, pady=0,relief=RIDGE, bg='#d4e6f1',
        font=('arial', 18, 'bold'), text='Transcript')
        RightFrame.pack(side=RIGHT)

    # Big Frame
        ButtonFrame = Frame(General_Frame, bd=10, width=1417, height=60, padx=5,pady=7, relief=RIDGE, bg='#d4e6f1')
        ButtonFrame.pack(side=BOTTOM)

    # Tabel Frame 
        FrameDetail = Frame(General_Frame, bd=10, width=1417, height=220, padx=5, relief=RIDGE, bg='#d4e6f1')
        FrameDetail.pack(side=BOTTOM)

    # Label Titel

        self.lblTitel1 = Label(Title_Frames1,width=46, font=('THE SOLSTICE', 20, 'bold'), text='\t\tREPORTING  MANAGEMENT  SYSTEM',
         bg='#d4e6f1', fg='#424242',justify='center', pady=10, padx=43)
        self.lblTitel1.grid()

        self.lblTitellogo = Label(Title_Frames2,width=300,height=50, image=self.logo,
         pady=7, padx=0, bg='#d4e6f1')
        self.lblTitellogo.grid()



    # Serial Number Labels and Entry

        self.lblsn = Label(LeftFrameupp, font=('arial', 14, 'bold'), text='Serial Number',bd=7, bg='#d4e6f1')
        self.lblsn.grid(row=0, column=0)
        self.textsn = Entry(LeftFrameupp, font=('arial', 12, 'bold'),bd=5, width=40, justify='left', textvariable=sn)
        self.textsn.grid(row=0, column=1, pady=7)

    # Device Name Labels and Entry

        self.lblDevicename = Label(LeftFrameupp, font=('arial', 14, 'bold'), text='Device Name',bd=7, bg='#d4e6f1')
        self.lblDevicename.grid(row=1, column=0,padx=0 )
        self.textDevicename = Entry(LeftFrameupp, font=('arial', 12, 'bold'),bd=5, width=40,  justify='left', textvariable=Devicename)
        self.textDevicename.grid(row=1, column=1, pady=7)

    # Clinic Number Labels and Entry

        self.lblClinicNumber = Label(LeftFrameupp, font=('arial', 14, 'bold'), text='Clinic Number',bd=7, bg='#d4e6f1')
        self.lblClinicNumber.grid(row=2, column=0,padx=0)
        self.textClinicNumber = Entry(LeftFrameupp, font=('arial', 12, 'bold'),bd=5, width=40, justify='left', textvariable=ClinicNumber)
        self.textClinicNumber.grid(row=2, column=1, pady=7)


    # Trouble Date Labels and Entry

        self.lblDate1 = Label(LeftFrameupp, font=('arial', 14, 'bold'), text='Trouble Date',bd=7, bg='#d4e6f1')
        self.lblDate1.grid(row=3, column=0,padx=0)
        self.textDate1 = Entry(LeftFrameupp, font=('arial', 12, 'bold'), bd=5, width=40, justify='left', textvariable=Date1)
        self.textDate1.grid(row=3, column=1, pady=7)

    # Trouble Status Labels and Entry

        self.lblTroubleStatus = Label(LeftFrameupp, font=('arial', 14, 'bold'), text='Trouble Status',bd=7, bg='#d4e6f1')
        self.lblTroubleStatus.grid(row=4, column=0,padx=0)
        self.cobTroubleStatus = ttk.Combobox(LeftFrameupp, width=40, font=('arial', 12, 'bold'), state='readonly', textvariable=TrobStatus)
        self.cobTroubleStatus['values'] = ('Pending','In Proccessing', 'Done')
        self.cobTroubleStatus.current(0)
        self.cobTroubleStatus.grid(row=4, column=1, pady=7)

    # Name Writter Entry

        self.lblNameWritter = Label(LeftFrameupp, font=('arial', 14, 'bold'), text='Name Writer',bd=7, bg='#d4e6f1')
        self.lblNameWritter.grid(row=0, column=2,padx=0)
        self.textNameWritter = Entry(LeftFrameupp, font=('arial', 12, 'bold'), bd=5, width=40, justify='left', textvariable=NameWritter)
        self.textNameWritter.grid(row=0, column=3, pady=7)


    # Trouble Reasons Labels and Entry

        self.lblTrobReasons = Label(LeftFrameupp, font=('arial', 14, 'bold'), text='Trouble Reasons',bd=7, bg='#d4e6f1')
        self.lblTrobReasons.grid(row=1, column=2,padx=0)
        self.textTrobReasons = Entry(LeftFrameupp, font=('arial', 12, 'bold'), bd=5, width=40, justify='left', textvariable=TrobReasons)
        self.textTrobReasons.grid(row=1, column=3, pady=7)

    # Fixed Date Labels and Entry

        self.lblDate2 = Label(LeftFrameupp, font=('arial', 14, 'bold'), text='Fixed Date',bd=7, bg='#d4e6f1')
        self.lblDate2.grid(row=2, column=2,padx=0)
        self.textDate2 = Entry(LeftFrameupp, font=('arial', 12, 'bold'), bd=5, width=40, justify='left', textvariable=Date2)
        self.textDate2.grid(row=2, column=3, pady=7)

    # Action Taken Labels and Entry 

        self.lblActionTaken = Label(LeftFrameupp, font=('arial', 14, 'bold'), text='Action Taken',bd=7, bg='#d4e6f1')
        self.lblActionTaken.grid(row=3, column=2,padx=0)
        self.textActionTaken = Entry(LeftFrameupp, font=('arial', 12, 'bold'), bd=5, width=40, justify='left', textvariable=ActionTaken)
        self.textActionTaken.grid(row=3, column=3, pady=7)

    # Branch Labels and Entry

        self.lblActionTaken = Label(LeftFrameupp, font=('arial', 14, 'bold'), text='Branch',bd=7, bg='#d4e6f1')
        self.lblActionTaken.grid(row=4, column=2,padx=0)
        self.cobBranchHosp = ttk.Combobox(LeftFrameupp, width=39, font=('arial', 12, 'bold'),state='readonly', textvariable=BranchHosp)
        self.cobBranchHosp['values'] = ('Al Rahmaniyya','Al Suwaidi', 'Al Rayyan')
        self.cobBranchHosp.current(0)
        self.cobBranchHosp.grid(row=4, column=3, pady=7)


    # Searching Entry and Button

        self.ButSearch = Button(LeftFrameDowne,pady=2,bd=4, font=('arial', 20, 'bold'), text='Search',
        width=160, height=28, bg='#424242',fg='white', command=Search)
        self.ButSearch.grid(row=0, column=0,padx=7, pady=2)
        self.search_cobo = ttk.Combobox(LeftFrameDowne, textvariable=Search_by, justify='left', font=('arial', 18))
        self.search_cobo['value'] = ('SN', 'Name')
        self.search_cobo.grid(row=0, column=1, pady=9, padx=5)
        self.textSearch = Entry(LeftFrameDowne, font=('arial', 16, 'bold'), bd=5, width=50, justify='left', textvariable=Searching)
        self.textSearch.grid(row=0, column=2, pady=9)


    # Transicript Board 

        self.textReport = Text(RightFrame, height=22, width=58, bd=7, font=('arial', 12, 'bold'), padx=2, pady=0)
        self.textReport.grid(row=0, column=0)
        
# Buttons

    # Add New Buttons
        self.ButtonAddNew = Button(ButtonFrame,pady=4,bd=4, font=('arial', 20, 'bold'), text='ADD NEW',
        width=160, height=26,bg='#424242',fg='white', command=AddReport)
        self.ButtonAddNew.grid(row=0, column=0,padx=35)
    
    # Update Button
        self.ButtonUpdate = Button(ButtonFrame,pady=4,bd=4, font=('Motion', 20, 'bold'), text='UPDATE',
        width=160, height=26,bg='#424242',fg='white', command=Update)
        self.ButtonUpdate.grid(row=0, column=1,padx=33)
    
    # Delete Button
        self.ButtonDelete = Button(ButtonFrame,pady=4,bd=4, font=('Motion', 20, 'bold'), text='DELETE',
        width=160, height=26, bg='#424242',fg='white', command=Delete)
        self.ButtonDelete.grid(row=0, column=2,padx=33)
    
    # Reset Button
        self.ButtonReset = Button(ButtonFrame,pady=4,bd=4, font=('arial', 20, 'bold'), text='RESET',
        width=160, height=26, bg='#424242',fg='white', command=Reset)
        self.ButtonReset.grid(row=0, column=3,padx=23)
    
    # Save Buttons
        self.ButtonSave = Button(ButtonFrame,pady=4,bd=4, font=('Motion', 20, 'bold'), text='SAVE',
        width=160, height=26, bg='#424242',fg='white', command=Save)
        self.ButtonSave.grid(row=0, column=4,padx=33)

    
    # Exit Button
        self.ButtonExit = Button(ButtonFrame,pady=4,bd=4, font=('arial', 20, 'bold'), text='EXIT',
        width=160, height=26, bg='#424242',fg='white', command=ExitProgram)
        self.ButtonExit.grid(row=0, column=6,padx=35)

    # Data Tabel 

        scroll_y = Scrollbar(FrameDetail, orient=VERTICAL)

        self.ReportingData=ttk.Treeview(FrameDetail,height=10 , columns=('SN', 'name','location',
        'date1','status','nameWriter','reasons','date2','action','branch'),yscrollcommand=scroll_y.set) 
        scroll_y.pack(side = RIGHT, fill=Y)

        self.ReportingData.heading('SN', text='Serial Number')
        self.ReportingData.heading('name', text='Device Name')
        self.ReportingData.heading('location', text='Clinic Number')
        self.ReportingData.heading('date1', text='Trouble Date')
        self.ReportingData.heading('status', text='Trouble Status')
        self.ReportingData.heading('nameWriter', text='Name Writer')
        self.ReportingData.heading('reasons', text='Trouble Reasons')
        self.ReportingData.heading('date2', text='Fixed Date')
        self.ReportingData.heading('action', text='Action Taken')
        self.ReportingData.heading('branch', text='Branch')

        self.ReportingData['show']='headings'

        self.ReportingData.column('SN', width=125)
        self.ReportingData.column('name', width=170)
        self.ReportingData.column('location', width=100)
        self.ReportingData.column('date1', width=108)
        self.ReportingData.column('status', width=115)
        self.ReportingData.column('nameWriter', width=115)
        self.ReportingData.column('reasons', width=230)
        self.ReportingData.column('date2', width=112)
        self.ReportingData.column('action', width=185)
        self.ReportingData.column('branch', width=122)

        self.ReportingData.pack(fill=BOTH, expand=1)
        self.ReportingData.bind('<ButtonRelease-1>', GetReport)
        ShowReport()


if __name__=='__main__':
    root = Tk()
    application = malfunctionDevices(root)
    root.mainloop()
