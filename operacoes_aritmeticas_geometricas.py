from PIL import Image


def subtracao(img_1, img_2):
    """
        Função que subtrai os valores dos pixels de duas imagens.
        As duas imagens devem ter as mesmas dimensões para que a operação possa ser feita.

        :param img_1: imagem recebida para subtração;
        :param img_2: imagem recebida para subtração;

        :return img_resultante: retorna imagem gerada a partir da subtração.
    """
    # Converter as imagens para o modo RGB se estiver em grayscale
    if img_1.mode != 'RGB':
        img_1 = img_1.convert('RGB')
    if img_2.mode != 'RGB':
        img_2 = img_2.convert('RGB')
    
    largura, altura = img_1.size
    
    if img_1.size != img_2.size:
        print("As imagens precisam ter o mesmo tamanho...")
        return

    # Criando uma imagem vazia para armazenar o resultado
    img_resultante = Image.new('RGB', (largura, altura))

    pixels_img_1 = img_1.load()
    pixels_img_2 = img_2.load()
    pixels_img_resultante = img_resultante.load()

    # Iterando sobre cada pixel
    for x in range(largura):
        for y in range(altura):
            # Para cada canal RGB, é escolhido o maior valor entre a subtração e 0, 
            # para evitar que valores negativos sejam atribuidos.
            r = max(pixels_img_1[x, y][0] - pixels_img_2[x, y][0], 0)
            g = max(pixels_img_1[x, y][1] - pixels_img_2[x, y][1], 0)
            b = max(pixels_img_1[x, y][2] - pixels_img_2[x, y][2], 0)

            # Atribuindo o novo valor de cor ao pixel resultante
            pixels_img_resultante[x, y] = (r, g, b)

    return img_resultante

def multiplicacao(img_1, img_2):
    """
        Função que multiplica os valores dos pixels de duas imagens.
        As duas imagens devem ter as mesmas dimensões para que a operação possa ser feita.

        :param img_1: imagem recebida para multiplicação;
        :param img_2: imagem recebida para multiplicação;

        :return img_resultante: retorna imagem gerada a partir da multiplicação.
    """
    # Converter as imagens para o modo RGB se estiver em grayscale
    if img_1.mode != 'RGB':
        img_1 = img_1.convert('RGB')
    if img_2.mode != 'RGB':
        img_2 = img_2.convert('RGB')
    
    largura, altura = img_1.size
    
    if img_1.size != img_2.size:
        print("As imagens precisam ter o mesmo tamanho...")
        return

    # Criando uma imagem vazia para armazenar o resultado
    img_resultante = Image.new('RGB', (largura, altura))

    pixels_img_1 = img_1.load()
    pixels_img_2 = img_2.load()
    pixels_img_resultante = img_resultante.load()

    # Iterando sobre cada pixel
    for x in range(largura):
        for y in range(altura):
            # Para cada canal RGB, é escolhido o menor valor entre a multiplicação e 255, 
            # para evitar que valores maiores que 255 sejam atribuidos.
            r = min(pixels_img_1[x, y][0] * pixels_img_2[x, y][0], 255)
            g = min(pixels_img_1[x, y][1] * pixels_img_2[x, y][1], 255)
            b = min(pixels_img_1[x, y][2] * pixels_img_2[x, y][2], 255)

            # Atribuindo o novo valor de cor ao pixel resultante
            pixels_img_resultante[x, y] = (r, g, b)

    return img_resultante

def rotacao(imagem, angulo):
    """
        Função que faz a rotação de uma imagem.

        :param imgagem: imagem recebida para rotação;
        :param angulo: ângulo de rotação da imagem;

        :return img_resultante: retorna imagem gerada após a rotação.
    """
    from math import radians, cos, sin

    # Converte o ângulo para radianos
    theta = radians(angulo)
    
    # Obtém as dimensões da imagem
    largura, altura = imagem.size
    
    # Calcula o centro da imagem
    cx, cy = largura // 2, altura // 2
    
    # Cria uma nova imagem com fundo preto
    nova_imagem = Image.new('RGB', (largura, altura))
    pixels_origem = imagem.load()
    pixels_nova = nova_imagem.load()

    # Funções de rotação
    cos_theta = cos(theta)
    sin_theta = sin(theta)
    
    # Itera sobre cada pixel da nova imagem
    for x in range(largura):
        for y in range(altura):
            # Desloca para o centro
            x_offset = x - cx
            y_offset = y - cy
            
            # Aplica a matriz de rotação
            novo_x = int(cos_theta * x_offset - sin_theta * y_offset + cx)
            novo_y = int(sin_theta * x_offset + cos_theta * y_offset + cy)
            
            # Se as novas coordenadas estiverem dentro da imagem original, define o pixel
            if 0 <= novo_x < largura and 0 <= novo_y < altura:
                pixels_nova[x, y] = pixels_origem[novo_x, novo_y]

    return nova_imagem

def main():
    imagens = {'cidade1': 'cidade_1.jpg', 'cidade2': 'cidade_2.jpg', 'radiação': 'radiacao.jpg', 'gato': 'gato.jpg', 'aguia': 'aguia.jpg', 
               'raiox': 'raiox.jpeg', 'moedas': 'moedas.jpg', 'pessoas': 'pessoas.jpg', 'objetos': 'objetos.jpg', 'superman': 'superman.png'}

    imagem_manipulada_1 = imagens['superman']
    imagem_manipulada_2 = imagens['cidade2']

    img_1 = Image.open(f"input/{imagem_manipulada_1}")
    img_2 = Image.open(f'input/{imagem_manipulada_2}')

    #nova_img = subtracao(img_1, img_2)
    #nova_img = multiplicacao(img_1, img_2)
    nova_img = rotacao(img_1, 45)
    
    # Salva a nova imagem
    try:
        nova_img.save(f'output/imagem_nova.png')
        print('Imagem salva')
    except:
        print('Erro ao salvar a imagem')


if __name__ == '__main__':
    main()