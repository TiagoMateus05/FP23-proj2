     ######################
    ##                  ##
   ##    Projeto 2     ##
  ##   Tiago Mateus   ##
 ##                  ##
######################

#2.1.1 - TAD interseção#
########################
def cria_intersecao(col, lin):
    """cria intersecao: str x int → intersecao
    Cria intersecao pelos argumentos recebidos

    Args:
        col ([str]): [string de A a Z]
        lin ([int]): [inteiro de 1 a 99]

    Raises:
        ValueError: [caso nao seja str de A a Z e inteiro de 1 a 99]

    Returns:
        [tuple]: [tuplo de interseção]
    """    
    #Confirma os argumentos introduzidos
    if not type(col) == str or len(col) != 1 or not ('A' <= col <= 'Z') \
        or not type(lin) == int or not (0 < lin <= 99):
        raise ValueError('cria_intersecao: argumentos invalidos')  
    #Retoma tuplo de interseção
    return (col, lin)

def obtem_col(i):
    """obtem col: intersecao → str
    Dá o valor em str da coluna de i

    Args:
        i ([tuple]): [interseção]

    Returns:
        [str]: [Letra da interseção]
    """    
    return i[0]

def obtem_lin(i):
    """obtem lin: intersecao → int
    Dá o valor em int da linha de i

    Args:
        i ([tuple]): [interseção]

    Returns:
        [int]: [Numero da interseção]
    """    
    return i[1]

def eh_intersecao(arg):
    """eh intersecao: universal → booleano
    Confirma argumento arg se é interseção

    Args:
        arg ([tuple]): [interseção]

    Returns:
        [bool]: [True or False, True se for interseção]
    """    
    #Comfirma possibilidade de que o argumento possa não ser interseção e indica
    #False caso quebre esses argumentos, tais como nao ser entre A a Z e 
    #de 1 a 99
    if not isinstance(arg, tuple) or len(arg) != 2 or not \
        isinstance(obtem_col(arg), str) or len(obtem_col(arg)) != 1 \
            or not 'A' <= obtem_col(arg) <= 'Z' or not type(obtem_lin(arg)) \
                == int or not 0 < obtem_lin(arg) <= 99:
        return False 
    #Toma True caso sejam verdadeiros
    return True 

def intersecoes_iguais(i1, i2):
    """intersecoes iguais: universal x universal → booleano
    Comfirma se os argumentos i1 e i2 são iguais
    Args:
        i1 ([tuple]): [interseção i1]
        i2 ([tuple]): [interseção i2]

    Returns:
        [bool]: [True or False caso se confirmem]
    """    
    #verifica se são interseções e se são iguais
    return eh_intersecao(i1) and eh_intersecao(i2) and i1 == i2 

def intersecao_para_str(i):
    """intersecao para str: intersecao → str

    Args:
        i ([tuple]): [interseção em tuplo]

    Returns:
        [str]: [interseção em str do tipo 'A1']
    """    
    #retoma interceção como str do tipo 'A1'
    return f"{obtem_col(i)}{obtem_lin(i)}"

def str_para_intersecao(i):
    """str para intersecao: str → intersecao

    Args:
        i ([str]): [interseção em str do tipo 'A1']

    Returns:
        [tuple]: [interseção em tuplo]
    """    
    #Retoma uma interseção em tuplo a partir dos argumentos da string
    return cria_intersecao(i[0],int(i[1:]))

#Alto Nivel#

def obtem_intersecoes_adjacentes(i, l):
    """obtem intersecoes adjacentes: intersecao x intersecao → tuplo
    Obtem as interseções adjacentes a uma interceção juntamente com o goban

    Args:
        i ([tuple]): [interceção]
        l ([list]): [goban]

    Returns:
        [tuple]: [conjunto das adjacentes]
    """    
    #Vê o tamanho horizontal máximo do tabuleiro
    tamanho_horizontal = (obtem_lin(l))
    tamanho_vertical = obtem_lin(l) #Vê o tamanho vertical máximo do tabuleiro

    adjacentes = ()
    #Baixo
    if 1 < obtem_lin(i):
        adjacentes += (cria_intersecao(obtem_col(i), obtem_lin(i) - 1), )

    #Esquerda
    if 1 < (ord(obtem_col(i)) - 64):
        adjacentes += (cria_intersecao(chr(ord(obtem_col(i))-1), obtem_lin(i)),)
    
    #Direita
    if (ord(obtem_col(i)) - 64) < tamanho_horizontal:
        adjacentes += (cria_intersecao(chr(ord(obtem_col(i)) + 1), \
                                       obtem_lin(i)), )

    #Cima
    if obtem_lin(i) < tamanho_vertical:
        adjacentes += (cria_intersecao(obtem_col(i), obtem_lin(i) + 1), )

    return adjacentes

