import sys
from Calculation_variable import Calculation_variable

#Check Python version and import appropriate tkinter module
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

def is_integer_value(string_value):
    """
    This will assume a value is a float only if its value after the decimal place
    is above 0. Also assumes only the float, self.total, will ever get passed to it
    """
    temp_index = string_value.index('.')
    temp_value = string_value[temp_index+1:]

    return int(temp_value) == 0


# from inspect import getsource
# print getsource(Button)

#CONSTS
DIVIDE = u"\u00F7"
MULTIPLY= u"\u00D7"

class App():

    def __init__(self, master):

        self.master = master
        self.master.geometry("405x565")
        self.master.resizable(width=False, height=False)

        self.total = 0.0
        self.next_input = ""
        self.operator_value = None
        self.is_new_calculation = True  #Basically keeps track of whether equals has been pressed

        self.display_variable = StringVar()
        self.calculation_variable = Calculation_variable()

        display_frame = Frame(master)

        self.total_display = Entry(display_frame, textvariable=self.display_variable, width=19) #width is number of characters
        self.total_display.config(font=('times', 29), justify=RIGHT, borderwidth=5, relief=FLAT)
        self.total_display.pack()
        self.display_variable.set("0")

        self.total_calcuation_display = Entry(display_frame, textvariable=self.calculation_variable, width=24) #width is number of characters
        self.total_calcuation_display.config(font=('times', 24), justify=RIGHT, borderwidth=5, relief=FLAT)
        self.total_calcuation_display.pack()
        self.calculation_variable.set("")

        #Basically, whatever gets typed in goes into the cacluation display...
        #This should only disappear if
        # 1) equals button is pressed or
        # 2) the clear button is pressed

        display_frame.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

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

        self.master.bind("-", lambda val: self.set_command('-'))
        self.master.bind("+", lambda val: self.set_command('+'))
        self.master.bind("*", lambda val: self.set_command(MULTIPLY))
        self.master.bind("/", lambda val: self.set_command(DIVIDE))

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
        divide_button = Std_button(master, text=DIVIDE)
        divide_button.config(command=lambda:self.set_command(DIVIDE))
        divide_button.grid(row=1, column=1, pady=2)

        #Multiple Button
        multiply_button = Std_button(master, text=MULTIPLY)
        multiply_button.config(command = lambda:self.set_command(MULTIPLY))
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
        dot_button = Std_button(master, text='.', command = self.add_decimal)
        dot_button.grid(row=5, column=2, pady=2)

        #Plus button
        plus_button = Std_button(master, text='+', command = lambda: self.set_command('+'))
        plus_button.grid(row=2, column=3, pady=2)

        #Minus button
        minus_button = Std_button(master, text='-', command = lambda:self.set_command('-'))
        minus_button.grid(row=3, column=3, pady=2)

        #Equals button
        equals_button = Tall_button(master, text='=', command = self.display_output)
        equals_button.grid(row=4, column=3, rowspan=2, pady=2)


    def clear_command(self):

        self.next_input = "0"
        self.calculation_variable.clear()
        self.total = 0.0
        self.operator_value = None
        self.display_output()

    #Called when next_input needs to be set to zero
    # def set_null(self):

    #     self.next_input = "0"

    def delete_value(self):

        if len(self.next_input) > 1:
            self.next_input = self.next_input[:-1]
        else:
            self.next_input = "0"

        self.calculation_variable.delete()
        self.display_variable.set(self.next_input)


    def recalculate_total(self):

        temp_value = self.calculation_variable.get()

        i = 0
        for i, char in enumerate(temp_value):
            if char.isdigit() == False and char != '.':
                break

        temp_total = str(self.total)
        if is_integer_value(temp_total):
            temp_total = temp_total[:-2]

        new_value = temp_total + temp_value[i:]
        self.calculation_variable.set(new_value)


    def calculate_total(self):

        #Need an 'if new_calculation' here
        if self.is_new_calculation:
            self.recalculate_total()


        self.total = float(self.calculation_variable.calculate_total())
        # input_float = float(self.next_input)

        # if self.operator_value == None:
        #     self.total = input_float

        # elif self.operator_value == '+':
        #     self.total += input_float

        # elif self.operator_value == '-':
        #     self.total -= input_float

        # elif self.operator_value == MULTIPLY:
        #     self.total *= input_float

        # elif self.operator_value == DIVIDE:
        #     self.total /= input_float


    def set_command(self, command_value):

        if self.is_new_calculation == True:
            self.next_input = ""
            temp_total = str(self.total)
            if is_integer_value(temp_total):
                temp_total = temp_total[:-2]

            self.calculation_variable.set(temp_total)
            self.is_new_calculation = False

        else:
            self.calculate_total()

        self.operator_value = command_value
        self.calculation_variable.add(command_value)
        self.next_input = "0"


    def get_input(self, input_value):

        if self.is_new_calculation == True:
            self.is_new_calculation = False
            self.operator_value = None

        if self.next_input != "0":
            self.next_input += input_value
        else:
            self.next_input = input_value

        self.display_variable.set(self.next_input)
        self.calculation_variable.add(input_value)


    def add_decimal(self):

        if self.is_new_calculation == True:
            self.is_new_calculation = False
            self.operator_value = None

        if '.' not in self.next_input:
            self.next_input += '.'
            self.calculation_variable.add('.')

        self.display_variable.set(self.next_input)



    def display_output(self):

        try:
            self.calculate_total()
            """
            In future, this should be done based on the self.calculation_varible value
            """
            temp_total = str(self.total)

            if is_integer_value(temp_total):
                temp_total = temp_total[:-2]

            self.display_variable.set(temp_total)

        except ZeroDivisionError:
            self.clear_command()
            self.display_variable.set("Zero division error")

        self.is_new_calculation = True



if __name__ == "__main__":

    root = Tk()
    app = App(root)
    root.mainloop()
