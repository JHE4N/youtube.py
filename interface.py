import PySimpleGUI as sg

def getLinks(str):
    links_list = str.split('\n')

    for link in links_list:
        print(link)
        
        #chamar a pytube




layout = [
    [sg.Multiline(default_text='Link1\nLink2\nLink3', size=(80, 20), font='_ 14')],
    [sg.Button('Baixar'), sg.Button('Cancelar')],
    ]


window = sg.Window('Music Downloader Py', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancelar':
        break
    #print('Eventoo ', values)
    getLinks(values[0])

window.close()
