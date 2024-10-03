from PIL import Image


def ampliar_vizinho_mais_proximo(img, dimensao_aumento):
    """
        Função que amplia imagem por vizinho mais próximo.

        :param img: imagem a ser ampliada
        :param largura_original: largura da imagem original em pixels
        :param altura_original: altura da imagem original em pixels
        :param dimensao_aumento: valor inteiro que representa o número de vezes que a imagem será ampliada

        :return nova_img: retorna a imagem gerada
    """
    if img.mode != 'RGB':
        img = img.convert('RGB')
        
    # Pega os valores de largura e altura da imagem
    largura_original, altura_original = img.size

    # Definição das novas dimensões da imagem
    largura_nova = largura_original * dimensao_aumento
    altura_nova = altura_original * dimensao_aumento

    # Criação de um novo objeto do tipo Image, definido com as novas dimensões
    nova_img = Image.new('RGB', (largura_nova, altura_nova))
    pixels = img.load()  # Carrega a matriz de pixels da img na variável pixels
    novos_pixels = nova_img.load()  # Carrega a matriz de pixels da nova_img na variável novos_pixels

    # Loop que percorre todos os pixels da nova_img
    for x in range(largura_nova):
        for y in range(altura_nova):
            x_original = int(x * largura_original / largura_nova)
            y_original = int(y * altura_original / altura_nova)
            novos_pixels[x, y] = pixels[x_original, y_original]

    return nova_img

def reduzir_vizinho_mais_proximo(img, dimensao_reducao):
    """
        Função que reduz imagem por vizinho mais próximo.

        :param img: imagem a ser reduzida
        :param largura_original: largura da imagem original em pixels
        :param altura_original: altura da imagem original em pixels
        :dimensao_aumento: valor inteiro que representa o número de vezes que a imagem será reduzida

        :return nova_img: retorna a imagem gerada
    """
    if img.mode != 'RGB':
        img = img.convert('RGB')

    # Pega os valores de largura e altura da ima
    largura_original, altura_original = img.size

    # Definição das novas dimensões da imagem
    largura_nova = int(largura_original / dimensao_reducao)
    altura_nova =  int(altura_original / dimensao_reducao)

    # Criação de um novo objeto do tipo Image, definido com as novas dimensões
    nova_img = Image.new('RGB', (largura_nova, altura_nova))
    pixels = img.load()  # Carrega a matriz de pixels da img na variável pixels
    novos_pixels = nova_img.load()  # Carrega a matriz de pixels da nova_img na variável novos_pixels

    # Loop que percorre todos os pixels da nova_img
    for x in range(largura_nova):
        for y in range(altura_nova):
            x_original = int(x * dimensao_reducao)
            y_original = int(y * dimensao_reducao)
            novos_pixels[x, y] = pixels[x_original, y_original]

    return nova_img

def reduzir_bilinear(img, dimensao_reducao):
    """
        Função que reduz imagem por interpolação bilinear.

        :param img: imagem a ser reduzida
        :param largura_original: largura da imagem original em pixels
        :param altura_original: altura da imagem original em pixels
        :dimensao_aumento: valor inteiro que representa o número de vezes que a imagem será reduzida

        :return nova_img: retorna a imagem gerada
    """
    if img.mode != 'RGB':
        img = img.convert('RGB')

    # Pega os valores de largura e altura da ima
    largura_original, altura_original = img.size

    # Definição das novas dimensões da imagem
    largura_nova = int(largura_original / dimensao_reducao)
    altura_nova = int(altura_original / dimensao_reducao)

    # Criação de um novo objeto do tipo Image, definido com as novas dimensões
    nova_img = Image.new('RGB', (largura_nova, altura_nova))
    pixels = img.load()  # Carrega a matriz de pixels da img na variável pixels
    novos_pixels = nova_img.load()  # Carrega a matriz de pixels da nova_img na variável novos_pixels

    # Loop que percorre todos os pixels da nova_img
    for x in range(largura_nova):
        for y in range(altura_nova):
            # Mapeamento das coordenadas da nova imagem na imagem original
            x_original = x * dimensao_reducao
            y_original = y * dimensao_reducao

            # Valores dos pixels nos quatro cantos
            pixel_11 = pixels[x_original, y_original]
            pixel_21 = pixels[x_original + 1, y_original]
            pixel_12 = pixels[x_original, y_original + 1]
            pixel_22 = pixels[x_original + 1, y_original + 1]

            # Interpolação bilinear para cada canal de cor (R, G, B)
            r = (pixel_11[0] + pixel_21[0] + pixel_12[0] + pixel_22[0]) / 4

            g = (pixel_11[1] + pixel_21[1] + pixel_12[1] + pixel_22[1]) / 4

            b = (pixel_11[2] + pixel_21[2] + pixel_12[2] + pixel_22[2]) / 4

            # Definir o valor do pixel interpolado na nova imagem
            novos_pixels[x, y] = (int(r), int(g), int(b))

    return nova_img

