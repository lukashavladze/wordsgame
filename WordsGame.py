import tkinter
import random
from importing_words import geo_words_dict


# defining variables
black = (255, 255, 255)
correct_answer_count = []


# defining functions
def get_rand_word():
    # list_of_words = geo_words_dict.keys()
    global output
    global label
    output = random.choice(list(geo_words_dict.keys()))
    output_hint = geo_words_dict.get(output)
    return output, output_hint


# TODO update function unda sheicvalos, 1xel rom davachert sanam 0-ze ar chamova meorejer dacheram araferi qnas
def update(score=30):
    if 0 < score <= 30:
        score -= 1
        ScoreL.configure(text=score)
        window.after(1000, update, score)
    elif score == 0:
        ScoreL.configure(text=score)


# adds new word and makes count on correct answers
def add_new_word_correct():
    if 0 < ScoreL['text'] <= 29:
        if rbValue.get() == 1:
            get_rand_word()
            global label
            label['text'] = output
            remove_text()
            correct_answer_count.append('y')
            count1 = correct_answer_count.count('y')
            tkinter.Label(window, text=count1, font=32, background="white", relief="solid").place(x=120, y=250)
    # elif ScoreL['text'] == 0:
        elif rbValue.get() == 2:
            get_rand_word()
            label['text'] = output
            remove_text()
            correct_answer_count.append('x')
            count2 = correct_answer_count.count('x')
            tkinter.Label(window, text=count2, font=32, background="white", relief="solid").place(x=470, y=250)


# adds new word but with correct answer 0
def add_new_word_wrong():
    get_rand_word()
    global label
    label['text'] = output
    remove_text()


# gives us explanation of word
def hint():
    global label2
    # output_hint aris mocemuli rand_word funqciis key-s value
    output_hint = geo_words_dict.get(output)
    label2['text'] = output_hint


def remove_text():
    label2.config(text=" ")


# making tkinter window
window = tkinter.Tk()
window.geometry("600x400")
window.title("Words Game")
window.configure(background="light gray")

# making labels for words
label = tkinter.Label(window, text=get_rand_word(), font=32,  relief='solid', background="white")
label.pack(padx=1, pady=1)
label2 = tkinter.Label(window, text=get_rand_word(), font=32, relief='sunken')
label2.pack(padx=3, pady=3)



# making  buttons
correct = tkinter.Button(window, text="Correct", width=10, height=2, background="green",
                         command=add_new_word_correct).place(x=150, y=100)
wrong = tkinter.Button(window, text="Next", width=10, height=2, background="red",
                       command=add_new_word_wrong).place(x=300, y=100)

# start_button = tkinter.Button(window, text="start", width=20, height=3, background="green",
#                               command=update).place(x=220, y=300)
start_button = tkinter.Button(window, text="start", width=20, height=3, background="green",
                              command= update).place(x=220, y=300)

hint_button = tkinter.Button(window, text="Meaning", width=10, height=2, background="yellow",
                             command=hint).place(x=450, y=100)

# TODO casashlelia team_first da team_second-i
# team_first = input("Please enter first teams name: ")
# team_second = input("Please enter second teams name: ")
team_first = "First Team"
team_second = "Second Team"

# labels for team names
team1_label = tkinter.Label(window, text=team_first, font=32, background="gray", width=10, relief="solid").place(x=100, y=200)
team2_label = tkinter.Label(window, text=team_second, font=32, background="gray", width=10, relief="solid").place(x=450, y=200)

# making timer labels
ScoreL = tkinter.Label(window, text=30)
ScoreL.pack(padx=50, pady=140)

# making frames for radiobuttons
team1_button_frame = tkinter.LabelFrame(window, bg="green")
team1_button_frame.place(x=20, y=70)
rbValue = tkinter.IntVar()
rbValue.set(1)

# making radiobuttons
team1_button = tkinter.Radiobutton(team1_button_frame, text=team_first, value=1, variable=rbValue).pack(padx=10, pady=10)
team2_button = tkinter.Radiobutton(team1_button_frame, text=team_second, value=2, variable=rbValue).pack(padx=11, pady=11)


window.mainloop()
