from random import randint
from PIL import Image


def preto_branco(img):
    """
        Função que gera imagens binárias

        :param img: imagem a ser reduzida

        :return nova_img: retorna a imagem binária gerada
    """

    largura, altura = img.size

    # Cria um novo objeto Image com a largura e altura da imagem original
    nova_img = Image.new('RGB', (largura, altura))
    novos_pixels = nova_img.load()  # Carrega em novos_pixels a matriz de pixels da nova_img
    pixels = img.load()  # Carrega em pixels a matriz de pixels da imagem original

    # Loop que percorre todos os pixels da nova_img
    for x in range(largura):
        for y in range(altura):
            # O procedimento é: caso o pixel esteja mais perto de 0, é convertido para 0
            if pixels[x, y] < (127, 127, 127):
                novos_pixels[x, y] = (0, 0, 0)
            # Caso contrário o pixel é convertido para 255
            else:
                novos_pixels[x, y] = (255, 255, 255)

    return nova_img

def colorir_rotulos(img, matriz_rotulos):
    largura, altura = img.size

    # Criar um novo dicionário para mapear rótulos a cores
    cores_rotulos = {}
    
    # Definir uma função para gerar cores aleatórias
    def gerar_cor_aleatoria():
        return (randint(0, 255), randint(0, 255), randint(0, 255))

    # Criar uma nova imagem colorida
    img_colorida = Image.new("RGB", (largura, altura))
    pixels_img_colorida = img_colorida.load()

    # Passo 1: Associar uma cor a cada rótulo único
    for x in range(largura):
        for y in range(altura):
            rotulo = matriz_rotulos[x][y]
            if rotulo != '':  # Apenas colorir os pixels rotulados
                if rotulo not in cores_rotulos:
                    cores_rotulos[rotulo] = gerar_cor_aleatoria()  # Associar uma nova cor ao rótulo
                pixels_img_colorida[x, y] = cores_rotulos[rotulo]  # Aplicar a cor ao pixel

    return img_colorida

"""def rotulacao(img):
    largura, altura = img.size
    equivalencias = {}
    rotulos = []
    ultimo_rotulo = 0
    matriz_rotulos = []
    
    # Função que gera a imagem binária para rotulação
    img_preto_branco = preto_branco(img)

    pixels_img_pb = img_preto_branco.load()

    ## algoritmo rotulação
    for x in range(largura):
        matriz_rotulos.append(list())
        for y in range(altura):
            matriz_rotulos[x].append('')
            if pixels_img_pb[x, y] == (255, 255, 255) and x > 0 and y > 0:  # Isto é, se o pixel for branco (1)
                if pixels_img_pb[x - 1, y] == (0, 0, 0) and pixels_img_pb[x, y - 1] == (0, 0, 0):
                    #novo label para pixels_img_pb[x, y]
                    if len(rotulos) - 1 < ultimo_rotulo:
                        rotulos.append(f'{ultimo_rotulo}')
                    matriz_rotulos[x][y] = rotulos[ultimo_rotulo]
                    ultimo_rotulo += 1
                elif (pixels_img_pb[x - 1, y] == (255, 255, 255) and pixels_img_pb[x, y - 1] == (0, 0, 0)) or (pixels_img_pb[x - 1, y] == (0, 0, 0) and pixels_img_pb[x, y - 1] == (255, 255, 255)):
                    #rotula pixels_img_pb[x, y] com rótulo de r ou t
                    matriz_rotulos[x][y] = matriz_rotulos[x - 1][y]
                elif (pixels_img_pb[x - 1, y] == (255, 255, 255) and pixels_img_pb[x, y - 1] == (255, 255, 255)) and matriz_rotulos[x - 1][y] == matriz_rotulos[x][y - 1]:
                    # se r == 1, t == 1 e ambos possuem o mesmo rótulo
                    #rotula-se p com esse rótulo
                    matriz_rotulos[x][y] = matriz_rotulos[x - 1][y]
                elif (pixels_img_pb[x - 1, y] == (255, 255, 255) and pixels_img_pb[x, y - 1] == (255, 255, 255)) and matriz_rotulos[x - 1][y] != matriz_rotulos[x][y - 1] and matriz_rotulos[x][y - 1] != '' and matriz_rotulos[x - 1][y] != '':
                    # se r==1, t==1 e possuem rótulos diferentes
                    #rotula-se p com um dos rótulos e declara equivalência na lista
                    matriz_rotulos[x][y] = matriz_rotulos[x - 1][y]
                    equivalencias[matriz_rotulos[x - 1][y]] = matriz_rotulos[x][y - 1]

    # Passo 1: Encontrar o rótulo final para cada conjunto de rótulos equivalentes
    def encontrar_rotulo_final(rotulo, equivalencias):
        # Seguir as equivalências até encontrar o rótulo final
        while rotulo in equivalencias:
            rotulo = equivalencias[rotulo]
        return rotulo

    # Atualizar o dicionário de equivalências para que cada rótulo aponte para o rótulo final
    for rotulo in equivalencias.keys():
        rotulo_final = encontrar_rotulo_final(rotulo, equivalencias)
        equivalencias[rotulo] = rotulo_final

    # Passo 2: Atualizar a matriz de rótulos com os rótulos finais
    for x in range(largura):
        for y in range(altura):
            rotulo = matriz_rotulos[x][y]
            if rotulo in equivalencias:
                matriz_rotulos[x][y] = equivalencias[rotulo]

    return colorir_rotulos(img_preto_branco, matriz_rotulos)"""

