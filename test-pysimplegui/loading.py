import PySimpleGUI as sg

image_source = 'Spinner.gif'

for i in range(1,10000):
    sg.popup_animated(
        image_source, # message = None,
        no_titlebar = True,
        keep_on_top = True, # location = (None, None), # alpha_channel = None, # time_between_frames = 0, # transparent_color = None,
        title = 'Loading', # icon = None
    )
