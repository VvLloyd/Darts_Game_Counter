from tkinter import *
import centerWindow as cW
from PIL import ImageTk, Image

def populateGUI(self, master):
    master.configure(bg=self.Button_bg_color)
    master.title("Score Board")
    master.geometry("1080x880")
    master.resizable(False, False)
    master.iconbitmap("./data/images/dart_icon.ico")
    cW.centerWindow(master)

    # --------------------------------------------------------------------------------------------------------------
    #   Create Frames for the UI Layout
    # --------------------------------------------------------------------------------------------------------------
    self.BackgroundFrame = LabelFrame(master, padx=5, pady=5, bg=self.Button_bg_color)
    self.BackgroundFrame.grid(row=0, column=0, sticky=NSEW)

    # Add player button frame
    self.frame0 = LabelFrame(self.BackgroundFrame, padx=5, pady=5, bg=self.Button_bg_color)
    self.frame0.grid(row=0, column=0, columnspan=7, sticky="W")

    # To create horizontal space between frames (this area provide instructions & Game Status)
    self.emptylabel0 = Label(self.BackgroundFrame, padx=25, pady=30, bg=self.Button_bg_color)
    self.emptylabel0.grid(row=2, column=0, columnspan=3)

    # To create a vertical space between first column of frames
    self.emptylabel_1 = Label(self.BackgroundFrame, padx=20, pady=5, bg=self.Button_bg_color)
    self.emptylabel_1.grid(row=2, column=0, rowspan=14)

    # Calculator and submit button frame
    self.frame1 = LabelFrame(self.BackgroundFrame, padx=25, pady=10, bg=self.Button_bg_color)
    self.frame1.grid(row=5, column=0, columnspan=3, rowspan=5)

    # To create a vertical space after first column of frames
    self.emptylabel_3 = Label(self.BackgroundFrame, padx=20, pady=10, bg=self.Button_bg_color)
    self.emptylabel_3.grid(row=5, column=4, rowspan=2)

    # To create vertical space between frames
    self.emptylabel_3 = Label(self.BackgroundFrame, padx=25, pady=2, bg=self.Button_bg_color)
    self.emptylabel_3.grid(row=0, column=10, columnspan=5, rowspan=5)

    # Entry Score frame
    self.frame2 = LabelFrame(self.BackgroundFrame, padx=10, pady=10, bg=self.Button_bg_color)
    self.frame2.grid(row=3, column=0, columnspan=3)

    # Start Game button frame
    self.frame9 = LabelFrame(self.BackgroundFrame, padx=10, pady=10, bg=self.Button_bg_color)
    self.frame9.grid(row=3, column=4, columnspan=7, rowspan=1, sticky=W)

    # End turn button frame
    self.frame7 = LabelFrame(self.BackgroundFrame, padx=10, pady=5, bg=self.Button_bg_color)
    self.frame7.grid(row=10, column=0, columnspan=3)

    # --------------------------------------------------------------------------------------------------------------
    #   CREATING BUTTONS
    # --------------------------------------------------------------------------------------------------------------

    # Define buttons
    # Clickpad
    self.button_0 = Button(self.frame1, text="0", padx=40, pady=20, font=("Helvetica", 25), bg=self.Button_bg_color,
                           fg=self.Button_ft_color, command=lambda: self.clickPad(0),
                           activebackground=self.activeButton_bg_color, activeforeground=self.activeButton_ft_color)

    self.button_1 = Button(self.frame1, text="1", padx=40, pady=20, font=("Helvetica", 25), bg=self.Button_bg_color,
                           fg=self.Button_ft_color, command=lambda: self.clickPad(1),
                           activebackground=self.activeButton_bg_color, activeforeground=self.activeButton_ft_color)

    self.button_2 = Button(self.frame1, text="2", padx=40, pady=20, font=("Helvetica", 25), bg=self.Button_bg_color,
                           fg=self.Button_ft_color, command=lambda: self.clickPad(2),
                           activebackground=self.activeButton_bg_color, activeforeground=self.activeButton_ft_color)

    self.button_3 = Button(self.frame1, text="3", padx=40, pady=20, font=("Helvetica", 25), bg=self.Button_bg_color,
                           fg=self.Button_ft_color, command=lambda: self.clickPad(3),
                           activebackground=self.activeButton_bg_color, activeforeground=self.activeButton_ft_color)

    self.button_4 = Button(self.frame1, text="4", padx=40, pady=20, font=("Helvetica", 25), bg=self.Button_bg_color,
                           fg=self.Button_ft_color, command=lambda: self.clickPad(4),
                           activebackground=self.activeButton_bg_color, activeforeground=self.activeButton_ft_color)

    self.button_5 = Button(self.frame1, text="5", padx=40, pady=20, font=("Helvetica", 25), bg=self.Button_bg_color,
                           fg=self.Button_ft_color, command=lambda: self.clickPad(5),
                           activebackground=self.activeButton_bg_color, activeforeground=self.activeButton_ft_color)

    self.button_6 = Button(self.frame1, text="6", padx=40, pady=20, font=("Helvetica", 25), bg=self.Button_bg_color,
                           fg=self.Button_ft_color, command=lambda: self.clickPad(6),
                           activebackground=self.activeButton_bg_color, activeforeground=self.activeButton_ft_color)

    self.button_7 = Button(self.frame1, text="7", padx=40, pady=20, font=("Helvetica", 25), bg=self.Button_bg_color,
                           fg=self.Button_ft_color, command=lambda: self.clickPad(7),
                           activebackground=self.activeButton_bg_color, activeforeground=self.activeButton_ft_color)

    self.button_8 = Button(self.frame1, text="8", padx=40, pady=20, font=("Helvetica", 25), bg=self.Button_bg_color,
                           fg=self.Button_ft_color, command=lambda: self.clickPad(8),
                           activebackground=self.activeButton_bg_color, activeforeground=self.activeButton_ft_color)

    self.button_9 = Button(self.frame1, text="9", padx=40, pady=20, font=("Helvetica", 25), bg=self.Button_bg_color,
                           fg=self.Button_ft_color, command=lambda: self.clickPad(9),
                           activebackground=self.activeButton_bg_color, activeforeground=self.activeButton_ft_color)


    # Commit Score
    self.button_commitScore = Button(self.frame1, text="Soumettre", padx=100, pady=20, font=("Helvetica", 25),
                                     bg=self.Button_bg_color, fg=self.currentplayer_color, command=self.commitScore,
                                     activebackground=self.activeButton_bg_color,
                                     activeforeground=self.activeButton_ft_color,
                                     state="disabled")

    self.button_clear = Button(self.frame1, text="C", padx=99.49999, pady=20, font=("Helvetica", 25),
                               bg=self.Button_bg_color, fg=self.Button_ft_color, command=self.clearClickPad,
                               activebackground=self.activeButton_bg_color, activeforeground=self.activeButton_ft_color)

    self.button_addPlayer = Button(self.frame0, text="Ajouter Joueur", padx=35, pady=3, font=("Helvetica", 12),
                                   bg=self.Button_bg_color, fg=self.Button_ft_color, command=self.addPlayer,
                                   activebackground=self.activeButton_bg_color,
                                   activeforeground=self.activeButton_ft_color)

    self.button_gameMode = Button(self.frame0, text="Mode de Jeu", padx=35, pady=3, font=("Helvetica", 12),
                                  bg=self.Button_bg_color, fg=self.Button_ft_color, state='normal',
                                  command=lambda: self.populateGModeGUI(master),
                                  activebackground=self.activeButton_bg_color,
                                  activeforeground=self.activeButton_ft_color)

    self.button_editScore = Button(self.frame0, text="Modifier Pointage", padx=20, pady=3, font=("Helvetica", 12),
                                   bg=self.Button_bg_color, fg=self.Button_ft_color, command=self.editScore,
                                   activebackground=self.activeButton_bg_color,
                                   activeforeground=self.activeButton_ft_color,
                                   state="disabled")

    self.button_editName = Button(self.frame0, text="Renommer Joueur", padx=20, pady=3, font=("Helvetica", 12),
                                  bg=self.Button_bg_color, fg=self.Button_ft_color, state=DISABLED,
                                  command=self.editName,
                                  activebackground=self.activeButton_bg_color,
                                  activeforeground=self.activeButton_ft_color)

    self.button_gameStart = Button(self.frame9, text="Démarrer Partie!", padx=40, pady=5,
                                   font=("Helvetica", 14, "bold"),
                                   bg=self.Button_bg_color, fg=self.Button_ft_color, command=self.startGame,
                                   activebackground=self.activeButton_bg_color,
                                   activeforeground=self.activeButton_ft_color, state="disabled")

    self.button_endTurn = Button(self.frame7, text="Tour terminé", padx=40, pady=5, font=("Helvetica", 12),
                                 bg=self.Button_bg_color, fg=self.Button_ft_color,
                                 command=self.endTurn, state="disabled",
                                 activebackground=self.activeButton_bg_color,
                                 activeforeground=self.activeButton_ft_color)

    # self.button_goBack = Button(master, text="<<", padx=5, pady=1, font=("Helvetica", 10),
    #                           bg=self.Button_bg_color, fg=self.Button_ft_color, state="normal", relief="groove",
    #                          activebackground=self.activeButton_bg_color,
    #                         activeforeground=self.activeButton_ft_color)

    # self.button_forward = Button(master, text=">>", padx=5, pady=1, font=("Helvetica", 10),
    #                            bg=self.Button_bg_color, fg=self.Button_ft_color, state="normal", relief="groove",
    #                           activebackground=self.activeButton_bg_color,
    #                          activeforeground=self.activeButton_ft_color)

    self.button_quit = Button(self.BackgroundFrame, text="Quitter", padx=40, pady=5, font=("Helvetica", 12),
                              bg=self.Button_bg_color, fg=self.Button_ft_color,
                              activebackground=self.activeButton_bg_color, activeforeground=self.activeButton_ft_color,
                              command=lambda: self.quitGame(master))

    # Warning: The restartBoard kills the window without changing the status of the quitGamePressed variable in the run.py.
    # This will cause the while loop to restart again.
    self.button_restartBoard = Button(self.BackgroundFrame, text="Réinitialiser Jeu", padx=40, pady=5,
                                      font=("Helvetica", 12),
                                      bg=self.Button_bg_color, fg=self.Button_ft_color, command=master.quit,
                                      state=NORMAL,
                                      activebackground=self.activeButton_bg_color,
                                      activeforeground=self.activeButton_ft_color)

    # Put the buttons on the screen
    self.button_0.grid(row=4, column=0)
    self.button_1.grid(row=3, column=0)
    self.button_2.grid(row=3, column=1)
    self.button_3.grid(row=3, column=2)
    self.button_4.grid(row=2, column=0)
    self.button_5.grid(row=2, column=1)
    self.button_6.grid(row=2, column=2)
    self.button_7.grid(row=1, column=0)
    self.button_8.grid(row=1, column=1)
    self.button_9.grid(row=1, column=2)
    self.button_commitScore.grid(row=5, column=0, columnspan=3)
    self.button_clear.grid(row=4, column=1, columnspan=2)
    self.button_addPlayer.grid(row=0, column=0, columnspan=1)
    self.button_gameMode.grid(row=0, column=2, columnspan=1)
    self.button_editScore.grid(row=0, column=3, columnspan=1)
    self.button_editName.grid(row=0, column=4, columnspan=1)
    self.button_endTurn.grid(row=0, column=0, columnspan=1)
    self.button_gameStart.grid(row=0, column=3, columnspan=1)
    # self.button_goBack.grid(row=13, column=5, ipadx=5, columnspan=1, sticky="SE")
    # self.button_forward.grid(row=13, column=6, ipadx=5, columnspan=1, sticky="SW")
    self.button_restartBoard.grid(row=13, column=10, columnspan=1, sticky="SE")
    self.button_quit.grid(row=13, column=11, columnspan=1, sticky="SE")  


    # ---------------------------------------------------------------------------------------------------------------
    # CREATING ENTRY BOXES
    # ---------------------------------------------------------------------------------------------------------------
    # Create Score Entry box
    self.input_Score = Entry(self.frame2, width=5, bg='black', fg=self.currentplayer_color, borderwidth=3, font=("Helvetica", 50),
                             justify='center', disabledbackground='black', disabledforeground=self.currentplayer_color,
                             state=DISABLED)
    self.input_Score.grid(row=0, column=0, columnspan=3) 


    
    # CREATING PLAYERS ENTRY BOXES
    # First Player Name and Score  
    # ===============================
    # PLAYERS FRAMES
    # ===============================
    player_frames = [
        ("frame_player_1", 5, 4, 4, 2),
        ("frame_player_2", 5, 8, 4, 2),
        ("frame_player_3", 7, 4, 4, 6),
        ("frame_player_4", 7, 8, 4, 6),
    ]

    for name, row, col, colspan, rowspan in player_frames:
        frame = LabelFrame(
            self.BackgroundFrame,
            padx=29,
            pady=20,
            bg=self.Button_bg_color,
            highlightbackground=self.Button_bg_color,   # border color
            highlightthickness=2         # border width
        )
        frame.grid(row=row, column=col, columnspan=colspan, rowspan=rowspan)
        setattr(self, name, frame)
    
    # ---------- Player Frames ----------
    self.player_frames_list = [
        self.frame_player_1,
        self.frame_player_2,
        self.frame_player_3,
        self.frame_player_4
    ]

    # Lists to store references for later use
    self.player_name_labels = []
    self.player_score_labels = []
    self.player_doubleIn_vars = []
    self.player_labels_dict = {}  # Optional dict per player
    self.player_buttons_dict = {}

    # ---------- Helper Functions ----------
    def create_entry(frame, width, font, justify='center', borderwidth=1, border_zero=True):
        return Entry(
            frame,
            width=width,
            bg=self.Button_bg_color,
            fg="grey",
            borderwidth=borderwidth,
            font=font,
            justify=justify,
            disabledbackground=self.Button_bg_color,
            disabledforeground="grey",
            border=0 if border_zero else borderwidth
        )

    def setup_entry(widget, row, column, text, pady=0, sticky=None, columnspan=None):
        widget.grid(row=row, column=column, pady=pady, sticky=sticky, columnspan=columnspan)
        widget.insert(0, text)
        widget.config(state=DISABLED)

    # ---------- Loop for 4 players ----------
    for i, frame in enumerate(self.player_frames_list, start=1):

        self.player_labels_dict[i] = {}

        # Name entry
        name_entry = create_entry(frame, 16, ("Helvetica", 14))
        setup_entry(name_entry, 0, 0, f"Ajoutez le Joueur #{i}", columnspan=3)
        self.player_labels_dict[i]['name'] = name_entry
        self.player_name_labels.append(name_entry)

        # AVR and HighScore entries
        avr_entry = create_entry(frame, 10, ("Helvetica", 8), justify='right')
        highscore_entry = create_entry(frame, 15, ("Helvetica", 8), justify='right')
        self.player_labels_dict[i]['avr'] = avr_entry
        self.player_labels_dict[i]['highscore'] = highscore_entry

        # Score entry (big number) keeps black border
        score_entry = create_entry(frame, 6, ("Helvetica", 25), borderwidth=1, border_zero=False)
        self.player_labels_dict[i]['score'] = score_entry
        self.player_score_labels.append(score_entry)
        
        mode = self.match_inst.CommitGameMode[0]

        # ---------- 301 / 501 ----------
        if mode in (1, 2):
            starting_score = "301" if mode == 1 else "501"

            # Double-In
            if self.match_inst.doubleInMode:
                var = IntVar()
                self.player_doubleIn_vars.append(var)
                self.player_labels_dict[i]['doubleIn_var'] = var

                checkbox = Checkbutton(
                    frame,
                    onvalue=True,
                    offvalue=0,
                    variable=var,
                    command=self.DoubleIncheckChanged,
                    disabledforeground=self.disabledButton_ft_color,
                    font="black",
                    bg=self.Button_bg_color,
                    state="disabled"
                )
                checkbox.grid(row=3, column=2, pady=0, sticky=E)
                self.player_labels_dict[i]['doubleIn_checkbox'] = checkbox

                double_in_label = create_entry(frame, 0, ("Helvetica", 8), justify='right')
                setup_entry(double_in_label, 3, 1, "Double In: ", sticky=E)
                self.player_labels_dict[i]['double_in'] = double_in_label

            setup_entry(score_entry, 2, 0, starting_score, pady=10, columnspan=3)
            setup_entry(avr_entry, 4, 1, "Avr: --", sticky=E)
            setup_entry(highscore_entry, 5, 1, "HighScore: --", sticky=E)

       # ---------- Mode 7 ----------
        elif mode == 7:

            self.player_labels_dict[i]['score'].config(font=("Helvetica", 18))

            self.player_labels_dict[i]['name'].grid_configure(columnspan=5)

            # Fixed grid layout inside player frame (keeps everything on the left)
            frame.grid_columnconfigure(0, minsize=90)
            frame.grid_columnconfigure(1, minsize=24)
            frame.grid_columnconfigure(2, minsize=24)
            frame.grid_columnconfigure(3, minsize=24)

            setup_entry(score_entry, 2, 0, "0", pady=4, columnspan=5)

            button_texts = ["Bullseye", "20", "19", "18", "17", "16", "15"]
            
            #“Open” → A number is open when it’s still available to be hit (i.e., not yet closed by a player).
            #“Closed” → A number is closed once a player has hit it three times.
            #“Scoring” → A number becomes scoring (for you) if you’ve closed it but 
            #             your opponent hasn’t—so any extra hits score points.
            #“Dead” → A number is dead when both players have closed it, so it no longer matters.                      
            self.open_button_texts = button_texts
            self.closed_button_texts = []
            self.dead_button_texts = []

            self.player_buttons_dict[i] = {}
            self.player_buttons_dict[i]['buttons']= {}
            self.player_buttons_dict[i]['checkboxes']= {}

            for j, text in enumerate(button_texts):

                btn = Button(
                    frame,
                    text=text,
                    width=12,
                    pady=-60,
                    font=("Helvetica", 9),
                    bg=self.Button_bg_color,
                    fg=self.Button_ft_color,
                    state=DISABLED,                                      
                    activebackground=self.activeButton_bg_color,
                    activeforeground=self.activeButton_ft_color
                )

                btn.bind("<Button-1>", lambda e, t=text, p=i: self.writeCommitScore(number=t, player_id=p, event=e))

                # Button aligned to the right inside its column
                btn.grid(row=4 + j, column=0, pady=1, sticky=W, columnspan=2)                

                self.player_buttons_dict[i]['buttons'][text]= btn
                self.player_buttons_dict[i]['checkboxes'][text] = {}

                # 3 Cricket marks
                for k in range(3):
                    lbl = Label(
                        frame,
                        text=" ",
                        #text="✓",
                        width=2,
                        height=1,
                        font=("Helvetica", 10),
                        relief="solid",
                        bd=1,
                        bg=self.Button_bg_color2,
                        fg=self.checkbox_fg_color1
                    )

                    lbl.grid(
                        row=4 + j,
                        column=2 + k,
                        padx=8,
                        pady=1,
                        sticky=W
                    )

                    self.player_buttons_dict[i]['checkboxes'][text][str(k)]= lbl

    # ---------------------------------------------------------------------------------------------------------------
    # CREATING STATUS
    # ---------------------------------------------------------------------------------------------------------------
    self.StatusLabel = Label(self.emptylabel0, padx=1, pady=20, text="Ajoutez au moins un Joueur!",
                             font=("Helvetica", 12), bg=self.Button_bg_color,
                             fg="cyan")
    self.StatusLabel.grid(row=0, column=0)

    # ---------------------------------------------------------------------------------------------------------------
    # CREATING IMAGES (from .SGI files)
    # ---------------------------------------------------------------------------------------------------------------
    global logoImage

    logoImage = ImageTk.PhotoImage(Image.open("./data/images/dart_Logo2.sgi"))
    self.logoImage = Label(self.emptylabel_3, image=logoImage, bg=self.Button_bg_color, fg="grey")
    self.logoImage.grid(row=1, column=1, columnspan=3)

    # ---------------------------------------------------------------------------------------------------------------
    # SOFTWARE VERSION LABEL
    # ---------------------------------------------------------------------------------------------------------------
    self.softVersionLabel = Label(self.BackgroundFrame, padx=1, pady=1, text=self.softVersion,
                                  font=("Helvetica", "12", "italic"), bg=self.Button_bg_color,
                                  fg="black")

    self.softVersionLabel.grid(row=13, column=0, rowspan=2, sticky="SW")

    return

