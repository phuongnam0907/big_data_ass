from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

BG_COLOR = 'white'


def set_text():
    text_speed_avg.set(1230)
    text_car_count.set(1231)
    text_hp_para_1.set(1232)
    text_hp_para_2.set(1233)
    text_hp_para_3.set(1234)


window = Tk()
window.title("VEHICLE COUNTING AND SPEED ESTIMATING SYSTEM")

window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)
window.configure(background=BG_COLOR)

left_form = Frame(window, relief=RAISED, bd=1, background=BG_COLOR)
right_form = Frame(window, relief=RAISED, bd=1, background=BG_COLOR)

# txt_edit = tk.Text(window)
# frm_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
# btn_open = tk.Button(frm_buttons, text="Open", command=open_file)
# btn_save = tk.Button(frm_buttons, text="Save As...", command=save_file)

# btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
# btn_save.grid(row=1, column=0, sticky="ew", padx=5)

# frm_buttons.grid(row=0, column=0, sticky="ns")
# txt_edit.grid(row=0, column=1, sticky="nsew")

######################## LEFT SIDE ############################

text_speed_avg = StringVar()
text_car_count = StringVar()
text_hp_para_1 = StringVar()
text_hp_para_2 = StringVar()
text_hp_para_3 = StringVar()

label_speed_avg = Label(left_form, background=BG_COLOR, text='Tốc độ trung bình:')
label_car_count = Label(left_form, background=BG_COLOR, text='Số lượng xe:')
label_hp_para_1 = Label(left_form, background=BG_COLOR, text='Hyper Parameter 01:')
label_hp_para_2 = Label(left_form, background=BG_COLOR, text='Hyper Parameter 02:')
label_hp_para_3 = Label(left_form, background=BG_COLOR, text='Hyper Parameter 03:')

entry_speed_avg = Entry(left_form, textvariable=text_speed_avg,
                        background=BG_COLOR, borderwidth=0, highlightthickness=0)
entry_car_count = Entry(left_form, textvariable=text_car_count,
                        background=BG_COLOR, borderwidth=0, highlightthickness=0)
entry_hp_para_1 = Entry(left_form, textvariable=text_hp_para_1,
                        background=BG_COLOR, borderwidth=0, highlightthickness=0)
entry_hp_para_2 = Entry(left_form, textvariable=text_hp_para_2,
                        background=BG_COLOR, borderwidth=0, highlightthickness=0)
entry_hp_para_3 = Entry(left_form, textvariable=text_hp_para_3,
                        background=BG_COLOR, borderwidth=0, highlightthickness=0)

button_export = Button(left_form, text="Export to Excel", command=set_text)

label_speed_avg.grid(row=0, column=0, sticky="n", padx=5, pady=5)
label_car_count.grid(row=1, column=0, sticky="s", padx=5, pady=5)
label_hp_para_1.grid(row=2, column=0, sticky="e", padx=5, pady=5)
label_hp_para_2.grid(row=3, column=0, sticky="w", padx=5, pady=5)
label_hp_para_3.grid(row=4, column=0, sticky="ew", padx=5, pady=5)
button_export.grid(row=5, column=0, sticky="s", padx=5, pady=5)

# entry_speed_avg.place(width=1)
# entry_car_count.place(width=1)
# entry_hp_para_1.place(width=1)
# entry_hp_para_2.place(width=1)
# entry_hp_para_3.place(width=1)

entry_speed_avg.grid(row=0, column=1, sticky="n", padx=0, pady=7)
entry_car_count.grid(row=1, column=1, sticky="n", padx=0, pady=7)
entry_hp_para_1.grid(row=2, column=1, sticky="n", padx=0, pady=7)
entry_hp_para_2.grid(row=3, column=1, sticky="n", padx=0, pady=7)
entry_hp_para_3.grid(row=4, column=1, sticky="n", padx=0, pady=7)

######################## RIGHT SIDE ############################

label_monitor = Label(right_form, background=BG_COLOR, text='Monitor 1')
label_source = Label(right_form, background=BG_COLOR, text='Source:')
label_mode = Label(right_form, background=BG_COLOR, text='Mode:')

button_open_source = Button(right_form, text="Video or Camera", command=set_text)

options = ["Counting Vehicle", "Measuring"]
clicked = StringVar()
clicked.set("Select Mode")
dropdown = OptionMenu(right_form, clicked, *options)
dropdown.configure(widt=20)

label_monitor.grid(row=0, column=0, sticky="n", padx=5, pady=5)
label_source.grid(row=0, column=1, sticky="n", padx=5, pady=5)
label_mode.grid(row=0, column=2, sticky="s", padx=5, pady=5)

button_open_source.grid(row=1, column=1, sticky="s", padx=5, pady=5)
dropdown.grid(row=1, column=2, sticky="s", padx=5, pady=5)

######################## END ############################

left_form.grid(row=0, column=0, sticky="nsew")
right_form.grid(row=0, column=1, sticky="nsew")

window.mainloop()
