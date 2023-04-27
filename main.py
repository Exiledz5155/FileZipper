import PySimpleGUI as sg
from zip_creator import make_archive

label1 = sg.Text("Select files to compress:")
input1 = sg.Input()
choose_button1 = sg.FilesBrowse("Choose", key="files") # naming the output for ease of use

label2 = sg.Text("Select destination folder:")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose", key="folder") # Note difference between files and folder

compress_button = sg.Button("Compress")
output_label = sg.Text(key="output") # left empty in order to update once compression completes

window = sg.Window("File Compressor",
                   layout=[[label1, input1, choose_button1],
                           [label2, input2, choose_button2],
                           [compress_button, output_label]])

while True:
    event, values = window.read()
    print(event, values)
    filepaths = values["files"].split(";") # each file seperated by ;
    folder = values["folder"]
    make_archive(filepaths, folder)
    window["output"].update(value="Compression completed!") # Update text for completion

window.close()