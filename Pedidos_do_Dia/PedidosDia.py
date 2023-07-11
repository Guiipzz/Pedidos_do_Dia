import setup as s
import os

continua = "S"
while continua == "S":
    resposta = s.menu()
    if resposta == "N":
        s.respostaN()
        os.startfile('PedidosDia.txt')

    elif resposta == "C":
        s.respostaC()
        os.startfile('PedidosDia.txt')

    elif resposta == "F":
        s.finalizar()
        print('Dia finalizado com sucesso. Bom descanso!!')
        continua = "N"

    elif resposta == "B":
        pedidoB = input("Número do pedido: ")
        resultado = s.respostaB(pedidoB)
        print(f'Esse pedido é mencionado nos seguintes blocos:\n{resultado}')