def ordena_intersecoes(t):
    """ordena intersecoes: tuplo → tuplo
    Ordena o conjunto de intersecoes de t

    Args:
        t ([list]): [lista com interseções]

    Returns:
        [tuple]: [tuplo com interseções ordenados]
    """    
    ordem_leitura = sorted(list(t), key= lambda i: (obtem_lin(i), obtem_col(i)))

    return tuple(ordem_leitura)

#2.1.2 - TAD pedra#
###################
def cria_pedra_branca():
    """cria pedra branca: {} → pedra

    Returns:
        [str]: [cria pedra branca]
    """    
    return "O"

def cria_pedra_preta():
    """cria pedra preta: {} → pedra

    Returns:
        [str]: [cria pedra preta]
    """    
    return "X"

def cria_pedra_neutra():
    """cria pedra neutra: {} → pedra

    Returns:
        [str]: [cria pedra neutra]
    """    
    return "."

def eh_pedra(arg):
    """eh pedra: universal → booleano

    Args:
        arg ([str]): [pedra]

    Returns:
        [bool]: [True or False, True se for pedra]
    """    
    #Verifica se o argumento dado é um dos três tipos de pedras
    return arg in (cria_pedra_branca(), cria_pedra_preta(), cria_pedra_neutra())

def eh_pedra_branca(arg):
    """eh pedra branca: pedra → booleano

    Args:
        arg ([str]): [pedra]

    Returns:
        [bool]: [True or False, True se for pedra branca]
    """    
    #Verifica se é pedra branca
    return arg == cria_pedra_branca()

def eh_pedra_preta(arg):
    """eh pedra preta: pedra → booleano

    Args:
        arg ([str]): [pedra]

    Returns:
        [bool]: [True or False, True se for pedra preta]
    """    
    #Verifica se é pedra preta
    return arg == cria_pedra_preta()

def pedras_iguais(p1, p2):
    """universal x universal → booleano

    Args:
        p1 ([str]): [pedra]
        p2 ([str]): [pedra]

    Returns:
        [bool]: [True or False, True se forem pedras iguais]
    """    
    #Verifica se p1 e p2 são pedras iguais
    return p1 == p2

def pedra_para_str(p):
    """pedra para str: pedra → str
    Converte pedra p para string

    Args:
        p ([str]): [tipo de pedra]

    Returns:
        [str]: [pedra]
    """    
    #Verifica o tipo de pedra de p e converte para a sua respetiva 
    #string de pedra
    if eh_pedra_branca(p): 
        return "O" 
    elif eh_pedra_preta(p): 
        return "X"
    else:
        return "."

#Alto Nível#
def eh_pedra_jogador(arg):
    """eh pedra jogador: pedra → booleano
    Verifica se arg é pedra de um jogador

    Args:
        arg ([str]): [pedra]

    Returns:
        [bool]: [True or False, True se for pedra de um jogador]
    """    
    #Verifica se a pedra é do jogador das pretas ou brancas
    return eh_pedra_branca(arg) or eh_pedra_preta(arg)


#2.1.3 - TAD goban#
###################
def cria_goban_vazio(n):
    """cria goban vazio: int → goban
    Cria um goban de tamanho n x n

    Args:
        n ([int]): [inteiro que define tamanho do goban]

    Raises:
        ValueError: [caso nao apresente argumentos como int ou de 9, 13, 19]

    Returns:
        [list]: [lista com o tabuleiro goban]
    """    
    #Verifica os argumentos
    if not type(n) == int or n not in (9, 13, 19):
        raise ValueError('cria_goban_vazio: argumento invalido')
    
    #Cria o goban como lista, adicionando pedra neutras (Goban vazio), do
    #tamanho n vertical e n horizontal
    goban = []
    for ltr in range(n):
        num = []
        goban += [num, ]
        for e in range(n):
            num += [cria_pedra_neutra(), ]

    return goban

