import PySimpleGUI as sg
import math


def createwindow():
    sg.theme("LightGreen4")
    sg.set_options(font = 'Calibri 20' , button_element_size = (3,1))
    button_size = (6, 1)
    enter_exit_size = (13, 1)
    layout = [[sg.Text("", font = 'Franklin 26', justification = 'center', expand_x = True, pad = (10, 20), key = '-TEXTO-')],
          [sg.Button('Limpiar', size = enter_exit_size), sg.Button("Enter", size = enter_exit_size)],
          [sg.Button(9, size = button_size), sg.Button(8, size = button_size),  sg.Button(7, size = button_size), sg.Button("x", size = button_size), sg.Button("sinf(x)", size = button_size),sg.Button("arsin(x)", size = button_size)], 
          [sg.Button(6, size = button_size), sg.Button(5, size = button_size), sg.Button(4, size = button_size), sg.Button("/", size = button_size), sg.Button("cosf(x)", size = button_size),sg.Button("arcos(x)", size = button_size)], 
          [sg.Button(3, size = button_size), sg.Button(2, size = button_size), sg.Button(1, size = button_size), sg.Button("-", size = button_size),  sg.Button("tanf(x)",size = button_size), sg.Button("artg(x)", size = button_size)],
          [sg.Button(".", size = button_size), sg.Button(0, size = button_size), sg.Button("+", size = button_size), sg.Button("=", size = button_size), sg.Button("Bint(x)", size = button_size),sg.Button("hexf(x)", size = button_size)]]

    
    #sg.theme("DarkPurple")
    return  sg.Window('Calculadora', layout)
window = createwindow()
current_value = []
operation = []

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    
    if event in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']:
        current_value.append(event)
        numtoString = ''.join(current_value)
        window['-TEXTO-'].update(numtoString)
        print(numtoString)
        
    if event in ['/', '-', '+']:
        print(event)
        operation.append( ''.join(current_value))
        current_value = []
        operation.append(event)
        window['-TEXTO-'].update('')
        
    if event in ['x']:
        operation.append( ''.join(current_value))
        current_value = []
        operation.append('*')
        window['-TEXTO-'].update('')
        
    if event == 'Enter' or event == '=':
        operation.append(''.join(current_value))
        result = eval(''.join(operation))
        current_value = []
        window['-TEXTO-'].update(result)
        operation = []
        current_value.append(str(result))
        
    if event == 'Limpiar':
        current_value = []
        operation = []
        window['-TEXTO-'].update('')
        
    if event == 'sinf(x)':
        sin = math.sin(int(numtoString))
        window['-TEXTO-'].update(sin)
        current_value = [str(sin)]
    
    if event == 'cosf(x)':
        cos = math.cos(int(numtoString))
        window['-TEXTO-'].update(cos)
        current_value = [str(cos)]
        
    if event == 'tanf(x)':
        tan = math.tan(int(numtoString))
        window['-TEXTO-'].update(tan)
        current_value = [str(tan)]
        
    if event == 'arsin(x)':
        try:
            arsin = math.asin(float(numtoString))
        except ValueError:
            try:
                arsin = math.asin(float("".join(current_value)))
            except ValueError:
                arsin ="error por exceso"
        window['-TEXTO-'].update(arsin)
        current_value = [str(arsin)]
        
    if event == 'arcos(x)':
        try:
            arcos = math.acos(float(numtoString))
        except ValueError:
            try:
                arcos = math.acos(float("".join(current_value)))
            except ValueError:
                arcos = "error por exceso"
        window['-TEXTO-'].update(arcos)
        current_value = [str(arcos)]
            
    if event == 'artg(x)':
        try:
            artg = math.atan(float(numtoString))
        except ValueError:
            try:
                artg = math.atan(float("".join(current_value)))
            except ValueError:
                artg = "error por exceso"
        window['-TEXTO-'].update(artg)
        current_value = [str(artg)]

    if event == "Bint(x)":
        try:
            binary = format(int(numtoString), 'b')
        except ValueError:
            binary = "Introduce un numero entero"
        window['-TEXTO-'].update(binary)
    
    if event == "hexf(x)":
        try:
            hexa = format(int(numtoString), 'X')
        except ValueError:
            gexa = "Introduce un numero entero"
        window['-TEXTO-'].update(hexa)
        
    if event == 'Memoria':
        print(sg.GetText('-TEXTO-'))
window.close()