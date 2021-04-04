######################################################################################################
import webbrowser
import tkinter.messagebox as msb
import tkinter.ttk as ttk
from tkinter import *
######################################################################################################

def function(text):
    print(text)


class Application:
    def __init__(self):
        self.window = tk.Tk()
        self.cb_value = tk.StringVar()
        # text['state'] = 'disabled'
        tx = tk.Label(self.window, text="Ponidziałek",
                      justify='left').place(x=37, y=5)
        tx2 = tk.Label(self.window, text="1.",
                       justify='left', fg='red').place(x=18, y=40)
        tx3 = tk.Label(self.window, text="2.",
                       justify='left', fg='red').place(x=18, y=80)
        tx4 = tk.Label(self.window, text="3.",
                       justify='left', fg='red').place(x=18, y=120)
        tx5 = tk.Label(self.window, text="4.",
                       justify='left', fg='red').place(x=18, y=160)
        tx6 = tk.Label(self.window, text="5.",
                       justify='left', fg='red').place(x=18, y=200)
        tx7 = tk.Label(self.window, text="6.",
                       justify='left', fg='red').place(x=18, y=240)
        # tx8 = tk.Label(self.window, text="7.",
        #                justify='left', fg='red').place(x=18, y=280)
        tx1 = tk.Label(self.window, text="Wtorek",
                       justify='left').place(x=200, y=5)
        tx2 = tk.Label(self.window, text="1.",
                       justify='left', fg='red').place(x=181, y=40)
        tx3 = tk.Label(self.window, text="2.",
                       justify='left', fg='red').place(x=181, y=80)
        tx4 = tk.Label(self.window, text="3.",
                       justify='left', fg='red').place(x=181, y=120)
        tx5 = tk.Label(self.window, text="4.",
                       justify='left', fg='red').place(x=181, y=160)
        tx6 = tk.Label(self.window, text="5.",
                       justify='left', fg='red').place(x=181, y=200)
        tx1 = tk.Label(self.window, text="Środa",
                       justify='left').place(x=363, y=5)
        tx2 = tk.Label(self.window, text="1.",
                       justify='left', fg='red').place(x=344, y=40)
        tx3 = tk.Label(self.window, text="2.",
                       justify='left', fg='red').place(x=344, y=80)
        tx4 = tk.Label(self.window, text="3.",
                       justify='left', fg='red').place(x=344, y=120)
        tx5 = tk.Label(self.window, text="4.",
                       justify='left', fg='red').place(x=344, y=160)
        tx6 = tk.Label(self.window, text="5.",
                       justify='left', fg='red').place(x=344, y=200)
        tx1 = tk.Label(self.window, text="Czwartek",
                       justify='left').place(x=526, y=5)
        tx2 = tk.Label(self.window, text="1.",
                       justify='left', fg='red').place(x=507, y=40)
        tx3 = tk.Label(self.window, text="2.",
                       justify='left', fg='red').place(x=507, y=80)
        tx4 = tk.Label(self.window, text="3.",
                       justify='left', fg='red').place(x=507, y=120)
        tx5 = tk.Label(self.window, text="4.",
                       justify='left', fg='red').place(x=507, y=160)
        tx6 = tk.Label(self.window, text="5.",
                       justify='left', fg='red').place(x=507, y=200)
        tx1 = tk.Label(self.window, text="Piątek",
                       justify='left').place(x=689, y=5)
        tx2 = tk.Label(self.window, text="1.",
                       justify='left', fg='red').place(x=670, y=40)
        tx3 = tk.Label(self.window, text="2.",
                       justify='left', fg='red').place(x=670, y=80)
        tx4 = tk.Label(self.window, text="3.",
                       justify='left', fg='red').place(x=670, y=120)
        tx5 = tk.Label(self.window, text="4.",
                       justify='left', fg='red').place(x=670, y=160)
        tx6 = tk.Label(self.window, text="5.",
                       justify='left', fg='red').place(x=670, y=200)
        tx7 = tk.Label(self.window, text="6.",
                       justify='left', fg='red').place(x=670, y=240)
        # tx8 = tk.Label(self.window, text="7.",
        #                justify='left', fg='red').place(x=181, y=280)
        # tx1 = Text(self.window, width=5, height=1).place(x=35, y=2)

        nic = tk.Button(self.window, text='',
                        width='15')
        Fizyka = tk.Button(self.window, text='Fizyka', width='15', command=lambda: webbrowser.open(
            ""))
        Fizyka1 = tk.Button(self.window, text='Fizyka', width='15', command=lambda: webbrowser.open(
            ""))
        Matematyka = tk.Button(self.window, text='Matematyka', width='15', height='1', command=lambda: webbrowser.open(
            ""))
        Matematyka1 = tk.Button(self.window, text='k.Matematyka', width='15', height='1', command=lambda: webbrowser.open(
            ""))
        Matematyka2 = tk.Button(self.window, text='Matematyka', width='15', height='1', command=lambda: webbrowser.open(
            ""))
        Matematyka3 = tk.Button(self.window, text='Matematyka', width='15', height='1', command=lambda: webbrowser.open(
            ""))
        Matematyka4 = tk.Button(self.window, text='Matematyka', width='15', height='1', command=lambda: webbrowser.open(
            ""))
        Historia = tk.Button(self.window, text='Historia', width='15', height='1', command=lambda: webbrowser.open(
            ""))
        Historia1 = tk.Button(self.window, text='Historia', width='15', height='1', command=lambda: webbrowser.open(
            ""))
        Polski = tk.Button(self.window, text='Polski', width='15', height='1', command=lambda: webbrowser.open(
            ""))
        Polski1 = tk.Button(self.window, text='Polski', width='15', height='1', command=lambda: webbrowser.open(
            ""))
        Polski2 = tk.Button(self.window, text='Polski', width='15', height='1', command=lambda: webbrowser.open(
            ""))
        Polski3 = tk.Button(self.window, text='Polski', width='15', height='1', command=lambda: webbrowser.open(
            ""))
        Polski4 = tk.Button(self.window, text='Polski', width='15', height='1', command=lambda: webbrowser.open(
            ""))
        kPolski = tk.Button(self.window, text='k.Polski', width='15', height='1', command=lambda: webbrowser.open(
            ""))
        Niemiecki = tk.Button(self.window, text='Niemiecki', width='15', height='1', command=lambda: webbrowser.open(
            ""))
        Niemiecki1 = tk.Button(self.window, text='Niemiecki', width='15', height='1', command=lambda: webbrowser.open(
            ""))
        Angielski = tk.Button(self.window, text='Angielski', width='15', height='1', command=lambda: webbrowser.open(
            ""))
        Angielski1 = tk.Button(self.window, text='Angielski', width='15', height='1', command=lambda: webbrowser.open(
            ""))
        Angielski2 = tk.Button(self.window, text='Angielski', width='15', height='1', command=lambda: webbrowser.open(
            ""))
        Geografia = tk.Button(self.window, text='Geografia', width='15', height='1', command=lambda: webbrowser.open(
            ""))
        Wos = tk.Button(self.window, text='Wos', width='15', height='1', command=lambda: webbrowser.open(
            ""))
        Wos1 = tk.Button(self.window, text='Wos', width='15', height='1', command=lambda: webbrowser.open(
            ""))
        Biologia = tk.Button(self.window, text='Biologia', width='15', height='1', command=lambda: webbrowser.open(
            ""))
        Biologia1 = tk.Button(self.window, text='Biologia', width='15', height='1', command=lambda: webbrowser.open(
            ""))
        Chemia = tk.Button(self.window, text='Chemia', width='15', height='1', command=lambda: webbrowser.open(
            ""))
