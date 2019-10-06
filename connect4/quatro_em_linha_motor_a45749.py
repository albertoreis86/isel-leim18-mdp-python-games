"""
=> Licenciatura Engenharia Informática e Miltimédia
    Disciplina:
    => Matemática Discreta e Programação
    Projecto:
    => Jogo Quatro em Linha
    ALUNO:
    => Alberto Neto - A45749
"""

LINHAS = 6  # Numero de linhas da grelha de jogo
COLUNAS = 7  # Numero de colunas da grelha de jogo
JOGADORUM = 1  # Número que representa o Jogador 2
JOGADORDOIS = 2  # Número que representa o Jogador 1


# enunciado
def novo_jogo():
    """""
    => função que inicia um novo jogo com valores "zerados"
    """
    grelha = [[0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0]]
    fim = False
    vencedor = None
    jogador = JOGADORUM
    linha_vitoria = None
    jogo = (grelha, fim, vencedor, jogador, linha_vitoria)
    return jogo


# enunciado
def jogar(jogo, coluna):
    """""
    => função que permite jogar:
        jogo com a posição jogada;
        valor de fim (T/F)
        vencedor (1 / 2 / None se empate)
        jogador do turno (1/2)
        lista com as coordenadas das peças que venceram o jogo
    se houver 4 em linha o jogo termina e o vencedor é o jogador do turno que chamou a função.
    verifica se há empate (caso não exista 4 em linha e não existam espaços vazios)
    retorna o jogo atualizado para o turno seguinte
    """
    grelha = jogo[0]
    fim = jogo[1]
    vencedor = jogo[2]
    jogador = jogo[3]
    linha_vitoria = jogo[4]
    largarpeca(jogo, coluna)
    _4emlinha = quatroemlinha(grelha, jogador)
    if _4emlinha[0] is True:
        fim = True
        linha_vitoria = _4emlinha[1]
        vencedor = jogador
    elif verificaempate(jogo) is True:
        vencedor = None
        fim = True
    jogador = turno(jogo)
    jogo = (grelha, fim, vencedor, jogador, linha_vitoria)
    return jogo

# enunciado


def ha_espaco(jogo, coluna):
    """""
    => Funcao que verifica se existem espaços vazios na "ultima linha da grelha", no caso é a de primeiro indice (0)
    enquanto houver um 0 em alguma coluna da linha de indice 0 então há espaço para se jogar.
    recebe o valor da coluna atraves da parte gráfica pelo que necessita de diminuir um valor ao indice.
    """
    coluna -= 1
    grelha = jogo[0]
    if grelha[0][coluna] == 0:
        return True
    else:
        return False


def largarpeca(jogo, coluna):
    """""
    => Funcao que faz com que uma peça seja introduzida na posição pretendida pelo jogador
    """
    grelha = jogo[0]
    fim = jogo[1]
    vencedor = jogo[2]
    jogador = jogo[3]
    linha_vitoria = jogo[4]
    coluna -= 1
    for l in reversed(range(LINHAS)):
        if grelha[l][coluna] == 0:
            grelha[l][coluna] = jogador
            return jogo


