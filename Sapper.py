from tkinter import *
from random import *
from tkinter import messagebox as mb


sizeGeneral = 0
difficult = 0
sizeW = 0
sizeH = 0
sumBombs = 0
numberField = 0
numberFieldIsNotBomb = 0
flag = 0
arrNeutralButtons = []
arrFields = []
arrBombButtons = []
arrNumbersBombs = []

def start_application():
    global window_start, difficult
    window_start = Tk()
    window_start.title("Сапер")
    screen_width = window_start.winfo_screenwidth()
    screen_height = window_start.winfo_screenheight()
    center_w = screen_width // 2  # середина экрана
    center_h = screen_height // 2
    shift_w = center_w - 200  # смещение от середины
    shift_h = center_h - 150
    window_start.geometry('400x300+{}+{}'.format(shift_w, shift_h))

    option = IntVar()
    option.set(1)
    difficult = option.get()

    def set_choice():
        global difficult
        difficult = option.get()

    label = Label(window_start, text="Выберите уровень сложности игры:")
    label.place(relx=.5, rely=.15, anchor="center")

    radio_button_easy = Radiobutton(window_start, text="Легкий", variable=option, value=1, command=set_choice)
    radio_button_easy.place(relx=.5, rely=.3, anchor="center")

    radio_button_medium = Radiobutton(window_start, text="Средний", variable=option, value=2, command=set_choice)
    radio_button_medium.place(relx=.5, rely=.4, anchor="center")

    radio_button_hard = Radiobutton(window_start, text="Тяжелый", variable=option, value=3, command=set_choice)
    radio_button_hard.place(relx=.5, rely=.5, anchor="center")

    enter_button = Button(text="Начать игру", command=start_game)
    enter_button.place(relx=.5, rely=.7, anchor="center")

    window_start.mainloop()


def start_game():
    global window_start, difficult, sizeW, sizeH, sizeGeneral
    settings(difficult)
    sizeGeneral = sizeW * sizeH
    window_start.destroy()
    create_game()


def settings(level):
    global sizeW, sizeH, sumBombs
    match level:
        case 1:
            sizeW = 4
            sizeH = 4
            sumBombs = 2
        case 2:
            sizeW = 5
            sizeH = 5
            sumBombs = 3
        case 3:
            sizeW = 6
            sizeH = 6
            sumBombs = 6


def on_bomb_button():
    global window_game
    for button in arrBombButtons:
        button['bg'] = 'red'
        button['text'] = 'Bomb'
    global flag
    flag = 1
    mb.showwarning('Проигрыш', 'К сожалению, Вы проиграли... Попробуйте еще раз!')
    window_game.destroy()


def on_neutral_button(number):
    global arrNeutralButtons, arrFields, flag, sumBombs, window_game
    arrNeutralButtons[number].config(bg='green')
    arrFields[number] = 1
    sum_green_fields = sizeGeneral - sumBombs
    if (sum(arrFields) == sum_green_fields) and (flag != 1):
        mb.showinfo('Победа!', 'Победа!')
        window_game.destroy()


def create_new_bomb():
    global sizeGeneral
    if len(arrNumbersBombs) == 0:
        number_new_bomb = randint(0, sizeGeneral)
        arrNumbersBombs.append(number_new_bomb)
    else:
        size_play_field = sizeGeneral - len(arrNumbersBombs)
        number_new_bomb = randint(0, size_play_field)
        while number_new_bomb in arrNumbersBombs:
            number_new_bomb = randint(0, size_play_field)
        arrNumbersBombs.append(number_new_bomb)
    return number_new_bomb


def create_bombs():
    for i in range(sumBombs):
        create_new_bomb()


def create_play_field():
    create_bombs()
    global numberField, numberFieldIsNotBomb, sizeW, sizeH
    for i in range(0, sizeGeneral):
        zero_element = 0
        arrFields.append(zero_element)

    for i in range(sizeW):
        for j in range(sizeH):
            if numberField in arrNumbersBombs:
                bomb_button = Button(width=6, height=3, command=on_bomb_button)
                bomb_button.grid(row=i, column=j)
                arrBombButtons.append(bomb_button)
            else:
                neutral_button = Button(width=6, height=3,
                                        command=lambda number=numberFieldIsNotBomb: on_neutral_button(number))
                neutral_button.grid(row=i, column=j)
                arrNeutralButtons.append(neutral_button)
                numberFieldIsNotBomb += 1
            numberField += 1


def centering(my_window):
    my_window.update_idletasks()
    s = my_window.geometry()
    s = s.split('+')
    s = s[0].split('x')
    width_window = int(s[0])
    height_window = int(s[1])

    screen_width = my_window.winfo_screenwidth()
    screen_height = my_window.winfo_screenheight()
    my_width = screen_width // 2
    my_height = screen_height // 2
    my_width = my_width - width_window // 2
    my_height = my_height - height_window // 2
    my_window.geometry('+{}+{}'.format(my_width, my_height))
    my_window.resizable(False, False)
    my_window.attributes('-topmost', True)
    my_window.update()
    my_window.attributes('-topmost', False)


def create_game():
    global window_game
    window_game = Tk()
    window_game.title('Сапер')
    create_play_field()
    centering(window_game)
    window_game.mainloop()


start_application()