def cria_goban(n, ib, ip):
    """cria goban: int x tuplo x tuplo → goban
    Cria um goban de tamanho n x n e com as entradas das pedra brancas e pretas
    iniciais

    Args:
        n ([int]): [tamanho do tabuleiro]
        ib ([tuple]): [tuplo com as pedras iniciais brancas]
        ip ([tuple]): [tuplo com as pedras iniciais pretas]

    Raises:
        ValueError: [caso n não seja tamanho 9, 13, 19 ou nao seja inteiro e
        caso ib e ip nao sejam tuplos ou tenham interseções repetidas]
        ValueError: [caso ib não seja interseção pertencente aos limites do g]
        ValueError: [caso ip não seja interseção pertencente aos limites do g]
        ValueError: [caso existe repetidos entre ib e ip]

    Returns:
        [list]: [lista do tabuleiro goban com as pedras iniciais]
    """    
    #Verifica se n é inteiro ou é 9, 13, 19 e se ib e ip são tuplo e  nao tem 
    # interseções repetidas
    if not type(n) == int or n not in (9, 13, 19) or not isinstance(ib, tuple) \
        or not isinstance(ip, tuple)  or len(ib) != len(tuple(set(ib))) or \
            len(ip) != len(tuple(set(ip))):
        raise ValueError('cria_goban: argumentos invalidos')
    goban = cria_goban_vazio(n)
    
    #Verifica em cada ib e ip se os elementos são interseções e se estao dentro
    #do goban
    for e in ib:
        if not eh_intersecao(e) or ord(obtem_col(e)) - 64 > n or \
            ord(obtem_col(e)) < 65 or obtem_lin(e) > n:
            raise ValueError('cria_goban: argumentos invalidos')
    for e in ip:
        if not eh_intersecao(e) or ord(obtem_col(e)) - 64 > n or \
            ord(obtem_col(e)) < 65 or obtem_lin(e) > n:
            raise ValueError('cria_goban: argumentos invalidos')
        
    #Verifica a possibilidade de interseções iguais em ib e ipe
    for e in ip:
        for i in ib:
            if intersecoes_iguais(e, i):
                raise ValueError('cria_goban: argumentos invalidos')
    
    #Adiciona as pedras brancas de ib no goban
    for e in ib:
        goban[ord(obtem_col(e)) - 65][obtem_lin(e) - 1] = cria_pedra_branca()
    #Adiciona as pedras pretas de ip no goban
    for e in ip:
        goban[ord(obtem_col(e)) - 65][obtem_lin(e) - 1] = cria_pedra_preta()

    return goban

def cria_copia_goban(t):
    """cria copia goban: goban → goban
    Cria uma cópia pura do goban t 
    Args:
        t ([list]): [lista com o goban]

    Returns:
        [list]: [copia da lista do goban]
    """
    #Cria lista a ser copiada
    copia_pura = []
    #Copia cada linha e cada elemento 
    for e in t:
        lst = []
        copia_pura += [lst]
        for i in e:
            lst += [i]

    return copia_pura

def obtem_ultima_intersecao(g):
    """obtem ultima intersecao: goban → intersecao
    Obtem a ultima interseção do goban dado

    Args:
        g ([list]): [lista com o goban todo]

    Returns:
        [tuple]: [tuplo com a ultima interseção do goban]
    """    
    return cria_intersecao(f"{chr(len(g) + 64)}", len(g[0]))

def obtem_pedra(g, i):
    """obtem pedra: goban x intersecao → pedra
    Obtem o tipo de pedra de uma interceçao de um goban

    Args:
        g ([list]): [lista com o goban]
        i ([tuple]): [tuplo interseção]

    Returns:
        [str]: [string com o tipo de pedra]
    """    
    return g[ord(obtem_col(i)) - 65][obtem_lin(i) - 1]

