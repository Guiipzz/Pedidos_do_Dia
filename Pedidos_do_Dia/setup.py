import os.path
import shutil
import glob
from datetime import date

hoje = date.today().strftime('%d.%m.%Y')


def menu():
    print('===============MENU===============\n'
          'N • Começar um novo arquivo\n'
          'C • Continuar com o arquivo do dia\n'
          'F • Finalizar o dia\n'
          'B • Buscar pedido')
    resposta = input('O que deseja fazer? ').upper()
    return resposta


def respostaN():
    nomeLote = input("Nome do lote: ")
    pedidosDia = open('PedidosDia.txt', 'w')
    tray, nfs = lerPedidos()
    texto(tray, nfs, pedidosDia, nomeLote)


def lerPedidos():
    tray = input('Digite os números dos pedidos na Tray.\n')
    nfs = input('Agora digite os pedidos que precisam de nota fiscal.\n')
    return tray, nfs


def respostaC():
    nomeLote = input("Nome do lote: ")
    pedidosDia = open('PedidosDia.txt', 'a')
    pedidosDia.write('\n\n')
    tray, nfs = lerPedidos()
    texto(tray, nfs, pedidosDia, nomeLote)


def respostaB(pedidoB):
    caminho = glob.glob('Logs/*.txt')
    resultado = []
    for arquivo in caminho:
        with open(arquivo, 'r') as f:
            conteudo = f.read()
            if pedidoB in conteudo:
                nomeArquivo = os.path.basename(arquivo)
                resultado.append(nomeArquivo)
    return resultado


def listas(tray, nfs):
    listaTray = tray.split(',')
    listaNfs = nfs.split(',')
    return listaTray, listaNfs


def replace(tray, nfs):
    trayBling = tray.replace(',', ';')
    nfsBling = nfs.replace(',', ';')
    return trayBling, nfsBling


def texto(tray, nfs, pedidosDia, nomeLote):
    trayBling, nfsBling = replace(tray, nfs)
    if nfsBling == "":
        textoNf = ""
    else:
        textoNf = f'\n\nPara Gerar NFs:\n{nfsBling}'
    textoFinal = f'{nomeLote.upper()} ===========================================\n' \
                 f'Na Tray:\n' \
                 f'{tray}\n\n' \
                 f'Na Bling:\n' \
                 f'{trayBling}' \
                 f'{textoNf}'

    pedidosDia.write(textoFinal)
    pedidosDia.close()


def finalizar():
    caminho_original = 'PedidosDia.txt'
    caminho_destino = f'Logs/{hoje}.txt'
    shutil.copy(caminho_original, caminho_destino)