def ampliar_bilinear(img, dimensao_aumento):
    """
        Função que amplia uma imagem por interpolação bilinear.

        :param img: imagem a ser reduzida
        :param largura_original: largura da imagem original em pixels
        :param altura_original: altura da imagem original em pixels
        :dimensao_aumento: valor inteiro que representa o número de vezes que a imagem será reduzida

        :return nova_img: retorna a imagem gerada
    """
    if img.mode != 'RGB':
        img = img.convert('RGB')

    # Pega os valores de largura e altura da ima
    largura_original, altura_original = img.size

    # Definição das novas dimensões da imagem
    largura_nova = largura_original * dimensao_aumento
    altura_nova = altura_original * dimensao_aumento

    # Criação de um novo objeto do tipo Image, definido com as novas dimensões
    nova_img = Image.new('RGB', (largura_nova, altura_nova))
    pixels = img.load()  # Carrega a matriz de pixels da img na variável pixels
    novos_pixels = nova_img.load()  # Carrega a matriz de pixels da nova_img na variável novos_pixels

    # Loop que percorre todos os pixels da nova_img
    for x in range(largura_nova):
        for y in range(altura_nova):
            # Mapeamento das coordenadas na imagem original
            x_original = x * largura_original / largura_nova
            y_original = y * altura_original / altura_nova

            if x_original + 1 >= largura_original:
                x_original -= 1
            if y_original + 1 >= altura_original:
                y_original -= 1

            pixel_11 = pixels[x_original, y_original]
            pixel_12 = pixels[x_original, y_original + 1]
            pixel_21 = pixels[x_original + 1, y_original]
            pixel_22 = pixels[x_original + 1, y_original + 1]

            # Interpolação bilinear para cada canal de cor (R, G, B)
            r = ((pixel_11[0] + pixel_21[0] + pixel_12[0] + pixel_22[0]) / 4)

            g = ((pixel_11[1] + pixel_21[1] + pixel_12[1] + pixel_22[1]) / 4)

            b = ((pixel_11[2] + pixel_21[2] + pixel_12[2] + pixel_22[2]) / 4)

            novos_pixels[x, y] = (int(r), int(g), int(b))

    return nova_img


def main():
    imagens = {'radiação': 'radiacao.jpg', 'gato': 'gato.jpg', 'aguia': 'aguia.jpg', 'texto':'texto.png',
               'raiox': 'raiox.jpeg', 'moedas': 'moedas.jpg', 'pessoas': 'pessoas.jpg', 'objetos': 'objetos.jpg'}

    imagem_manipulada = imagens['texto']

    img = Image.open(f"input/{imagem_manipulada}")

    #nova_img = ampliar_vizinho_mais_proximo(img, 2)
    #nova_img = ampliar_bilinear(img, 2)
    #nova_img = reduzir_vizinho_mais_proximo(img, 2)
    nova_img = reduzir_bilinear(img, 3)

    # Salva a nova imagem
    try:
        nova_img.save(f'output/{imagem_manipulada}')
        print('Imagem salva')
    except:
        print('Erro ao salvar a imagem')

if __name__ == '__main__':
    main()
