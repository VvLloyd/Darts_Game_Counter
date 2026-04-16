"""Temporary method to store data; The variables are stored in "self" (i.e. mainApp).
Since all methods use the mainApp Object as an input/output, it is a lazy effective way to implement functionalities"""

def initializeGUIvar(mainApp):
    mainApp.softVersion = "ver 2.0.0"
    mainApp.colorTheme = "default"
    #mainApp.font = 'Consolas'
    mainApp.font = 'Fixedsys'
    # Visual Stuff. These are used in the Populate GUI methods:
    if mainApp.colorTheme == "default":
        mainApp.Button_bg_color = "#21453A"
        mainApp.Button_game_start_ft_color = "#2BFB44"
        mainApp.Button_ft_color = "#D3DBE5"
        mainApp.Button_status_ft_color = "#1AC9F1"
        mainApp.activeButton_bg_color = "#9aa794"
        mainApp.activeButton_ft_color = "#D3DBE5"
        mainApp.disabledButton_ft_color = "#D3DBE5"
        mainApp.disabledButton_bg_color = "#21453A"
        mainApp.currentplayer_color = "#CAB812"

        mainApp.modeButton_bg_color = "#21453A"
        mainApp.modeButton_ft_color = "#D3DBE5"
        mainApp.modeButtonDisable_bg_color = "#21453A"
        mainApp.modeButtonDisable_ft_color = "#D3DBE5"

        mainApp.checkbox_fg_color1 = "#CAB812"
        mainApp.checkbox_fg_color2 = "#59FF62"
        mainApp.Button_bg_color2 = "#1E332D"

        mainApp.team_1_color = "#129FE1"
        mainApp.team_2_color = "#DC8E0F"

        mainApp.textured_path = "./data/images/retro_pattern_default.png"

    if mainApp.colorTheme == "Dark":
        mainApp.Button_bg_color = "#282828"
        mainApp.Button_game_start_ft_color = "#2BFB44"
        mainApp.Button_ft_color = "#D1D2D3"
        mainApp.Button_status_ft_color = "#1AC9F1"
        mainApp.activeButton_bg_color = "#a9a9a9"
        mainApp.activeButton_ft_color = "#D3DBE5"
        mainApp.disabledButton_ft_color = "#D3DBE5"
        mainApp.disabledButton_bg_color = "#262626"
        mainApp.currentplayer_color = "#CAB812"

        mainApp.modeButton_bg_color = "#282828"
        mainApp.modeButton_ft_color = "#D1D2D3"
        mainApp.modeButtonDisable_bg_color = "#333333"
        mainApp.modeButtonDisable_ft_color = "#D3DBE5"

        mainApp.checkbox_fg_color1 = "#CAB812"
        mainApp.checkbox_fg_color2 = "#59FF62"
        mainApp.Button_bg_color2 = "#161616"

        mainApp.team_1_color = "#129FE1"
        mainApp.team_2_color = "#DC8E0F"

        mainApp.textured_path = "./data/images/retro_pattern.png"

    # Variables  
    mainApp.p1_DoubleInVar = False
    mainApp.p2_DoubleInVar = False
    mainApp.p3_DoubleInVar = False
    mainApp.p4_DoubleInVar = False

    mainApp.quitbuttonPressed = False

    return
