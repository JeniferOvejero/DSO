import PySimpleGUI as sg

sg.theme('Material1')
layout = [
    [sg.Text('Incluir novo cliente')],
    [sg.Text('Nome', size=(15,1)), sg.InputText('nome', key= "k_nome")],
    [sg.Text('Endereço', size=(15,1)), sg.InputText('endereço', key="k_endereco")],
    [sg.Submit(), sg.Cancel()]
]
#sg.theme_previewer()
window = sg.Window('Cadastro de clientes').layout(layout)

button, values = window.read()

print(button, values)