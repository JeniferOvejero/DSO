import PySimpleGUI as sg
from PySimpleGUI import (
    Window, Button, Text, Image, Input,
    Column, VSeparator, Push
)
sg.ChangeLookAndFeel('lightblue')
layout_esquerda= [
    [Image(filename='icon.png')]
]
layout_direita =[
    [Text('Dia:'), Push(), Input()],
    [Text('Mês:'), Push(), Input()],
    [Text('Título:'), Push(), Input()],
    [Text('Descrição:'), Push(), Input()],
    [Button('Criar'), Push(), sg.Cancel()]
]
layout= [
    [Column(layout_esquerda),
    VSeparator(),
    Column(layout_direita)]
]

window = Window(
    'Oniverso',
    layout=layout,

)
print(window.read())
window.close()