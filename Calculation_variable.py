from __future__ import division #Need floating-point division
import sys

#Check Python version and import appropriate tkinter module
if sys.version_info.major == 3:
    from tkinter import *
else:
    from Tkinter import *

DIVIDE = u"\u00F7"
MULTIPLY= u"\u00D7"

class Calculation_variable(StringVar):

    # #Can't get super() working with old-style objects
    #  def __init__(self):
    #     super(StringVar, self).__init__()
    #     pass

    def add(self, string_value):

        temp_value = self.get()
        temp_value += string_value
        self.set(temp_value)

    def delete(self):

        temp_value = self.get()
        if temp_value:
            temp_value = temp_value[:-1]
            self.set(temp_value)

    def clear(self):

        self.set("")

    def calculate_total(self):

        temp_value = self.get()
        if not temp_value:
            return '0'

        temp_value = temp_value.replace(DIVIDE, '/').replace(MULTIPLY, '*')
        temp_value = "x=" + temp_value
        exec(temp_value)

        return x