###########<Button-place>#############################################################################
        nic.place(x=40, y=30)
        Fizyka.place(x=40, y=70)
        Matematyka.place(x=40, y=110)
        Historia.place(x=40, y=150)
        Polski.place(x=40, y=190)
        Matematyka1.place(x=40, y=230)

        Niemiecki.place(x=203, y=30)
        Angielski.place(x=203, y=70)
        Polski1.place(x=203, y=110)
        Geografia.place(x=203, y=150)
        kPolski.place(x=203, y=190)

        Historia1.place(x=366, y=30)
        Wos.place(x=366, y=70)
        Polski2.place(x=366, y=110)
        Biologia.place(x=366, y=150)
        Matematyka2.place(x=366, y=190)

        Angielski1.place(x=529, y=30)
        Fizyka1.place(x=529, y=70)
        Matematyka3.place(x=529, y=110)
        Niemiecki1.place(x=529, y=150)
        Polski3.place(x=529, y=190)

        Polski4.place(x=692, y=30)
        Biologia1.place(x=692, y=70)
        Chemia.place(x=692, y=110)
        Angielski2.place(x=692, y=150)
        Matematyka4.place(x=692, y=190)
        Wos1.place(x=692, y=230)

###########<Button-place>#############################################################################
        self.window.geometry('840x280')
        self.window.mainloop()

        def on_select_changed(self, event):
            msb.showinfo("Info", self.cb_value.get())


apl = Application()