def obtem_cadeia(g, i):
    """obtem cadeia: goban x intersecao → tuplo
    Obtem a cadeia de uma certa interseção num dado goban, sendo que a cadeia
    equivale a pedra conectadas entre si e do mesmo tipo de pedra
    Args:
        g ([list]): [lista com o goban]
        i ([tuple]): [tuplo interseção]
    """    
    def obtem_cadeia_nrepetidos(atual, jadentro):
        """obtem cadeia nrepetidos: PRIVATE: tuple x tuple → tuple

        Args:
            atual ([tuple]): [tuplo com a interceção atual]
            jádentro ([tuple]): [tuplo com interseções já vistas]

        Returns:
            [tuple]: [tuplo com as cadeias]
        """        
        #Adiciona o tuplo atual ao conjunto já vistos
        jadentro.add(atual)
        #obtem os adjacentes do atual e define o atual como pertencente 
        # há cadeia
        adjacentes = obtem_intersecoes_adjacentes(atual, \
                                                  obtem_ultima_intersecao(g))
        cadeia = (atual, )
        #Adiciona as pedras que são iguais e adjacentes e que não ainda não
        #estejam no jádentro
        for e in adjacentes:
            if e not in jadentro and pedras_iguais(obtem_pedra(g, atual), \
                                                   obtem_pedra(g, e)):
                cadeia += obtem_cadeia_nrepetidos(e, jadentro)
        #ordena as interceções da cadeia
        return ordena_intersecoes(cadeia)
    
    #Chama a função privada criada para obter a cadeia
    return ordena_intersecoes(obtem_cadeia_nrepetidos(i, set()))

def coloca_pedra(g, i, p):
    """coloca pedra: goban x intersecao x pedra → goban
    coloca a pedra i de tipo p no goban g

    Args:
        g ([list]): [lista que contem o goban]
        i ([tuple]): [tuplo interseção]
        p ([str]): [string com o tipo de pedra]

    Returns:
        [list]: [goban modificado destrutivamente]
    """    
    #Substitui a pedra no goban
    g[ord(obtem_col(i)) - 65][obtem_lin(i) - 1] = p
    return g

def remove_pedra(g, i):
    """remove pedra: goban x intersecao → goban
    remove a pedra i no goban g

    Args:
        g ([list]): [lista com o goban]
        i ([tuple]): [tuplo interceção]

    Returns:
        [list]: [lista goban modificado destrutivamente]
    """    
    #Subtitui a pedra no goban
    g[ord(obtem_col(i)) - 65][obtem_lin(i) - 1] = cria_pedra_neutra()
    return g

def remove_cadeia(g ,t):
    """remove cadeia: goban x tuplo → goban
    remove a cadeia t no goban t

    Args:
        g ([list]): [lista goban]
        t ([tuple]): [tuplo com interceções]

    Returns:
        [list]: [lista goban modificado destrutivamente]
    """    
    #Aplica a remoção para cada interceção de t no g 
    for e in t:
        g = remove_pedra(g, e)
    return g

def eh_goban(arg):
    """eh goban: universal → booleano
    Verifica se é goban

    Args:
        arg ([list]): [lista goban]

    Returns:
        [bool]: [True or False, True caso seja goban]
    """    
    #verifica se arg é uma lista, se o tamanho é 9, 13, 19, se os tamanhos das 
    # listas são 9, 13, 19 e se o tamanho vertical e horizontal são todos iguais
    if not isinstance(arg, list) or not len(arg) in (9, 13, 19) or \
        not (len(e) in (9, 13, 19) for e in arg) or not \
            (len(e) == len(arg) for e in arg):
        return False
    
    #Verifica se todos os elementos são listas dentro do goban
    for e in arg:
        if not isinstance(arg, list):
            return False
    
    #Verifica se todos os elementos dentros das listas dentro do 
    # goban sao pedras
    for e in arg:
        for i in e:
            if not eh_pedra(i):
                return False
            
    return True

#FUNÇÃO ADICIONAL
def cria_todas_intersecoes(g):
    """cria_todas_intersecoes: lista → tuplo
    cria um tuplo com todas as interceções dentro do goban g

    Args:
        g ([list]): [lista goban]

    Returns:
        [tuple]: [tuplo com todas as interceções]
    """    
    #Calcula tamanho máxmio vertica e horizontal
    tamanho_horizontal = len(g)
    tamanho_vertical = len(g)
    conjunto_de_coordenadas_total = ()

    #Vai criar um conjunto de interseções que existe no goban
    for H in range(tamanho_horizontal):
        for V in range(1, tamanho_vertical + 1):
            conjunto_de_coordenadas_total += (cria_intersecao(chr(65 + H), V), )
    return conjunto_de_coordenadas_total

