import PySimpleGUI as sg


def janelasys():
    layoutsys = [
        [sg.Text("Cadastro de Produtos!")],
        [sg.Input(key="Nome"), sg.Text("Nome")],
        [sg.Input(key="Quant"), sg.Text("Quantidade")],
        [sg.Input(key="Preco"), sg.Text("Preço")],
        [sg.Button("Inserir Produto")],
        [sg.Listbox(values=[], size=(80, 23), key="lista", enable_events=True)],
        [sg.Button("Deslogar")],
        [sg.Button("Auto-Insert")],
    ]
    return sg.Window("System", layoutsys, size=(600, 620), location=(400, 50))

