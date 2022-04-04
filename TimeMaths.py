import tkinter
import math
import tkinter.messagebox
import turtle
import webbrowser

class calculator:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.minsize(280, 450)
        self.root.maxsize(280, 470)
        self.root.title('TimeMaths')
        self.result = tkinter.StringVar()
        self.result.set(0)
        self.lists = []
        self.ispresssign = False
        self.menus()
        self.layout()
        self.root.mainloop()
    def menus(self):
        allmenu = tkinter.Menu(self.root)
        helpmenu = tkinter.Menu(allmenu, tearoff=0)
        helpmenu.add_command(label='查看帮助', command=self.aboutit)
        helpmenu.add_separator()
        helpmenu.add_command(label='关于TimeMaths', command=self.myfunc)
        allmenu.add_cascade(label='帮助', menu=helpmenu)

        self.root.config(menu=allmenu)


    def layout(self):
        result = tkinter.StringVar()
        result.set(0)
        show_label = tkinter.Label(self.root, bd=3, bg='white', font=('幼圆', 30), anchor='e', textvariable=self.result)
        show_label.place(x=5, y=20, width=270, height=70)
        button_mc = tkinter.Button(self.root, text='MC', command=self.wait)
        button_mc.place(x=5, y=95, width=50, height=50)
        button_mr = tkinter.Button(self.root, text='MR', command=self.wait)
        button_mr.place(x=60, y=95, width=50, height=50)
        button_ms = tkinter.Button(self.root, text='MS', command=self.wait)
        button_ms.place(x=115, y=95, width=50, height=50)
        button_mjia = tkinter.Button(self.root, text='M+', command=self.wait)
        button_mjia.place(x=170, y=95, width=50, height=50)
        button_mjian = tkinter.Button(self.root, text='M-', command=self.wait)
        button_mjian.place(x=225, y=95, width=50, height=50)
        button_zuo = tkinter.Button(self.root, text='←', command=self.dele_one)
        button_zuo.place(x=5, y=150, width=50, height=50)
        button_ce = tkinter.Button(self.root, text='CE', command=lambda: self.result.set(0))
        button_ce.place(x=60, y=150, width=50, height=50)
        button_c = tkinter.Button(self.root, text='C', command=self.sweeppress)
        button_c.place(x=115, y=150, width=50, height=50)
        button_zf = tkinter.Button(self.root, text='±', command=self.zf)
        button_zf.place(x=170, y=150, width=50, height=50)
        button_kpf = tkinter.Button(self.root, text='√', command=self.kpf)
        button_kpf.place(x=225, y=150, width=50, height=50)
        button_7 = tkinter.Button(self.root, text='7', command=lambda: self.pressnum('7'))
        button_7.place(x=5, y=205, width=50, height=50)
        button_8 = tkinter.Button(self.root, text='8', command=lambda: self.pressnum('8'))
        button_8.place(x=60, y=205, width=50, height=50)
        button_9 = tkinter.Button(self.root, text='9', command=lambda: self.pressnum('9'))
        button_9.place(x=115, y=205, width=50, height=50)
        button_division = tkinter.Button(self.root, text='/', command=lambda: self.presscalculate('/'))
        button_division.place(x=170, y=205, width=50, height=50)
        button_remainder = tkinter.Button(self.root, text='//', command=lambda:self.presscalculate('//'))
        button_remainder.place(x=225, y=205, width=50, height=50)
        button_4 = tkinter.Button(self.root, text='4', command=lambda: self.pressnum('4'))
        button_4.place(x=5, y=260, width=50, height=50)
        button_5 = tkinter.Button(self.root, text='5', command=lambda: self.pressnum('5'))
        button_5.place(x=60, y=260, width=50, height=50)
        button_6 = tkinter.Button(self.root, text='6', command=lambda: self.pressnum('6'))
        button_6.place(x=115, y=260, width=50, height=50)
        button_multiplication = tkinter.Button(self.root, text='*', command=lambda: self.presscalculate('*'))
        button_multiplication.place(x=170, y=260, width=50, height=50)
        button_reciprocal = tkinter.Button(self.root, text='1/x', command=self.ds)
        button_reciprocal.place(x=225, y=260, width=50, height=50)
        button_1 = tkinter.Button(self.root, text='1', command=lambda: self.pressnum('1'))
        button_1.place(x=5, y=315, width=50, height=50)
        button_2 = tkinter.Button(self.root, text='2', command=lambda: self.pressnum('2'))
        button_2.place(x=60, y=315, width=50, height=50)
        button_3 = tkinter.Button(self.root, text='3', command=lambda: self.pressnum('3'))
        button_3.place(x=115, y=315, width=50, height=50)
        button_subtraction = tkinter.Button(self.root, text='-', command=lambda: self.presscalculate('-'))
        button_subtraction.place(x=170, y=315, width=50, height=50)
        button_equal = tkinter.Button(self.root, text='=', command=lambda: self.pressequal())
        button_equal.place(x=225, y=315, width=50, height=105)
        button_0 = tkinter.Button(self.root, text='0', command=lambda: self.pressnum('0'))
        button_0.place(x=5, y=370, width=105, height=50)
        button_point = tkinter.Button(self.root, text='.', command=lambda: self.pressnum('.'))
        button_point.place(x=115, y=370, width=50, height=50)
        button_plus = tkinter.Button(self.root, text='+', command=lambda: self.presscalculate('+'))
        button_plus.place(x=170, y=370, width=50, height=50)


    def myfunc(self):
        tkinter.messagebox.showinfo('版本信息',"version1.0(beta)")
    
    def aboutit(self):
        tkinter.messagebox.showinfo('帮助',"前往我们的官网获取更多帮助。")
        webbrowser.open("http://192.168.31.128/", new=0, autoraise=True)



    def pressnum(self,num):

        if self.ispresssign == False:
            pass
        else:
            self.result.set(0)
         
            self.ispresssign = False
        if num == '.':
            num = '0.'
  
        oldnum = self.result.get()

        if oldnum == '0':
            self.result.set(num)
        else:
       
            newnum = oldnum + num

 
            self.result.set(newnum)



    def presscalculate(self,sign):

        num = self.result.get()
        self.lists.append(num)

        self.lists.append(sign)

        self.ispresssign = True


 
    def pressequal(self):
    
        curnum = self.result.get()
      
        self.lists.append(curnum)

        calculatestr = ''.join(self.lists)
  
        endnum = eval(calculatestr)

        self.result.set(str(endnum)[:10])
        if self.lists != 0:
            self.ispresssign = True

        self.lists.clear()

    def wait(self):
        tkinter.messagebox.showinfo('功能正在完善，请期待正式版本的发布')


    def dele_one(self):
        if self.result.get() == '' or self.result.get() == '0':
            self.result.set('0')
            return
        else:
            num = len(self.result.get())
            if num > 1:
                strnum = self.result.get()
                strnum = strnum[0:num - 1]
                self.result.set(strnum)
            else:
                self.result.set('0')

    def zf(self):
        strnum = self.result.get()
        if strnum[0] == '-':
            self.result.set(strnum[1:])
        elif strnum[0] != '-' and strnum != '0':
            self.result.set('-' + strnum)

    def ds(self):
        dsnum = 1 / int(self.result.get())
        self.result.set(str(dsnum)[:10])
        if self.lists != 0:
            self.ispresssign = True

        self.lists.clear()

    def sweeppress(self):
        self.lists.clear()
        self.result.set(0)

    def kpf(self):
        strnum = float(self.result.get())
        endnum = math.sqrt(strnum)
        if str(endnum)[-1] == '0':
            self.result.set(str(endnum)[:-2])
        else:
            self.result.set(str(endnum)[:10])
        if self.lists != 0:
            self.ispresssign = True
        self.lists.clear()
mycalculator = calculator()