def eh_intersecao_valida(g, i):
    """eh intersecao valida: goban x intersecao → booleano
    Verifica se uma interseção é valida no goban

    Args:
        g ([list]): [lista com goban]
        i ([tuple]): [tuplo interseção]

    Returns:
        [bool]: [True or False, True caso seja]
    """    
    #Verifica se é interseção e se i está dentro de todas as interseções de g
    return eh_intersecao(i) and i in cria_todas_intersecoes(g)

def gobans_iguais(g1, g2):
    """gobans iguais: universal × universal 7→ booleano

    Args:
        g1 ([list]): [lista do goban 1]
        g2 ([list]): [lista do goban 2]

    Returns:
        [bool]: [True or False, True caso sejam iguais]
    """    
    #Caso nenhum seja goban, retoma falso
    if not eh_goban(g1) or not eh_goban(g2):
        return False
    
    #Caso exista diferença do tamanho dos gobans
    if len(g1) != len(g2):
        return False
    
    #Verifica se cada pedra dentro do goban é iguais e na posição igual nos
    #dois gobans
    for i in range(len(g1)):
        for m in range(len(g1)):
            if not pedras_iguais(obtem_pedra(g1, cria_intersecao(chr(i + 65),\
             m + 1)), obtem_pedra(g2, cria_intersecao(chr(i + 65), m + 1)) ):
                return False
    return True

def goban_para_str(g):
    """goban para str: goban → str
    Cria a visualização de string do goban
    Args:
        g ([list]): [lista de goban]

    Returns:
        [str]: [string com a visualização ]
    """    
    visualizacao = '  '

    #Define o tamanho do goban através do tamanho horizontal e vertical
    tamanho = obtem_ultima_intersecao(g)
    len_horizontal, len_vertical = (ord(obtem_col(tamanho)) -64),\
                                                             obtem_lin(tamanho)

    #Adiciona as letras em cima da visualização
    for letra in range(len_horizontal): 
        visualizacao += ' ' + chr(65 + letra)
    
    #Adiciona os espaços, sendo "." caso diferente de 1 e "X" se igual a 1
    i = len_vertical - 1
    while 0 <= i:

        #Adiciona números na lateral esquerda, corrigindo o espaçamento dos numeros
        if i < 9:
            visualizacao += '\n ' + f'{i + 1}'
        else:
            visualizacao += '\n' + f'{i + 1}'

        #Ciclo para adição dos espaços, fazendo por sequencia de elementos 
        # dos tuplos da lista t
        for e in range(len_horizontal):
            visualizacao += f' {g[e][i]}'
        
        #Adiciona números na lateral direita, 
        # utilização de if para correção do espaçamento dos numeros
        if i < 9:
            visualizacao += '  ' + f'{i + 1}'
        else:
            visualizacao += ' ' + f'{i + 1}'
        i -= 1

    #Adiciona as letras em baixo da visualização
    visualizacao += '\n  ' #Segue a str para baixo
    for letra in range(len_horizontal):
        visualizacao += ' ' + chr(65 + letra)

    return visualizacao

#Alto Nível#
def obtem_adjacentes_neutros(g, e):
    """obtem adjacentes neutro: list x tuple → tuple
    Cria todas as interseções adjacentes que sejam neutros

    Args:
        g ([list]): [lista goban]
        e ([tuple]): [tuplo intercesão]

    Returns:
        [tuple]: [tuplo com interseções neutras]
    """    
    #Verifica se cada interseção adjacente a e é neutra e obtem esse conjunto 
    #nas pedras
    pedras = []
    for cada in e:
        poss_pedras = obtem_intersecoes_adjacentes(cada, \
                                                   obtem_ultima_intersecao(g))
        for e in poss_pedras:
            if obtem_pedra(g, e) != cria_pedra_neutra() and e not in pedras:
                pedras.append(e)
    return pedras