def quatroemlinha(grelha, jogador):
    """""
    => Funcao que permite verificar as quatro possibilidaddes de vitória de jogo:
        Retorna um Valor Verdadeiro caso haja vitória e uma lista com as posições das peças vencedoras
        Se não houver vitória retorna um valor Falso e uma lista vazia

    => Variável local limitevitoria - como a função verifica a peça jogada e otras 3 peças em indices superiores
    (com excessão da verificação na diagonal contrária "\" que subtrai um índice)
    apenas é necessário iterar atè ao limite de linhas e colunas - 3
    pois entre os 3 ultimos indíces só restam 3 peças sendo impossivel obter a vitória nesse cenário.
    => Iteração: colunas entre 0-3 e linhas entre 0-2
    => vitoriagrafica vs. vitoriaindice0 - diferente do motor, os índices no modo gráfico começam por 1
        daí a criação de duas listas diferentes, para compararar a vitória com índices "real" com a
        representação gráfica da vitória
    """
    limitevitoria = 3
    # Verifica vitória Horizontal
    for c in range(COLUNAS - limitevitoria):
        for l in range(LINHAS):
            vitoriagrafica = []
            quatro_em_linha = False
            # vitoriaindice0 = []
            if grelha[l][c] == jogador:
                vitoriagrafica.append([l + 1, c + 1])
                # vitoriaindice0.append( [l, c] )
                if grelha[l][c + 1] == jogador:
                    vitoriagrafica.append([l + 1, c + 2])
                    # vitoriaindice0.append( [l, c + 1] )
                    if grelha[l][c + 2] == jogador:
                        vitoriagrafica.append([l + 1, c + 3])
                        # vitoriaindice0.append( [l, c + 2] )
                        if grelha[l][c + 3] == jogador:
                            vitoriagrafica.append([l + 1, c + 4])
                            # vitoriaindice0.append( [l, c + 3] )
                            quatro_em_linha = True
                            # print( "Vitória Motor: " + str(vitoriaindice0) )
                            # print( "Vitória modo Gráfico: " + str(vitoriagrafica)  )

            if quatro_em_linha is True:
                return True, vitoriagrafica

    # Vertical
    for c in range(COLUNAS):
        for l in range(LINHAS - limitevitoria):
            vitoriagrafica = []
            quatro_em_linha = False
            # vitoriaindice0 = []
            if grelha[l][c] == jogador:
                vitoriagrafica.append([l + 1, c + 1])
                # vitoriaindice0.append( [l, c] )
                if grelha[l + 1][c] == jogador:
                    vitoriagrafica.append([l + 2, c + 1])
                    # vitoriaindice0.append( [l + 1, c] )
                    if grelha[l + 2][c] == jogador:
                        vitoriagrafica.append([l + 3, c + 1])
                        # vitoriaindice0.append( [l + 2, c] )
                        if grelha[l + 3][c] == jogador:
                            vitoriagrafica.append([l + 4, c + 1])
                            # vitoriaindice0.append( [l + 3, c] )
                            quatro_em_linha = True
                            # print( "Vitória Motor: " + str( vitoriaindice0 ) )
                            # print( "Vitória modo Gráfico: " + str( vitoriagrafica ) )
            if quatro_em_linha is True:
                return True, vitoriagrafica
    # Diagonal \
    for c in range(COLUNAS - limitevitoria):
        for l in range(LINHAS - limitevitoria):
            vitoriagrafica = []
            quatro_em_linha = False
            # vitoriaindice0 = []
            if grelha[l][c] == jogador:
                vitoriagrafica.append([l + 1, c + 1])
                # vitoriaindice0.append( [l, c] )
                if grelha[l + 1][c + 1] == jogador:
                    vitoriagrafica.append([l + 2, c + 2])
                    # vitoriaindice0.append( [l + 1, c + 1] )
                    if grelha[l + 2][c + 2] == jogador:
                        vitoriagrafica.append([l + 3, c + 3])
                        # vitoriaindice0.append( [l + 2, c + 2] )
                        if grelha[l + 3][c + 3] == jogador:
                            vitoriagrafica.append([l + 4, c + 4])
                            # vitoriaindice0.append( [l + 3, c + 3] )
                            quatro_em_linha = True
                            # print( "Vitória Motor: " + str( vitoriaindice0 ) )
                            # print( "Vitória modo Gráfico: " + str( vitoriagrafica ) )
            if quatro_em_linha is True:
                return True, vitoriagrafica
    # Diagonal  /
    for c in range(COLUNAS - limitevitoria):
        for l in range(3, LINHAS):
            vitoriagrafica = []
            quatro_em_linha = False
            # vitoriaindice0 = []
            if grelha[l][c] == jogador:
                vitoriagrafica.append([l + 1, c + 1])
                # vitoriaindice0.append( [l, c] )
                if grelha[l - 1][c + 1] == jogador:
                    vitoriagrafica.append([l, c + 2])
                    # vitoriaindice0.append( [l - 1, c + 1] )
                    if grelha[l - 2][c + 2] == jogador:
                        vitoriagrafica.append([l - 1, c + 3])
                        # vitoriaindice0.append( [l - 2, c + 2] )
                        if grelha[l - 3][c + 3] == jogador:
                            vitoriagrafica.append([l - 2, c + 4])
                            # vitoriaindice0.append( [l - 3, c + 3] )
                            quatro_em_linha = True
                            # print( "Vitória Motor: " + str( vitoriaindice0 ) )
                            # print( "Vitória modo Gráfico: " + str( vitoriagrafica ) )
            if quatro_em_linha is True:
                return True, vitoriagrafica
    return False, []


def verificaempate(jogo):
    """""
    => Funcao verifica se ainda existem espaços a jogar e se não há vencedor, caso não existam espaços nem vencedor,
        retorna True.
    (o vencedor tem que ser None já que o 4emlinha pode ser alcançado ao colocar a peça na última posição disponível)
    """
    grelha = jogo[0]
    vencedor = jogo[2]
    if grelha[0][0] != 0 and grelha[0][1] != 0 and grelha[0][2] != 0 and grelha[0][3] != 0 and grelha[0][4] != 0 and \
            grelha[0][5] != 0 and grelha[0][6] != 0 and vencedor is None:
        return True


def turno(jogo):
    """""
    => Função que alera a vez de cada jogador, recebe o como argumento jogo "jogado"
    """""
    jogador = jogo[3]
    if jogador == JOGADORUM:
        jogador = JOGADORDOIS
    else:
        jogador = JOGADORUM
    return jogador


# enunciado
def valor(jogo, linha, coluna):
    """""
    => Função que permite obter o valor de cada peça, se é uma peça do Jogador 1 ou do Jogador 2
        Necessita que as linhas e as colunas sejam indexadas com um valor a menos pois a
        parte grafica recebe valores a partir do indice 1

    # Erro na construção da matriz de jogo se não fizer linha-1 e coluna-1
    """
    linha -= 1
    coluna -= 1
    grelha = jogo[0]
    return grelha[linha][coluna]

# enunciado


def terminou(jogo):
    """""
    => Retorna o fim do jogo
    """
    return jogo[1]


# enunciado
def quem_ganhou(jogo):
    """""
    => Retorna o vencedor, JOGADRUM, JOGADORDOIS ou, em caso de empate, None
     """
    return jogo[2]


# enunciado
def get_linha_vitoria(jogo):
    """""
    => Retorna a lista com as coordenadas das quatro peças que ditam a vitória
    """
    return jogo[4]
