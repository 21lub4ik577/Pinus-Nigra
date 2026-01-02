from tkinter import*
import random

def clear_canvas():
    canvas.delete("all")
    canvas.config(bg="indianRed1")


#MindReader
def show_mind_reader():
    canvas.delete("all")
    label = Label(canvas, text="ENTER NUMBER:", font=("consolas", 12, "bold"), bg="DarkOrchid1")
    canvas.create_window(95, 20, window=label)
    canvas.config(bg="DarkOrchid1")
    entry = Entry(canvas, font=("consolas", 12, "bold"), bg="yellow", width=10, justify="center")
    canvas.create_window(95, 50, window=entry)

    def process_number():
        number = entry.get()
        result_label.config(text="Wait...")
        canvas.update()
        canvas.after(3000, lambda:result_label.config(text="Calculations..."))
        canvas.after(5000, lambda: result_label.config(text=f"Your number: {number}"))

    ok_button = Button(canvas, text="Ok", font=("consolas", 12, "bold"), command=process_number, bg="brown1")
    canvas.create_window(95, 90, window=ok_button)

    result_label = Label(canvas, text="", font=("consolas", 12, "bold"), bg="DarkOrchid1")
    canvas.create_window(100, 130, window=result_label)


#Notepad
def show_notepad():
    clear_canvas()
    canvas.config(bg="indianRed1")
    notes = Text(canvas, font="consolas 12 bold", bg="indianRed1")
    canvas.create_window(98, 90, window=notes, width=195, height=180)
    try:
        with open("notes.txt", "r", encoding="utf-8") as file:
            notes.insert("1.0", file.read())
    except FileNotFoundError:
        pass

    def write(event=None):
        with open("notes.txt", "w", encoding="utf-8") as file:
            file.write(notes.get(1.0, END))

    notes.bind("<KeyRelease>", write)


#RPS
def show_rps():
    clear_canvas()
    canvas.config(bg="hot pink")
    canvas.create_text(95, 20, text="ROCK•PAPER•SCISSORS", font=("consolas", 11, "bold"))
    result = canvas.create_text(95, 120, text="Make your choice", font=("consolas", 11))
    choices = ["ROCK", "PAPER", "SCISSORS"]

    def play(user):
        canvas.itemconfig(result, text="Wait... ⏳", font=("consolas", 11, "bold"))
        computer = random.choice(choices)

        def show_result():
            if user == computer:
                text = f"Draw 🤝\nPC: {computer}"
            elif (user == "ROCK" and computer == "SCISSORS") or \
                (user == "SCISSORS" and computer == "PAPER") or \
                (user == "PAPER" and computer == "ROCK"):
                text = f"You win 🏆\nPC: {computer}"
            else:
                text = f"You lose 😢\nPC: {computer}"
            canvas.itemconfig(result, text=text)
        canvas.after(3000, show_result)

    b1 = Button(canvas, text="ROCK", width=7, command=lambda: play("ROCK"),bg="firebrick1", activebackground="firebrick4")
    b2 = Button(canvas, text="PAPER", width=7, command=lambda: play("PAPER"),bg="gold", activebackground="dark goldenrod")
    b3 = Button(canvas, text="SCISSORS", width=7, command=lambda: play("SCISSORS"),bg="green2", activebackground="green4")

    canvas.create_window(35, 60, window=b1)
    canvas.create_window(95, 60, window=b2)
    canvas.create_window(155, 60, window=b3)


#GuesNum
def show_gues_num():
    clear_canvas()
    canvas.config(bg="pale green")
    canvas.create_text(100, 25, text="GUES THE NUMBER \n(1-100)", font=("consolas", 11, "bold"), justify="center")
    entry = Entry(canvas, font=("consolas", 15, "bold"), width=10, justify="center", bg="coral1")
    canvas.create_window(100, 65, window=entry)
    result_label = Label(canvas, text="", font=("consolas", 12, "bold"), bg="pale green")
    canvas.create_window(95, 95, window=result_label)
    
    number_to_guess = random.randint(1, 100)

    def check_gues():
        try:
            guess = int(entry.get())
            if guess < number_to_guess:
                result_label.config(text="Too low! ⬇", bg="pale green")
            elif guess > number_to_guess:
                result_label.config(text="Too high! ⬆", bg="pale green")
            else:
                result_label.config(text="🎉POTUZHNO VGADAV!🎉", bg="pale green")
        except ValueError:
            result_label.config(text="INVALID VALUE!", bg="pale green")
    
    ok_button = Button(canvas, text="Check", font=("consolas", 12, "bold"), command=check_gues, bg="gold", activebackground="cyan3")
    canvas.create_window(95, 130, window=ok_button)


#MainMenu
window = Tk()
window.title("Pinus Nigra")
window.geometry("430x270")
window.resizable(False, False)
window.config(bg="SeaGreen1")

label = Label(window, text="Pinus Nigra", font=("consolas", 20, "bold"), fg="SpringGreen4", bg="SeaGreen1")
label.pack(pady=10)

canvas = Canvas(window, width=191, height=174, bg="indianRed1")
canvas.place(x=220, y=65)    
button1 = Button(window, text="Mind Reader", width=23, font="consolas 11 bold", bg="firebrick1",activebackground="firebrick4", command=show_mind_reader)
button2 = Button(window, text="Notepad", width=23, font="consolas 11 bold",bg="gold",activebackground="dark goldenrod", command=show_notepad)
button3 = Button(window, text="RPS", width=23, font="consolas 11 bold", bg="green2", activebackground="green4", command=show_rps)
button4 = Button(window, text="Gues Num", width=23, font="consolas 11 bold", bg="cyan2", activebackground="cyan4", command=show_gues_num)

button1.pack(anchor="w", pady=8, padx=10)
button2.pack(anchor="w", pady=8, padx=10)
button3.pack(anchor="w", pady=8, padx=10)
button4.pack(anchor="w", pady=8, padx=10)

window.mainloop()