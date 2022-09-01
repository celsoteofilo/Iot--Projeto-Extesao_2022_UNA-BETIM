

# ESTE E O CODIGO DA BUSSULA


direcao = 0

def on_forever():
    global direcao
    direcao = input.compass_heading()
    if direcao == 338 or direcao < 21:
        # Atribuimos uma variável direção, usando.
        basic.show_string("N")
    elif direcao == 22 or direcao < 67:
        basic.show_string("NE")
    elif direcao == 68 or direcao < 111:
        basic.show_string("L")
    elif direcao == 112 or direcao < 157:
        basic.show_string("SE")
    elif direcao == 158 or direcao < 202:
        basic.show_string("S")
    elif direcao == 203 or direcao < 247:
        basic.show_string("SO")
    else:
        basic.show_string("NO")
basic.forever(on_forever)

# ESTE E O CODIGO DO DETECTOR