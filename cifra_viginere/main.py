"""
Este módulo contém funções para lidar com mensagens interceptadas.
"""
MENSAGEM_INTERCEPTADA = "machi nesca nnott hink"
CHAVE_USADA = 'iamie xistt hatis cert'


def criptografar(mensagem, chave):
    """ Função usada para fazer a criptografia de um texto utilizando a cifra de viginère

    Args:
        mensagem (str): _description_
        chave (str): _description_

    Returns:
        str: texto criptografado
    """
    texto = ""
    while len(mensagem) > len(chave):
        chave += chave

    for indice, caractere in enumerate(mensagem):
        valor = 32 + (ord(caractere) - 32 + ord(chave[indice]) - 32) % 91
        caractere = chr(valor)
        texto += caractere
    return texto


def descriptografar(texto_cifrado, chave):
    """ Função usada para descriptografar um texto utilizando a cifra de viginère

    Args:
        cipher_text (_type_): _description_
        chave (_type_): _description_

    Returns:
        _type_: _description_
    """
    texto = ""
    while len(texto_cifrado) > len(chave):
        chave += chave

    for indice, caractere_cifrado in enumerate(texto_cifrado):
        valor = 32 + (ord(caractere_cifrado) - ord(chave[indice])) % 91
        caractere = chr(valor)
        texto += caractere

    return texto


texto_criptografado = criptografar(MENSAGEM_INTERCEPTADA, CHAVE_USADA)
print(texto_criptografado)
print(descriptografar(texto_criptografado, CHAVE_USADA))
