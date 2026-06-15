import PySimpleGUI as sg
import os
from training_model_bonus import training_model
from create_image import create_image
from math_function import calculate_precision, calculate_mse, calculate_r2
from get_value import get_value

def display_gui():

    layout = [[sg.Text("Greetings from simple ft_linear_regression GUI\nFirst you should launch the training model right under")],
                [sg.Button("Launch Training Model")],
                [sg.Button("Display csv file")], 
                [sg.Button("Display linear function")], 
                [sg.Button("Show Precision")],
                [sg.Button("Display all")],
                [sg.Button("Simple Quit")],
                [sg.Button("Quit and Clean")]]

    window = sg.Window("Bonus_GUI", layout, margins=(500, 300))
    T0, T1 = get_value('output_bonus.txt')
    if T0 == 0 and T1 == 0:
        Training_done = False
    else:
        Training_done = True

    while True:

        event, values = window.read()
        

        if event == "Simple Quit" or event == sg.WIN_CLOSED:
            break

        if event == "Quit and Clean":
            files_to_remove = ['bonus_regression_all.png', 'bonus_regression_linearfunction.png', 'bonus_regression_scatter.png', 'output_bonus.txt']
            for file in files_to_remove:
                try:
                    os.remove(file)
                except FileNotFoundError:
                    continue
            break

        if event == "Launch Training Model":
            if training_model() == False:
                sg.popup_quick_message('Data.csv isnt present, cant launch the training module', auto_close_duration=3)
            else:
                Training_done = True
                create_image()
                sg.popup_quick_message('Training Complete!', auto_close_duration=2)

        if event == "Show Precision":
            if not Training_done:
                sg.popup_quick_message("Training hasnt been launch. Please launch it before doing anything else.", auto_close_duration=3)
            else:
                mse, rmse, r2 = calculate_precision()
                message = "This training model is: " + "{:.1f}".format(r2 * 100) + "% precise.\nOn average, your model's price predictions are off by about:" + "{:.2f}".format(rmse)
                sg.popup_quick_message(message, auto_close_duration=6)

        if event == "Display csv file":
            if not Training_done:
                sg.popup_quick_message("Training hasnt been launch. Please launch it before doing anything else.", auto_close_duration=3)
            else:
                layout_img = [[sg.Image(filename="bonus_regression_scatter.png")], [sg.Button("Close")]]
                win_img = sg.Window("Image", layout_img)

                while True:
                    event1, values1 = win_img.read()
                    if event1 == sg.WIN_CLOSED or event1 == "Close":
                        break
                win_img.close()


        if event == "Display linear function":
            if not Training_done:
                sg.popup_quick_message("Training hasnt been launch. Please launch it before doing anything else.", auto_close_duration=3)
            else:
                layout_img = [[sg.Image(filename="bonus_regression_linearfunction.png")], [sg.Button("Close")]]
                win_img = sg.Window("Image", layout_img)

                while True:
                    event1, values1 = win_img.read()
                    if event1 == sg.WIN_CLOSED or event1 == "Close":
                        break
                win_img.close()


        if event == "Display all":
            if not Training_done:
                sg.popup_quick_message("Training hasnt been launch. Please launch it before doing anything else.", auto_close_duration=3)
            else:
                layout_img = [[sg.Image(filename="bonus_regression_all.png")], [sg.Button("Close")]]
                win_img = sg.Window("Image", layout_img)

                while True:
                    event1, values1 = win_img.read()
                    if event1 == sg.WIN_CLOSED or event1 == "Close":
                        break
                win_img.close()