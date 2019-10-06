"""
=> Licenciatura Engenharia Informática e Miltimédia
    Disciplina:
    => Matemática Discreta e Programação
    Projecto:
    => 2048 Desenvolvido em aulas - Motor de jogo
    ALUNO:
    => Alberto Neto - A45749
"""

from random import random
from random import choice


def get_2ou4():
    if random() > 0.1:
        return 2
    else:
        return 4


def get_posicoes_vazias(grelha):
    posicoes_vazias = []

    for ilinha in range( 4 ):
        for icoluna in range( 4 ):
            if grelha[ilinha][icoluna] == 0:
                posicoes_vazias.append( [ilinha, icoluna] )

    return posicoes_vazias


def inserir_2ou4(grelha, numero):
    posicoes_vazias = get_posicoes_vazias( grelha )
    posicao_vazia = choice( posicoes_vazias )

    ilinha = posicao_vazia[0]
    icoluna = posicao_vazia[1]
    grelha[ilinha][icoluna] = numero


def novo_jogo():
    grelha = [[0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0]]
    fim = False
    vitoria = False
    pontos = 0

    inserir_2ou4( grelha, get_2ou4() )
    inserir_2ou4( grelha, get_2ou4() )

    jogo = (grelha, fim, vitoria, pontos)

    return jogo


def move_esquerda(linha):
    nova_linha = []

    for numero in linha:
        if numero != 0:
            nova_linha.append( numero )

    acrescenta_zeros( nova_linha )

    return nova_linha


def acrescenta_zeros(linha):
    while len( linha ) < 4:
        linha.append( 0 )


def somar_esquerda(linha):
    nova_linha = []

    pontos = 0

    indice = 0

    while indice < 4 - 1:
        if linha[indice] == linha[indice + 1]:
            soma = linha[indice] + linha[indice]
            pontos = pontos + soma
            nova_linha.append( soma )
            indice = indice + 2
        else:
            nova_linha.append( linha[indice] )
            indice = indice + 1

    if indice == 3:
        nova_linha.append( linha[indice] )

    acrescenta_zeros( nova_linha )

    return (nova_linha, pontos)


def atualizar_grelha(grelha, nova_grelha):
    inserir = False
    for il in range( 4 ):
        for ic in range( 4 ):
            if grelha[il][ic] != nova_grelha[il][ic]:
                inserir = True

    if inserir:
        inserir_2ou4( nova_grelha, get_2ou4() )


def get_vitoria(grelha):
    vitoria = False
    for linha in grelha:
        for numero in linha:
            if numero == 2048:
                vitoria = True

    return vitoria


def ha_iguais_adjacentes(grelha):
    ha = False

    for il in range( 4 ):
        for ic in range( 4 - 1 ):
            if grelha[il][ic] == grelha[il][ic + 1]:
                ha = True

    for il in range( 4 - 1 ):
        for ic in range( 4 ):
            if grelha[il][ic] == grelha[il + 1][ic]:
                ha = True

    return ha


def get_fim(grelha):
    if len( get_posicoes_vazias( grelha ) ) == 0 \
            and (not ha_iguais_adjacentes( grelha )):
        return True
    else:
        return False


def esquerda(jogo):
    "Operação esquerda"

    grelha = jogo[0]
    fim = jogo[1]
    vitoria = jogo[2]
    pontos = jogo[3]

    nova_grelha = []
    for linha in jogo[0]:
        nova_linha = move_esquerda( linha )
        (nova_linha2, pontos_a_somar) = somar_esquerda( nova_linha )
        nova_grelha.append( nova_linha2 )
        pontos = pontos + pontos_a_somar

    atualizar_grelha( grelha, nova_grelha )

    if vitoria == False:
        vitoria = get_vitoria( nova_grelha )

    fim = get_fim( nova_grelha )

    novo_jogo = (nova_grelha, fim, vitoria, pontos)

    return novo_jogo


