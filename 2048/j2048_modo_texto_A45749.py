"""
=> Licenciatura Engenharia Informática e Miltimédia
    Disciplina:
    => Matemática Discreta e Programação
    Projecto:
    => 2048 Desenvolvido em aulas - Modo de Texto
    ALUNO:
    => Alberto Neto - A45749
"""

from j2048_motor_A45749 import novo_jogo
from j2048_motor_A45749 import pontuacao
from j2048_motor_A45749 import terminou
from j2048_motor_A45749 import valor
from j2048_motor_A45749 import esquerda
from j2048_motor_A45749 import direita
from j2048_motor_A45749 import acima
from j2048_motor_A45749 import abaixo

from j2048_gestor_A45749 import inicializa_semente
from j2048_gestor_A45749 import le_identificacao
from j2048_gestor_A45749 import regista_grelha_inicial
from j2048_gestor_A45749 import regista_jogada
from j2048_gestor_A45749 import regista_pontos
from j2048_gestor_A45749 import escreve_registo

print( "Jogo 2048 MDP Use as teclas WASD para jogar, use a tecla n para novo jogo e q para sair" )

def alinhar_direita(numero):
    numero_string = str( numero )
    while len( numero_string ) < 5:
        numero_string = " " + numero_string
    return numero_string


def print_jogo(jogo):
    # print("pontos=" + str(pontuacao(jogo)))
    print( jogo )
    for l in range( 1, 5 ):
        linha_string = " "
        for c in range( 1, 5 ):
            v = valor( jogo, l, c )
            linha_string = linha_string + alinhar_direita( v ) + " "
        print( linha_string )


le_identificacao()
semente = None
inicializa_semente( semente )

jogo = novo_jogo()

regista_grelha_inicial( valor( jogo, 1, 1 ), valor( jogo, 1, 2 ), valor( jogo, 1, 3 ), valor( jogo, 1, 4 ),
                        valor( jogo, 2, 1 ), valor( jogo, 2, 2 ), valor( jogo, 2, 3 ), valor( jogo, 2, 4 ),
                        valor( jogo, 3, 1 ), valor( jogo, 3, 2 ), valor( jogo, 3, 3 ), valor( jogo, 3, 4 ),
                        valor( jogo, 4, 1 ), valor( jogo, 4, 2 ), valor( jogo, 4, 3 ), valor( jogo, 4, 4 ) )

print_jogo( jogo )

tecla = None

while (tecla != "q") and (not terminou( jogo )):
    tecla = input()

    if tecla == 'n':
        jogo = novo_jogo()
    elif tecla == 'a':
        jogo = esquerda( jogo )
        regista_jogada( tecla )
    elif tecla == 'd':
        jogo = direita( jogo )
        regista_jogada( tecla )
    elif tecla == 'w':
        jogo = acima( jogo )
        regista_jogada( tecla )
    elif tecla == 's':
        jogo = abaixo( jogo )
        regista_jogada( tecla )

    print_jogo( jogo )

regista_pontos( pontuacao( jogo ) )
escreve_registo()
