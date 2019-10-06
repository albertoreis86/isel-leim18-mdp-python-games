"""
=> Licenciatura Engenharia Informática e Miltimédia
    Disciplina:
    => Matemática Discreta e Programação
    Projecto:
    => 2048 Desenvolvido em aulas - Gestor ranking
    ALUNO:
    => Alberto Neto - A45749
"""

from random import randint
from random import seed
from urllib import request

numero = None
amigos = None
grelha = None
jogadas = None
pontos = None
semente = None

def inicializa_semente(semente_a_usar):
    global semente

    if semente_a_usar == None:
        semente_a_usar = randint(1, 1000)

    seed(semente_a_usar)

    semente = semente_a_usar

def le_identificacao():
    global numero
    global amigos

    nome = "identificacao.txt"
    modo = "r"

    ficheiro = open(nome, modo)

    linha1 = ficheiro.readline()
    linha2 = ficheiro.readline()

    ficheiro.close()

    numero = linha1[7:-1]
    amigos = linha2[7:-1]

    print('"' + numero + '"')
    print('"' + amigos + '"')


def regista_grelha_inicial(g11, g12, g13, g14,
                           g21, g22, g23, g24,
                           g31, g32, g33, g34,
                           g41, g42, g43, g44):

    global grelha
    global jogadas
    global pontos

    grelha = [[g11, g12, g13, g14],
              [g21, g22, g23, g24],
              [g31, g32, g33, g34],
              [g41, g42, g43, g44]]
    jogadas = ''
    pontos = None

def regista_jogada(letra):
    global jogadas

    jogadas = jogadas + letra

def regista_pontos(p):
    global pontos

    pontos = p

def regista_ranking():
    mensagem = None
    try:
        url_string = "http://ec2-54-76-249-109.eu-west-1.compute.amazonaws.com/cgi-bin/submit_2048.py?numero=" + numero + "&amigos=" + amigos + "&jogadas=" + jogadas + "&pontos=" + str(pontos) + "&semente=" + str(semente)
        url = request.urlopen(url_string)
        mensagem = url.read().decode("utf-8")
    except Exception as err:
        mensagem = "Não foi possível registar a pontuação no ranking.\n"
        mensagem = mensagem + str(err)

    return mensagem

def escreve_registo():
    nome = numero + '.' + str(pontos)
    modo = 'w'

    ficheiro = open(nome, modo)

    ficheiro.write("numero=" + numero + '\n')
    ficheiro.write("amigos=" + amigos + '\n')
    ficheiro.write("grelha_inicial=" + str(grelha) + '\n')
    ficheiro.write("jogadas=" + jogadas + '\n')
    ficheiro.write("pontos=" + str(pontos) + '\n')
    ficheiro.write("semente=" + str(semente) + '\n')

    ficheiro.close()

    mensagem_cloud = regista_ranking()

    return mensagem_cloud