def reverter_lista(uma_lista):
    nova_lista = []

    indice = len( uma_lista ) - 1

    while indice >= 0:
        nova_lista.append( uma_lista[indice] )
        indice = indice - 1

    return nova_lista


def reverter_grelha(grelha):
    grelha_revertida = []

    for linha in grelha:
        grelha_revertida.append( reverter_lista( linha ) )

    return grelha_revertida


def direita(jogo):
    "Operação direita"

    grelha = jogo[0]
    fim = jogo[1]
    vitoria = jogo[2]
    pontos = jogo[3]

    grelha_revertida = reverter_grelha( grelha )

    jogo_revertido = (grelha_revertida, fim, vitoria, pontos)
    novo_jogo_revertido = esquerda( jogo_revertido )

    nova_grelha_revertida = novo_jogo_revertido[0]
    novo_fim = novo_jogo_revertido[1]
    nova_vitoria = novo_jogo_revertido[2]
    novos_pontos = novo_jogo_revertido[3]

    nova_grelha = reverter_grelha( nova_grelha_revertida )

    novo_jogo = (nova_grelha, novo_fim, nova_vitoria, novos_pontos)

    return novo_jogo


def transpor(matriz):
    nova_matriz = []

    n_linhas_matriz = len( matriz )
    n_colunas_matriz = len( matriz[0] )

    n_linhas_nova_matriz = n_linhas_matriz
    n_colunas_nova_matriz = n_colunas_matriz

    for il in range( n_linhas_nova_matriz ):
        nova_linha = []
        for ic in range( n_colunas_nova_matriz ):
            nova_linha.append( None )
        nova_matriz.append( nova_linha )

    for il in range( n_linhas_nova_matriz ):
        for ic in range( n_colunas_nova_matriz ):
            nova_matriz[il][ic] = matriz[ic][il]

    return nova_matriz


def acima(jogo):
    "Operação acima"

    grelha = jogo[0]
    fim = jogo[1]
    vitoria = jogo[2]
    pontos = jogo[3]

    grelha_transposta = transpor( grelha )

    jogo_transposto = (grelha_transposta, fim, vitoria, pontos)
    novo_jogo_transposto = esquerda( jogo_transposto )

    nova_grelha_transposta = novo_jogo_transposto[0]
    novo_fim = novo_jogo_transposto[1]
    nova_vitoria = novo_jogo_transposto[2]
    novos_pontos = novo_jogo_transposto[3]

    nova_grelha = transpor( nova_grelha_transposta )

    novo_jogo = (nova_grelha, novo_fim, nova_vitoria, novos_pontos)

    return novo_jogo


def abaixo(jogo):
    "Operação abaixo"

    grelha = jogo[0]
    fim = jogo[1]
    vitoria = jogo[2]
    pontos = jogo[3]

    grelha_transposta = transpor( grelha )

    jogo_transposto = (grelha_transposta, fim, vitoria, pontos)
    novo_jogo_transposto = direita( jogo_transposto )

    nova_grelha_transposta = novo_jogo_transposto[0]
    novo_fim = novo_jogo_transposto[1]
    nova_vitoria = novo_jogo_transposto[2]
    novos_pontos = novo_jogo_transposto[3]

    nova_grelha = transpor( nova_grelha_transposta )

    novo_jogo = (nova_grelha, novo_fim, nova_vitoria, novos_pontos)

    return novo_jogo


def valor(jogo, linha, coluna):
    "Operação grelha"

    grelha = jogo[0]

    return grelha[linha - 1][coluna - 1]


def terminou(jogo):
    "Operação fim"

    fim = jogo[1]

    return fim


def ganhou_ou_perdeu(jogo):
    "Operação ganhou/perdeu"

    vitoria = jogo[2]

    return vitoria


def pontuacao(jogo):
    "Operação pontos"

    pontos = jogo[3]

    return pontos