def obtem_territorios(g):
    """obtem territorios: goban → tuplo
    obtem os territórios de um goban
    Args:
        g ([list]): [lista goban]

    Returns:
        [tuple]: [tuplos com territórios]
    """
    #Obtem o conjunto de todas as interseções
    conjunto = ordena_intersecoes(cria_todas_intersecoes(g))
    territorios = ()
    já_visto = ()
    #Obtem, para cada elemento do goban, as cadeias de neutras e verifica se já
    #pertencem aos territórios
    for e in conjunto:
        if not eh_pedra_jogador(obtem_pedra(g, e)) and e not in já_visto:
            #Obtem cadeia para duas variáveis para melhor otimização
            cadeia = obtem_cadeia(g, e)
            já_visto += cadeia
            territorios += (cadeia, )
            
    return territorios

def obtem_adjacentes_diferentes(g, t):
    """obtem adjacentes diferentes: goban x tuplo → tuplo
    Obtem os adjacentes que sejam o contrário do valor eh_pedra_jogador do tuplo
    t
    Args:
        g ([list]): [lista goban]
        t ([tuple]): [tuplo com interceções]

    Returns:
        [tuple]: [tuplo ordenado com as interseções diferentes]
    """    
    #Verifica se todas as pedras da cadeia t são iguais
    valor = all(eh_pedra_jogador(obtem_pedra(g, e)) for e in t)
    diferentes = ()

    #Obtem adjacentes para cada elemento em t, verificando se é oposto ao valor
    for e in t:
        adjacentes_provisório = \
        obtem_intersecoes_adjacentes(e, obtem_ultima_intersecao(g))
        #Verifica cada elemento dos adjacentes_provisórios, resultado do
        #Obtem_adjacentes
        for i in adjacentes_provisório:
            if eh_pedra_jogador(obtem_pedra(g, i)) != valor and i \
                                                not in diferentes:
                diferentes += (i, )

    return ordena_intersecoes(diferentes)

def jogada(g, i, p):
    """jogada: goban x intersecao x pedra 7→ goban
    Faz a jogada no goban g com a interseção i de valor de pedra p
    Args:
        g ([list]): [lista goban]
        i ([tuple]): [tuplo interceção]
        p ([str]): [string com valor do tipo de pedra]

    Returns:
        [list]: [goban modificado destrutivamente]
    """    
    #Primeiro coloca pedra no goban
    g = coloca_pedra(g, i, p)

    #Verifica o valor da pedra oposta do eh_pedra_jogador
    if pedras_iguais(p, cria_pedra_branca()):
        jogador_oposto = cria_pedra_preta()
    elif pedras_iguais(p, cria_pedra_preta()):
        jogador_oposto = cria_pedra_branca()

    #Obtem as interceções adjacentes da pedra jogada
    cadeia_jogada = obtem_intersecoes_adjacentes(i, obtem_ultima_intersecao(g))
    
    #Para cada interceção, verifica se as pedras adjacentes têm valor oposto e
    #verifica se a cadeias dessas pedras perdem a liberdade, removendo a 
    #destrutivamente do goban
    for e in cadeia_jogada:
        if pedras_iguais(obtem_pedra(g, e), jogador_oposto):
            cadeia_possivel_eliminada = obtem_cadeia(g, e)
            if obtem_adjacentes_diferentes(g, cadeia_possivel_eliminada) == ():
                g = remove_cadeia(g, cadeia_possivel_eliminada)
    return g

def obtem_pedras_jogadores(g):
    """obtem pedras jogadores: goban 7→ tuplo
    Obtem o numero de pedras do jogador das brancas e pretas
    Args:
        g ([list]): [lista goban]

    Returns:
        [tuple]: [tuplo com pedras]
    """    
    #Cria todas as interceções do tabuleiro g
    conjunto = cria_todas_intersecoes(g)
    brancas = 0
    pretas = 0

    #Verifica as pedras para cada posição e verifica se é branca ou preta
    for e in conjunto:
        if pedras_iguais(obtem_pedra(g, e), cria_pedra_branca()):
            brancas += 1
        elif pedras_iguais(obtem_pedra(g, e), cria_pedra_preta()):
            pretas += 1

    return (brancas, pretas)

    ###################################
   #                                 #
  #  2ª Parte - Funções Adicionais  #
 #                                 #
###################################


