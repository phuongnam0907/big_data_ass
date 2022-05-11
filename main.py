from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import PIL.Image, PIL.ImageTk
import cv2

BG_COLOR = 'white'

class videoGUI:

    def __init__(self, window, window_title):

        self.window = window
        self.window.title(window_title)

        self.window.rowconfigure(0, minsize=300, weight=1)
        self.window.columnconfigure(1, minsize=600, weight=1)

        top_frame_0 = Frame(self.window, bd=1)
        top_frame_0.grid(row=0, column=0)

        top_frame_1 = Frame(self.window, bd=1)
        top_frame_1.grid(row=0, column=1)

        top_frame_2 = Frame(self.window, bd=1)
        top_frame_2.grid(row=0, column=2)

        top_frame_3 = Frame(self.window, bd=1)
        top_frame_3.grid(row=0, column=3, ipadx=5)

        bottom_frame_0 = Frame(self.window)
        bottom_frame_0.grid(row=1, column=0)

        bottom_frame_1 = Frame(self.window)
        bottom_frame_1.grid(row=1, column=1, ipadx=5)

        bottom_frame_2 = Frame(self.window)
        bottom_frame_2.grid(row=1, column=2)

        bottom_frame_3 = Frame(self.window)
        bottom_frame_3.grid(row=1, column=3)

        self.pause_1 = False  # Parameter that controls pause button
        self.pause_2 = False  # Parameter that controls pause button

        self.canvas_1 = Canvas(top_frame_1)
        self.canvas_1.pack()
        self.canvas_1.config(width=400, height=300)
        self.canvas_2 = Canvas(top_frame_2)
        self.canvas_2.pack()
        self.canvas_2.config(width=400, height=300)

        # Select Button
        self.btn_select_1 = Button(bottom_frame_1, text="Select video", width=15, command=self.open_file_1)
        self.btn_select_1.grid(row=0, column=0)
        self.btn_select_2 = Button(bottom_frame_2, text="Select video", width=15, command=self.open_file_2)
        self.btn_select_2.grid(row=0, column=0)

        # Play Button
        self.btn_play_1 = Button(bottom_frame_1, text="Play", width=15, command=self.play_video_1)
        self.btn_play_1.grid(row=0, column=1)
        self.btn_play_2 = Button(bottom_frame_2, text="Play", width=15, command=self.play_video_2)
        self.btn_play_2.grid(row=0, column=1)

        # Pause Button
        self.btn_pause_1 = Button(bottom_frame_1, text="Pause", width=15, command=self.pause_video_1)
        self.btn_pause_1.grid(row=0, column=2)
        self.btn_pause_2 = Button(bottom_frame_2, text="Pause", width=15, command=self.pause_video_2)
        self.btn_pause_2.grid(row=0, column=2)

        # Resume Button
        self.btn_resume_1 = Button(bottom_frame_1, text="Resume", width=15, command=self.resume_video_1)
        self.btn_resume_1.grid(row=0, column=3)
        self.btn_resume_2 = Button(bottom_frame_2, text="Resume", width=15, command=self.resume_video_2)
        self.btn_resume_2.grid(row=0, column=3)

        # Dropdown Mode
        options = ["Counting Vehicle", "Measuring"]
        clicked_1 = StringVar()
        clicked_2 = StringVar()
        clicked_1.set("Select Mode")
        clicked_2.set("Select Mode")

        dropdown_1 = OptionMenu(bottom_frame_1, clicked_1, *options)
        dropdown_1.configure(widt=20)
        dropdown_1.grid(row=0, column=4)

        dropdown_2 = OptionMenu(bottom_frame_2, clicked_2, *options)
        dropdown_2.configure(widt=20)
        dropdown_2.grid(row=0, column=4)

        text_speed_avg_1 = StringVar()
        text_car_count_1 = StringVar()
        text_hp_para_1_1 = StringVar()
        text_hp_para_2_1 = StringVar()
        text_hp_para_3_1 = StringVar()
        text_speed_avg_2 = StringVar()
        text_car_count_2 = StringVar()
        text_hp_para_1_2 = StringVar()
        text_hp_para_2_2 = StringVar()
        text_hp_para_3_2 = StringVar()

        label_speed_avg_1 = Label(top_frame_0, text='Tốc độ trung bình:')
        label_car_count_1 = Label(top_frame_0, text='Số lượng xe:')
        label_hp_para_1_1 = Label(top_frame_0, text='Hyper Parameter 01:')
        label_hp_para_2_1 = Label(top_frame_0, text='Hyper Parameter 02:')
        label_hp_para_3_1 = Label(top_frame_0, text='Hyper Parameter 03:')
        label_speed_avg_2 = Label(top_frame_3, text='Tốc độ trung bình:')
        label_car_count_2 = Label(top_frame_3, text='Số lượng xe:')
        label_hp_para_1_2 = Label(top_frame_3, text='Hyper Parameter 01:')
        label_hp_para_2_2 = Label(top_frame_3, text='Hyper Parameter 02:')
        label_hp_para_3_2 = Label(top_frame_3, text='Hyper Parameter 03:')

        entry_speed_avg_1 = Entry(top_frame_0, textvariable=text_speed_avg_1,
                                background=BG_COLOR, borderwidth=0, highlightthickness=0)
        entry_car_count_1 = Entry(top_frame_0, textvariable=text_car_count_1,
                                background=BG_COLOR, borderwidth=0, highlightthickness=0)
        entry_hp_para_1_1 = Entry(top_frame_0, textvariable=text_hp_para_1_1)
        entry_hp_para_2_1 = Entry(top_frame_0, textvariable=text_hp_para_2_1)
        entry_hp_para_3_1 = Entry(top_frame_0, textvariable=text_hp_para_3_1)

        entry_speed_avg_2 = Entry(top_frame_3, textvariable=text_speed_avg_2,
                                  background=BG_COLOR, borderwidth=0, highlightthickness=0)
        entry_car_count_2 = Entry(top_frame_3, textvariable=text_car_count_2,
                                  background=BG_COLOR, borderwidth=0, highlightthickness=0)
        entry_hp_para_1_2 = Entry(top_frame_3, textvariable=text_hp_para_1_2)
        entry_hp_para_2_2 = Entry(top_frame_3, textvariable=text_hp_para_2_2)
        entry_hp_para_3_2 = Entry(top_frame_3, textvariable=text_hp_para_3_2)

        button_export_1 = Button(bottom_frame_0, text="Export to Excel")
        button_export_2 = Button(bottom_frame_3, text="Export to Excel")

        label_speed_avg_1.grid(row=0, column=0, sticky="n", padx=5, pady=5)
        label_car_count_1.grid(row=1, column=0, sticky="s", padx=5, pady=5)
        label_hp_para_1_1.grid(row=2, column=0, sticky="e", padx=5, pady=5)
        label_hp_para_2_1.grid(row=3, column=0, sticky="w", padx=5, pady=5)
        label_hp_para_3_1.grid(row=4, column=0, sticky="ew", padx=5, pady=5)
        button_export_1.grid(row=5, column=0, sticky="nsew", padx=5, pady=5)

        label_speed_avg_2.grid(row=0, column=0, sticky="n", padx=5, pady=5)
        label_car_count_2.grid(row=1, column=0, sticky="s", padx=5, pady=5)
        label_hp_para_1_2.grid(row=2, column=0, sticky="e", padx=5, pady=5)
        label_hp_para_2_2.grid(row=3, column=0, sticky="w", padx=5, pady=5)
        label_hp_para_3_2.grid(row=4, column=0, sticky="ew", padx=5, pady=5)
        button_export_2.grid(row=5, column=0, sticky="nsew", padx=5, pady=5)

        entry_speed_avg_2.grid(row=0, column=1, sticky="n", padx=0, pady=7)
        entry_car_count_2.grid(row=1, column=1, sticky="n", padx=0, pady=7)
        entry_hp_para_1_2.grid(row=2, column=1, sticky="n", padx=0, pady=7)
        entry_hp_para_2_2.grid(row=3, column=1, sticky="n", padx=0, pady=7)
        entry_hp_para_3_2.grid(row=4, column=1, sticky="n", padx=0, pady=7)

        entry_speed_avg_1.grid(row=0, column=1, sticky="n", padx=0, pady=7)
        entry_car_count_1.grid(row=1, column=1, sticky="n", padx=0, pady=7)
        entry_hp_para_1_1.grid(row=2, column=1, sticky="n", padx=0, pady=7)
        entry_hp_para_2_1.grid(row=3, column=1, sticky="n", padx=0, pady=7)
        entry_hp_para_3_1.grid(row=4, column=1, sticky="n", padx=0, pady=7)

        self.delay = 10  # ms

        self.window.mainloop()

    def open_file_1(self):
        self.pause_1 = False
        self.filename_1 = filedialog.askopenfilename(title="Select Video",
                                                     filetypes=(
                                                         ("MP4 files", "*.mp4"),
                                                         ("WMV files", "*.wmv"),
                                                         ("AVI files", "*.avi")))
        print(self.filename_1)

        # Open the video file
        self.cap_1 = cv2.VideoCapture(self.filename_1)

    def open_file_2(self):
        self.pause_2 = False
        self.filename_2 = filedialog.askopenfilename(title="Select Video",
                                                     filetypes=(
                                                         ("MP4 files", "*.mp4"),
                                                         ("WMV files", "*.wmv"),
                                                         ("AVI files", "*.avi")))
        print(self.filename_2)

        # Open the video file
        self.cap_2 = cv2.VideoCapture(self.filename_2)


    def get_frame_1(self):  # get only one frame
        try:
            if self.cap_1.isOpened():
                ret, frame = self.cap_1.read()
                return ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        except:
            # messagebox.showerror(title='Video_1 file not found', message='Please select a video file.')
            print("End of video_1")

    def get_frame_2(self):  # get only one frame
        try:
            if self.cap_2.isOpened():
                ret, frame = self.cap_2.read()
                return ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        except:
            # messagebox.showerror(title='Video_2 file not found', message='Please select a video file.')
            print("End of video_2")

    def play_video_1(self):
        # Get a frame from the video source, and go to the next frame automatically
        ret, frame = self.get_frame_1()
        if ret:
            self.photo_1 = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
            self.canvas_1.create_image(0, 0, image=self.photo_1, anchor=NW)

        if not self.pause_1:
            self.window.after(self.delay, self.play_video_1)

    def pause_video_1(self):
        self.pause_1 = True

    # Addition
    def resume_video_1(self):
        self.pause_1 = False
        self.play_video_1()

    def play_video_2(self):
        # Get a frame from the video source, and go to the next frame automatically
        ret, frame = self.get_frame_2()
        if ret:
            self.photo_2 = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
            self.canvas_2.create_image(0, 0, image=self.photo_2, anchor=NW)

        if not self.pause_2:
            self.window.after(self.delay, self.play_video_2)

    def pause_video_2(self):
        self.pause_2 = True

    # Addition
    def resume_video_2(self):
        self.pause_2 = False
        self.play_video_2()

    # Release the video source when the object is destroyed
    def __del__(self):
        if self.cap_1.isOpened():
            self.cap_1.release()
        if self.cap_2.isOpened():
            self.cap_2.release()


##### End Class #####


# Create a window and pass it to videoGUI Class
videoGUI(Tk(), "VEHICLE COUNTING AND SPEED ESTIMATING SYSTEM")