def rotulacao(img):
    largura, altura = img.size
    equivalencias = {}
    rotulos = []
    ultimo_rotulo = 0
    matriz_rotulos = []
    
    # Função que gera a imagem binária para rotulação
    img_preto_branco = preto_branco(img)

    pixels_img_pb = img_preto_branco.load()

    ## algoritmo rotulação
    for x in range(largura):
        matriz_rotulos.append(list())
        for y in range(altura):
            matriz_rotulos[x].append('')

            if pixels_img_pb[x, y] == (255, 255, 255):  # Isto é, se o pixel for branco (1)
                vizinhos_rotulados = []

                # Verifica o pixel à esquerda (x - 1, y)
                if x > 0 and matriz_rotulos[x - 1][y] != '':
                    vizinhos_rotulados.append(matriz_rotulos[x - 1][y])

                # Verifica o pixel acima (x, y - 1)
                if y > 0 and matriz_rotulos[x][y - 1] != '':
                    vizinhos_rotulados.append(matriz_rotulos[x][y - 1])

                if len(vizinhos_rotulados) == 0:
                    # Novo rótulo se nenhum vizinho foi rotulado
                    if len(rotulos) - 1 < ultimo_rotulo:
                        rotulos.append(f'{ultimo_rotulo}')
                    matriz_rotulos[x][y] = rotulos[ultimo_rotulo]
                    ultimo_rotulo += 1

                elif len(vizinhos_rotulados) == 1:
                    # Apenas um vizinho rotulado, usa o mesmo rótulo
                    matriz_rotulos[x][y] = vizinhos_rotulados[0]

                else:
                    # Mais de um vizinho rotulado
                    matriz_rotulos[x][y] = vizinhos_rotulados[0]

                    # Se os rótulos dos vizinhos forem diferentes, adiciona equivalência
                    for rotulo in vizinhos_rotulados[1:]:
                        if rotulo != matriz_rotulos[x][y]:
                            equivalencias[rotulo] = matriz_rotulos[x][y]

    # Passo 1: Encontrar o rótulo final para cada conjunto de rótulos equivalentes
    def encontrar_rotulo_final(rotulo, equivalencias):
        # Seguir as equivalências até encontrar o rótulo final
        while rotulo in equivalencias:
            rotulo = equivalencias[rotulo]
        return rotulo

    # Atualizar o dicionário de equivalências para que cada rótulo aponte para o rótulo final
    for rotulo in equivalencias.keys():
        rotulo_final = encontrar_rotulo_final(rotulo, equivalencias)
        equivalencias[rotulo] = rotulo_final

    # Passo 2: Atualizar a matriz de rótulos com os rótulos finais
    for x in range(largura):
        for y in range(altura):
            rotulo = matriz_rotulos[x][y]
            if rotulo in equivalencias:
                matriz_rotulos[x][y] = equivalencias[rotulo]

    return colorir_rotulos(img_preto_branco, matriz_rotulos)


def main():
    imagens = {'radiação': 'radiacao.jpg', 'gato': 'gato.jpg', 'aguia': 'aguia.jpg', 
               'raiox': 'raiox.jpeg', 'moedas': 'moedas.jpg', 'pessoas': 'pessoas.jpg', 'objetos': 'objetos.jpg'}

    imagem_manipulada = imagens['moedas']

    img = Image.open(f"input/{imagem_manipulada}")

    #nova_img = preto_branco(img)
    nova_img = rotulacao(img)
    
    # Salva a nova imagem
    try:
        nova_img.save(f'output/{imagem_manipulada}')
        print('Imagem salva')
    except:
        print('Erro ao salvar a imagem')


if __name__ == '__main__':
    main()