#2.2.1 calcula_pontos
def calcula_pontos(g):
    """goban x intersecao x pedra x goban → booleano
    Calcula os pontos no goban g
    Args:
        g ([list]): [lista goban]

    Returns:
        [tuple]: [tuplo com a pontuação das brancas e pretos]
    """    
    #Obtem os pontos das pedras de ambos os jogadores
    pontos_pedra = obtem_pedras_jogadores(g)
    pontos_brancas = pontos_pedra[0]
    pontos_pretas = pontos_pedra[1]
    #Caso não haja pedras, devolve tuplo (0,0) pontuação
    if pontos_pretas == pontos_brancas == 0:
        return (0, 0)
    
    #Obtem os territorios de g
    territorios = obtem_territorios(g)
    #Calcula para cada interseção os pontos dos territórios, comfirmando cada
    #território a que jogador pertence, sendo rodeado apenas pelo mesmo tipo 
    #de pedra
    for e in territorios:
        adjacentes = obtem_adjacentes_diferentes(g, e)
        if all(pedras_iguais(obtem_pedra(g, e), cria_pedra_branca())\
                for e in adjacentes):
            pontos_brancas += len(e)
        elif all(pedras_iguais(obtem_pedra(g, e), cria_pedra_preta())\
                  for e in adjacentes):
            pontos_pretas += len(e)

    return (pontos_brancas, pontos_pretas)

#2.2.2 eh_jogada_legal
def eh_jogada_legal(g, i, p, l):
    """goban x intersecao x pedra x goban → booleano
    Verifica se uma jogada é válida ou não
    Args:
        g ([list]): [lista goban]
        i ([tuple]): [tuplo interseção]
        p ([str]): [string de pedra]
        l ([list]): [list goban copia]

    Returns:
        [bool]: [True or False, True caso seja]
    """    
    #Verifica se i é uma interseção válida em g
    if not eh_intersecao_valida(g, i):
        return False
    
    copia = cria_copia_goban(g)
    jogada(copia, i, p)

    #Verifica se a jogada está num espaço vazio, se a jogada é suicidio ou se 
    #é uma repetição ou Ko
    if not pedras_iguais(obtem_pedra(g, i), cria_pedra_neutra()) \
    or obtem_adjacentes_diferentes(copia, obtem_cadeia(copia, i)) == () \
    or gobans_iguais(copia, l):
        return False
    return True

#2.2.3 turno_jogador
def turno_jogador(g, p, l):
    """turno jogador: goban x pedra x goban 7→ booleano 
    Cria um turno para o jogador, verificando argumentos dados introduzidos pelo
    utilizador
    Args:
        g ([list]): [lista goban]
        p ([str]): [string pedra]
        l ([list]): [lista goban]

    Returns:
        [bool]: [True or False, true caso seja]
        [function]: [Retoma função caso seja falso]
    """    
    #Regista o input do jogador
    jogad = input(f"Escreva uma intersecao ou 'P' para passar [{pedra_para_str(p)}]:")
    #Verifica se o jogador passou "P"
    if jogad == 'P':
        return False
    
    #Verifica a validade do argumento dado pelo jogador, caso não seja, repete
    if not 2 <= len(jogad) <= 3 or not 'A' <= jogad[0] <= 'Z' or\
      not '1' <= jogad[1:] <= '99':
        return turno_jogador(g, p, l)

    #Converte a interseção de string para tuplo
    intersecao = str_para_intersecao(jogad)

    #Verifica se a jogada é possivel, se é interseção, se é válida
    # e se é legal
    if eh_intersecao(intersecao) and eh_intersecao_valida(g, intersecao) \
    and eh_jogada_legal(g, intersecao, p, l):
        jogada(g, intersecao, p)
        return True
    return turno_jogador(g, p, l)

