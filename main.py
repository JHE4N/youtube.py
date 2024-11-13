import PySimpleGUI as sg
from music_download import music_download

def getLinks(str):
    urls_list = str.split('\n')

    for url in urls_list:
        print(url)
        music_download(url)


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
    print('Todos os links foram baixados')
    window.close()

window.close()
