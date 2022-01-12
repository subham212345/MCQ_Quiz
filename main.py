from tkinter import *
from questions import questions
import random


window = Tk()
window.title("ASO Quiz")
window.config(height=400, width=400, padx=25, pady=25)


def disable():
    option_a_button.config(state=DISABLED)
    option_b_button.config(state=DISABLED)
    option_c_button.config(state=DISABLED)
    option_d_button.config(state=DISABLED)


def next_question():
    result.config(text="")
    reset()
    qn_no = str(random.randint(1, len(questions.keys())))
    qn = str(questions[qn_no]["question"])
    opt_a = questions[qn_no]["options"][0]
    opt_b = questions[qn_no]["options"][1]
    opt_c = questions[qn_no]["options"][2]
    opt_d = questions[qn_no]["options"][3]
    message_box.config(text=qn)
    option_a_button.config(text=opt_a, command=lambda: choice_update(qn_no, "1"))
    option_b_button.config(text=opt_b, command=lambda: choice_update(qn_no, "2"))
    option_c_button.config(text=opt_c, command=lambda: choice_update(qn_no, "3"))
    option_d_button.config(text=opt_d, command=lambda: choice_update(qn_no, "4"))


def off():
    pass


def choice_update(question_number, a):
    correct_option = (questions[question_number]["correct answer"])
    explain = questions[question_number]["explanation"]
    if a == correct_option:
        result.config(text="Correct Answer", fg="green")
    else:
        result.config(text="Wrong Answer", fg="red")
    explanation_box.config(text=explain)
    disable()


def reset():
    global message_box, result, option_a_button, option_b_button, option_c_button, option_d_button, explanation_box, next_button
    message_box = Label(window, text="Press 'Next' to continue", font=("arial", 17, "bold"), fg="black", height=10, width=40)
    message_box.grid(row=0, column=0, columnspan=2)

    result = Label(window, text="", font=("arial", 20, "bold"), fg="black")
    result.grid(row=1, column=0)

    option_a_button = Button(height=5, width=25, text="Options-A", command=lambda: off(), bg="blue", fg="white")
    option_a_button.grid(row=1, column=1)
    option_b_button = Button(height=5, width=25, text="Options-B", command=lambda: off(), bg="blue", fg="white")
    option_b_button.grid(row=1, column=2)
    option_c_button = Button(height=5, width=25, text="Options-C", command=lambda: off(), bg="blue", fg="white")
    option_c_button.grid(row=1, column=3)
    option_d_button = Button(height=5, width=25, text="Options-D", command=lambda: off(), bg="blue", fg="white")
    option_d_button.grid(row=1, column=4)

    explanation_box = Label(window, text="", font=("arial", 15, "bold"), fg="black", height=20, width=45)
    explanation_box.grid(row=2, column=0)

    next_button = Button(height=5, width=25, text="Next", command=lambda: next_question(), bg="green", fg="white")
    next_button.grid(row=2, column=4)


reset()


window.mainloop()
