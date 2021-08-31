import tkinter
import tkinter.font


class Calculator(object):

    def __init__(self, a=None, b=None):
        self.a = a
        self.b = b
        self.function = None
        self._result = None
        self.command_count = 0
        self.iterative = 0
        self.point_var = False

    def point(self):
        global answer
        if self.a is None:
            answer.set("{}.".format(self.a))
            self.a = float(0)
        elif self.b is None:
            answer.set("{}.".format(self.a))
            self.a = float(self.a)
        elif self.b is not None:
            answer.set("{}.".format(self.b))
            self.b = float(self.b)
        self.point_var = True

    def add(self):
        global answer
        if self.b is not None:
            self._result = self.a + self.b
            self.a = self._result
            self.b = None
            answer.set("{}".format(self._result))
        self.command_count += 1
        self.function = "+"

    def subtract(self):
        global answer
        if self.b is not None:
            self._result = self.a - self.b
            self.a = self._result
            self.b = None
            answer.set("{}".format(self._result))
        self.function = "-"
        self.command_count += 1

    def multiply(self):
        global answer
        if self.a and self.b is not None:
            self._result = self.a * self.b
            self.a = self._result
            self.b = None
            answer.set("{}".format(self._result))
        self.command_count += 1
        self.function = "*"

    def divide(self):
        global answer
        if self.b is not None:
            if self.b == 0:
                self._result = 0
            else:
                self._result = self.a / self.b
            answer.set("{}".format(self._result))
            self.a = self._result
            self.b = None
        self.command_count += 1
        self.function = "/"

    def clear(self):
        global answer
        self.a = None
        self.b = None
        self.function = ""
        self._result = None
        answer.set("0")
        self.iterative = 0
        self.command_count = 0
        self.point_var = False

    def negative(self):
        global answer
        if self.a is not None:
            self._result = -self.a
            self.a *= -1
            answer.set("{}".format(self._result))

    def percent(self):
        global answer
        if self.a is not None:
            self._result = self.a / 100
            self.a = self._result
            answer.set("{}".format(self._result))
        self.command_count += 1

    def equals(self):
        global answer
        if "+" == self.function:
            self.add()
        elif '-' == self.function:
            self.subtract()
        elif '*' == self.function:
            self.multiply()
        elif '/' == self.function:
            self.divide()
        if self._result is not None:
            answer.set("{}".format(self._result))
        self.command_count = 0
        self.iterative = 0
        self.function = '='

    def _get_result(self):
        return self._result

    def _set_result(self):
        self._result = 0

    def numbers(self, parameter):
        global answer
        if self.function == '=':
            self.clear()
        if self.point_var is False:
            if self.iterative == self.command_count != 0:
                if self.a and self.b is not None and self._result is not None:
                    self.a = self._result
                    a = "{}{}".format(self.b, parameter)
                    self.b = a
                    answer.set(a)
                if self.a is not None and self.b is None:
                    a = "{}{}".format(self.a, parameter)
                    self.a = int(a)
                    answer.set("{}".format(int(a)))
                elif self.a is not None and self.b is not None:
                    a = "{}{}".format(self.b, parameter)
                    self.b = int(a)
                    answer.set("{}".format(int(a)))
            else:
                if self.a and self.b is not None and self._result is not None:
                    self._result = self.a
                    self.b = parameter
                    answer.set("{}".format(self.b))
                elif self.b is None and self.a is not None:
                    self.b = parameter
                    answer.set("{}".format(self.b))
                elif self.b is None and self.a is None:
                    self.a = parameter
                    answer.set("{}".format(self.a))
                self.iterative = 0
                self.command_count = 0
            self.iterative += 1
            self.command_count += 1
        else:
            self.point_var = False
            if self.iterative == self.command_count != 0:

                if self.a and self.b is not None and self._result is not None:
                    self.a = self._result
                    a = "{}.{}".format(int(self.b), parameter)
                    self.b = float(a)
                    answer.set(a)
                elif self.a is not None and self.b is None:
                    a = "{}.{}".format(int(self.a), parameter)
                    self.a = float(a)
                    answer.set("{}".format(float(a)))
                elif self.a and self.b is not None and self._result is None:
                    a = "{}.{}".format(int(self.b), parameter)
                    self.b = float(a)
                    answer.set("{}".format(float(a)))
                    print(self.a, self.b, self._result)
            else:
                if self.a and self.b is not None and self._result != 0:
                    self._result = self.a
                    self.b = parameter
                    answer.set("{}".format(self.b))
                elif self.b is None and self.a is not None:
                    self.b = parameter
                    answer.set("{}".format(self.b))
                elif self.b is None and self.a is None:
                    self.a = parameter
                    answer.set("{}".format(self.a))
                self.iterative = 0
                self.command_count = 0
            self.iterative += 1
            self.command_count += 1


def play():
    mainWindow.mainloop()


mainWindow = tkinter.Tk()
mainWindow.title("Calculator")
mainWindow.geometry("480x640")
mainWindow.configure(background='black', padx=5, pady=5)
mainWindow.minsize(300, 440)
mainWindow.maxsize(300, 440)

font = tkinter.font.Font(font='TkHeadingFont')

answer = tkinter.StringVar()
label = tkinter.Label(mainWindow, textvariable=answer, font=(font, 40), background='black', fg='white',
                      borderwidth=0, height=0, width=0)
label.grid(row=0, column=0, columnspan=4, sticky='e', padx=2, pady=2)

Calculator_command = Calculator()

Calculator_command_list = [[('AC', 1, lambda: Calculator_command.clear()),
                            ("+/-", 1, lambda: Calculator_command.negative()),
                            ("%", 1, lambda: Calculator_command.percent()),
                            ("÷", 1, lambda: Calculator_command.divide())],
                           [('7', 1, lambda: Calculator_command.numbers(7)),
                            ('8', 1, lambda: Calculator_command.numbers(8)),
                            ('9', 1, lambda: Calculator_command.numbers(9)),
                            ('x', 1, lambda: Calculator_command.multiply())],
                           [('4', 1, lambda: Calculator_command.numbers(4)),
                            ('5', 1, lambda: Calculator_command.numbers(5)),
                            ('6', 1, lambda: Calculator_command.numbers(6)),
                            ('-', 1, lambda: Calculator_command.subtract())],
                           [('1', 1, lambda: Calculator_command.numbers(1)),
                            ('2', 1, lambda: Calculator_command.numbers(2)),
                            ('3', 1, lambda: Calculator_command.numbers(3)),
                            ('+', 1, lambda: Calculator_command.add())],
                           [('0', 2, lambda: Calculator_command.numbers(0)),
                            ('.', 1, lambda: Calculator_command.point()),
                            ('=', 1, lambda: Calculator_command.equals())],
                           ]

frame = tkinter.Frame(mainWindow, background='black')
frame.grid(row=1, column=0, sticky='nsew', padx=2, pady=2)
row = 0

name = "orange_circle.png"
image_name = tkinter.PhotoImage(file=name)

for items in Calculator_command_list:
    data = 0
    for text, value, command in items:
        button = tkinter.Button(frame, image=image_name, compound="center", background='black', font=(font, 20),
                                activebackground="black", text='{}'.format(text), fg='white', border=0, command=command)
        button.grid(row=row, column=data, columnspan=value, sticky='nsew', padx=2, pady=2)

        data += value
    row += 1

if __name__ == "__main__":
    play()
