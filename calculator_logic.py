#calculator_logic.py

total = 0.0

class Calculator(object):

    def __init__(self):

        self.total = 0.0
        self.next_input = ""
        self.operator_value = None
        self.is_new_calculation = True

    def set_display_text(self, display_value):
        display_width = 16
        white_space = display_width - len(display_value)
        return_value = "*" * white_space + display_value

        #Used to be: self.display_variable = return_value
        return return_value

    def clear_command(self):
        self.set_null()
        self.total = 0.0

    #Called when next_input needs to be set to zero
    def set_null(self):
        self.next_input = "0"
        
    def delete_value(self):
        
        if len(self.next_input) > 1:
            self.next_input = self.next_input[:-1]
        else:
            self.set_null()
        
        self.set_display_text(self.next_input)

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

    def get_input(self, input_value):

        if self.is_new_calculation == True:
            self.clear_command()
            self.is_new_calculation = False

        if self.next_input != "0":
            self.next_input += input_value
        else:
            self.next_input = input_value

        self.set_display_text(self.next_input)

    def display_output(self):
        self.is_new_calculation = True
        self.calculate_total()
        #self.set_null()
        total_string = str(self.total)
        self.set_display_text(total_string)

my_calc = Calculator()

while True:
    
    my_var = input("Enter var: ")
    if my_var == "q":
        break


    if my_var in ('+', '-', '*', '/'):
        my_calc.set_command(my_var)

    elif my_var in ("0123456789"):
        my_calc.get_input(my_var)

    elif my_var == "=":
        my_calc.display_output()

    print("Total: ", my_calc.total)
    print("Input: ", my_calc.next_input)
    print()