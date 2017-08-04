import sys
if sys.version_info.major == 3:
    from tkinter import *
else:
    from Tkinter import *

class Std_button(Button):
    """Declare button with sandard hight and width"""
    def __init__(self, master=None, cnf={}, **kw):
        Button.__init__(self, master, kw)

        self.config(height=5, width=12)

class Tall_button(Button):
    """Declare button with sandard hight and width"""
    def __init__(self, master=None, cnf={}, **kw):
        Button.__init__(self, master, kw)

        self.config(height=11, width=12)

class Wide_button(Button):
    """Declare button with sandard hight and width"""
    def __init__(self, master=None, cnf={}, **kw):
        Button.__init__(self, master, kw)

        self.config(height=5, width=26)

# from inspect import getsource
# print getsource(Button)

class App():

    def __init__(self, master):

        self.master = master
        self.master.geometry("400x515")
        self.master.resizable(width=False, height=False)

        self.total = 0.0
        self.next_input = ""
        self.operator_value = None
        self.is_new_calculation = True  #Basically keeps track of whether equals has been pressed

        self.display_variable = StringVar()
        self.total_display = Entry(master, textvariable=self.display_variable, width=19) #width is number of characters
        self.total_display.config(font=('times', 29), justify=RIGHT, borderwidth=5, relief=FLAT)
        self.total_display.grid(row=0, column=0, columnspan=4, padx=5, pady=5)
        self.total_display.grid_propagate(False)
        self.display_variable.set("0")

        # self.calculation_variable = StringVar()
        # self.total_calcuation_display = Entry(master, textvariable=self.calculation_variable, width=19) #width is number of characters
        # self.total_calcuation_display.config(font=('times', 29), justify=RIGHT, borderwidth=5, relief=FLAT)
        # self.total_calcuation_display.grid(row=0, column=0, columnspan=4, padx=5, pady=5)
        # self.total_calcuation_display.grid_propagate(False)
        # self.display_variable.set("0")


        #############
        #Key Bindings
        #############

        #Keys 0-9
        for i in xrange(10):
            #Function creates new scope, so values are passed to lambda
            #   in key binding, rather than the variable itself.
            def make_lambda(x):
                return lambda val: self.get_input(str(x))

            self.master.bind(i, make_lambda(i))

        #Keys +, -, *, /
        for i in ("+-*/"):
            #Function creates new scope, so values are passed to lambda
            #   in key binding, rather than the variable itself.
            def make_lambda(x):
                return lambda val: self.set_command(x)

            self.master.bind(i, make_lambda(i))

        #keys = and <return>
        self.master.bind('=', lambda val: self.display_output())
        self.master.bind('<Return>', lambda val: self.display_output())

        #BackSpace and del keys
        self.master.bind('<Delete>', lambda val: self.delete_value())
        self.master.bind('<BackSpace>', lambda val: self.delete_value())

        #Decimal Place key
        self.master.bind('.', lambda val: self.add_decimal())

        #Clear button mapped to 'c' key and Num_lock
        self.master.bind('c', lambda val: self.clear_command())


        ##################
        #Interface Buttons
        ##################

        #Clear Button
        clear_button = Std_button(master, text="C")
        clear_button.config(command=self.clear_command)
        clear_button.grid(row=1, column=0, pady=2)

        #Divide Button
        divide_button = Std_button(master, text="/")
        divide_button.config(command=lambda:self.set_command("/"))
        divide_button.grid(row=1, column=1, pady=2)

        #Multiple Button
        multiply_button = Std_button(master, text="X")
        multiply_button.config(command = lambda:self.set_command("*"))
        multiply_button.grid(row=1, column=2, pady=2)

        #Delete Button
        delete_button = Std_button(master, text="Del")
        delete_button.config(command=self.delete_value)
        delete_button.grid(row=1, column=3, pady=2)

        #Set One
        button_1 = Std_button(master, text="1", command = lambda:self.get_input("1"))
        button_1.grid(row=4, column=0, pady=2)

        #Set Two
        button_2 = Std_button(master, text="2", command = lambda:self.get_input("2"))
        button_2.grid(row=4, column=1, pady=2)

        #Set Three
        button_3 = Std_button(master, text="3", command = lambda:self.get_input("3"))
        button_3.grid(row=4, column=2, pady=2)

        #Set Four
        button_4 = Std_button(master, text="4", command = lambda:self.get_input("4"))
        button_4.grid(row=3, column=0, pady=2)

        #Set Five
        button_5 = Std_button(master, text="5", command = lambda:self.get_input("5"))
        button_5.grid(row=3, column=1, pady=2)

        #Set Six
        button_6 = Std_button(master, text="6", command = lambda:self.get_input("6"))
        button_6.grid(row=3, column=2, pady=2)

        #Set Seven
        button_7 = Std_button(master, text="7", command = lambda:self.get_input("7"))
        button_7.grid(row=2, column=0, pady=2)

        #Set Eight
        button_8 = Std_button(master, text="8", command = lambda:self.get_input("8"))
        button_8.grid(row=2, column=1, pady=2)

        #Set Nine
        button_9 = Std_button(master, text="9", command = lambda:self.get_input("9"))
        button_9.grid(row=2, column=2, pady=2)

        #set_zero
        button_0 = Wide_button(master, text="0", command = lambda:self.get_input("0"))
        button_0.grid(row=5, column=0, columnspan=2, pady=2)

        #decimal button
        dot_button = Std_button(master, text=".", command = self.add_decimal)
        dot_button.grid(row=5, column=2, pady=2)

        #Plus button
        plus_button = Std_button(master, text="+", command = lambda: self.set_command('+'))
        plus_button.grid(row=2, column=3, pady=2)

        #Minus button
        minus_button = Std_button(master, text="-", command = lambda:self.set_command('-'))
        minus_button.grid(row=3, column=3, pady=2)

        #Equals button
        equals_button = Tall_button(master, text="=", command = self.display_output)
        equals_button.grid(row=4, column=3, rowspan=2, pady=2)


    # #This can probably be removed
    # def set_display_text(self, display_value):

    #     display_width = 16
    #     # white_space = display_width - len(display_value)
    #     # return_value = '*' * white_space + display_value

    #     self.display_variable.set(display_value)


    def clear_command(self):

        self.set_null()
        self.total = 0.0
        self.operator_value = None
        self.display_output()

    #Called when next_input needs to be set to zero
    def set_null(self):

        self.next_input = "0"


    def delete_value(self):

        if len(self.next_input) > 1:
            self.next_input = self.next_input[:-1]
        else:
            self.set_null()

        self.display_variable.set(self.next_input)


    def calculate_total(self):

        input_float = float(self.next_input)

        if self.operator_value == None:
            self.total = input_float

        elif self.operator_value == '+':
            self.total += input_float

        elif self.operator_value == '-':
            self.total -= input_float

        elif self.operator_value == '*':
            self.total *= input_float

        elif self.operator_value == '/':
            self.total /= input_float


    def set_command(self, command_value):

        if self.is_new_calculation == True:
            self.next_input = ""
            self.is_new_calculation = False

        else:
            self.calculate_total()

        self.operator_value = command_value
        self.set_null()


    def check_new_calculation(self):

        if self.is_new_calculation == True:
            self.clear_command()
            self.is_new_calculation = False
            self.operator_value = None


    def get_input(self, input_value):

        self.check_new_calculation()

        if self.next_input != "0":
            self.next_input += input_value
        else:
            self.next_input = input_value

        self.display_variable.set(self.next_input)


    def add_decimal(self):

        self.check_new_calculation()

        if '.' not in self.next_input:
            self.next_input += '.'

        self.display_variable.set(self.next_input)


    def display_output(self):

        self.is_new_calculation = True
        try:
            self.calculate_total()
            total_string = str(self.total)

            if total_string.endswith(".0"):
                total_string = total_string[:-2]

            self.display_variable.set(total_string)
        except ZeroDivisionError:
            self.clear_command()
            self.display_variable.set("Zero division error")



if __name__ == "__main__":

    root = Tk()
    app = App(root)
    root.mainloop()
