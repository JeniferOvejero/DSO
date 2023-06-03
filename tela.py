import PySimpleGUI as sg


class ExemploView:

    def __init__(self):
        self.__window = None
        self.init_components()

    def init_components(self):
        layout = [
        [sg.Text('Incluir novo cliente')],
        [sg.Text('Nome', size=(15,1)), sg.InputText('nome', key= "k_nome")],
        [sg.Text('Endereço', size=(15,1)), sg.InputText('endereço', key="k_endereco")],
        [sg.Submit(), sg.Cancel()]
        ]
        self.__window = sg.Window('Titulo da tela', default_element_size=(40,1)).layout(layout)

    def open(self):
        button, values = self.__window.read()
        return button, values

    def close(self):
        self.__window.close()

    def show_message(self, titulo: str, mensagem: str):
        sg.popup(titulo, mensagem)

tela = ExemploView()
tela.open()