def go(n, tb, tp):
    """go: int x tuple x tuple → booleano

    Args:
        n ([int]): [inteiro que define tamanho do goban]
        tb ([tuple]): [tuplo das interceções iniciais brancas]
        tp ([tuple]): [tuplo das interceções iniciais pretas]

    Raises:
        ValueError: [caso não sejam argumentos para criar goban valido]
        ValueError: [caso não sejam tuplos]
        ValueError: [caso os argumentos no tuplo das brancas sejam inválidos]
        ValueError: [caso os argumentos no tuplo das pretas sejam inválidos]
        ValueError: [caso os elementos não sejam interseções válidas]
        ValueError: [caso os elementos não sejam interseções válidas]
        ValueError: [caso nao seja goban válido]

    Returns:
        [bool]: [True or False, True caso as brancas ganhem]
    """
    #Verifica se n tem argumentos corretos para goban
    if not type(n) == int or n not in (9, 13, 19):
        raise ValueError('go: argumentos invalidos')
    
    #Verifica se tb e tp são tuplos
    if not isinstance(tb, tuple) or not isinstance(tp, tuple):
        raise ValueError('go: argumentos invalidos')
    
    #Verifica se cada elemento de ambos os tuplos é válido ou não
    for e in tb:
        if not isinstance(e, str) or not 2 <= len(e) <= 3 or\
          not 'A' <= e[0] <= 'Z' or not '1' <= e[1:] <= '99':
            raise ValueError('go: argumentos invalidos')
    for e in tp:
        if not isinstance(e, str) or not 2 <= len(e) <= 3 or \
        not 'A' <= e[0] <= 'Z' or not '1' <= e[1:] <= '99':
            raise ValueError('go: argumentos invalidos')

    #Transforma as strings dos tuplos para interseções de tuplos
    ib = tuple(str_para_intersecao(i) for i in tb)
    ip = tuple(str_para_intersecao(i) for i in tp)

    #Cria o goban vazio para verificar se são interseções válidas
    g = cria_goban_vazio(n)
    for e in ib:
        if not eh_intersecao(e) or not eh_intersecao_valida(g, e):
            raise ValueError('go: argumentos invalidos')
    for e in ip:
        if not eh_intersecao(e) or not eh_intersecao_valida(g, e) or e in ib:
            raise ValueError('go: argumentos invalidos')
        
    #Verifica se o goban é válido
    g = cria_goban(n, ib, ip)
    if not eh_goban(g):
        raise ValueError('go: argumentos invalidos')
        
    #Define pedra branca e preta e as variáveis para o correto funcionamento
    branca = cria_pedra_branca()
    preta = cria_pedra_preta()
    verificação = [[], []]
    c = 1
    fim = 0
    g = cria_goban(n, ib, ip)
    p = preta
    #Dá o primeiro print de introdução do jogo
    pontos = calcula_pontos(g)
    print(f"Branco (O) tem {pontos[0]} pontos")
    print(f"Preto (X) tem {pontos[1]} pontos")
    print(goban_para_str(g))

    #Função que começa o jogo
    def jogo(g, p,  branca, preta, pontos, verificação, c, fim):
        """jog: PRIVATE

        Args:
            g ([list]): [goban]
            p ([str]): [pedra]
            branca ([str]): [pedra branca]
            preta ([str]): [pedra preta]
            pontos ([tuple]): [tuplo com os pontos]
            verifica ([list]): [lista com os tuplos passados]
            c ([int]): [int com contador]
            fim ([int]): [int com contador para final]

        Returns:
            [bool]: [True or False, True caso as brancas ganhem]
        """        
        #Lista com os gobans passados para verificação
        verificação = [verificação[1], cria_copia_goban(g)]

        #Verificação se a jogada é passada ou não
        if turno_jogador(g, p, verificação[-2]):
            #Se não for passado, calcula os pontos e representa o tabuleiro goban
            #atual, após ser feita a jogada
            pontos = calcula_pontos(g)
            print(f"Branco (O) tem {pontos[0]} pontos")
            print(f"Preto (X) tem {pontos[1]} pontos")
            print(goban_para_str(g))
            fim = 0
        else:
            #Caso seja passado, representa o mesmo tabuleiro goban e aumenta o
            #fim + 1
            print(f"Branco (O) tem {pontos[0]} pontos")
            print(f"Preto (X) tem {pontos[1]} pontos")
            print(goban_para_str(g))
            fim += 1
            #Caso seja passado duas vezes, retorna True or False, True se as
            #brancas ganharem
            if fim == 2:
                return pontos[0] >= pontos[1]

        #Define o turno do jogador
        p = preta if c % 2 == 0 else branca

        return jogo(g, p, branca, preta, pontos, verificação, c + 1, fim)
    
    return jogo(g, p, branca, preta, pontos, verificação, c, fim)
