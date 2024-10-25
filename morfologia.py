# Alunos: Luís Felipe Krause de Castro & Patryck Henryck Moreira Silva

from PIL import Image

# Abertura e fechamento de imagem binária
# Dilatação e erosão de imagem em escala de cinza



def binarizar_img(img):
    """
        Função que gera imagens binárias

        :param img: imagem a ser reduzida

        :return nova_img: retorna a imagem binária gerada
    """

    largura, altura = img.size

    if img.mode != 'L':
        img = img.convert('L')

    # Cria um novo objeto Image com a largura e altura da imagem original
    nova_img = Image.new('L', (largura, altura))
    novos_pixels = nova_img.load()  # Carrega em novos_pixels a matriz de pixels da nova_img
    pixels = img.load()  # Carrega em pixels a matriz de pixels da imagem original

    # Loop que percorre todos os pixels da nova_img
    for x in range(largura):
        for y in range(altura):
            # O procedimento é: caso o pixel esteja mais perto de 0, é convertido para 0
            if pixels[x, y] < 127:
                novos_pixels[x, y] = 0
            # Caso contrário o pixel é convertido para 255
            else:
                novos_pixels[x, y] = 255

    return nova_img

def dilatar_Bi(img):
    """
        Utiliza o conceito de dilatação para dilatar imagens binárias.
        Elemento estruturante utilizado é análogo a 4-vizinhança.

        :param img: imagem recebida para manipulação;

        :return nova_img: retorna imagem após a dilatação;
    """
    img = binarizar_img(img)

    largura, altura = img.size

    nova_img = Image.new("L", (largura, altura))
    pixels = img.load()
    novos_pixels = nova_img.load()

    for x in range(largura):
        for y in range(altura):
            if pixels[x, y] == 255 and (x > 0 and y > 0) and (x < largura - 1 and y < altura - 1):
                pixel_acima = pixels[x, y - 1]
                pixel_direita = pixels[x + 1, y]
                pixel_esquerda = pixels[x - 1, y]
                pixel_abaixo = pixels[x, y + 1]

                novos_pixels[x, y] = pixels[x, y]

                if pixel_acima != 255:
                    novos_pixels[x, y - 1] = 255
                if pixel_direita != 255:
                    novos_pixels[x + 1, y] = 255
                if pixel_esquerda != 255:
                    novos_pixels[x - 1, y] = 255
                if pixel_abaixo != 255:
                    novos_pixels[x, y + 1] = 255
            else:
                novos_pixels[x, y] = pixels[x, y]

    return nova_img

def erodir_Bi(img):
    """
        Utiliza o conceito de erosão de imagens para erodir imagens binárias.
        Elemento estruturante utilizado é análogo a 4-vizinhança.

        :param img: imagem recebida para manipulação;

        :return nova_img: retorna imagem após a erosão;
    """
    img = binarizar_img(img)

    largura, altura = img.size

    nova_img = Image.new('L', (largura, altura))
    pixels = img.load()
    novos_pixels = nova_img.load()

    for x in range(largura):
        for y in range(altura):
            if pixels[x, y] == 255 and (x > 0 and y > 0) and (x < largura - 1 and y < altura - 1):
                pixel_acima = pixels[x, y - 1]
                pixel_direita = pixels[x + 1, y]
                pixel_esquerda = pixels[x - 1, y]
                pixel_abaixo = pixels[x, y + 1]

                if pixel_acima == 255 and pixel_direita == 255 and pixel_esquerda == 255 and pixel_abaixo == 255:
                    novos_pixels[x, y] = 255

                    novos_pixels[x, y - 1] = 0
                    novos_pixels[x + 1, y] = 0
                    novos_pixels[x - 1, y] = 0
                    novos_pixels[x, y + 1] = 0
            else: 
                novos_pixels[x, y] = 0

    return nova_img

def abertura_Bi(img):
    """
        Realiza a operação de abertura em uma imagem binária (erosão -> dilatação).

        :param img: imagem para manipulação

        :return img: retorna a imagem após as operações
    """
    return dilatar_Bi(erodir_Bi(img))

def fechamento_Bi(img):
    """
        Realiza a operação de fechamento em uma imagem binária (erosão -> dilatação).

        :param img: imagem para manipulação

        :return img: retorna a imagem após as operações
    """
    return erodir_Bi(dilatar_Bi(img))

def dilatar_GS(img):
    """
        Utiliza o conceito de dilatação de imagens para dilatar imagens em tons de cinza.
        Elemento estruturante utilizado é análogo a 4-vizinhança.

        :param img: imagem recebida para manipulação;

        :return nova_img: retorna imagem após a dilatação;
    """
    if img.mode != 'L':
        img = img.convert('L')

    largura, altura = img.size

    nova_img = Image.new("L", (largura, altura))
    pixels = img.load()
    novos_pixels = nova_img.load()

    for x in range(largura):
        for y in range(altura):
            if (x > 0 and y > 0) and (x < largura - 1 and y < altura - 1):
                pixel_acima = pixels[x, y - 1]
                pixel_direita = pixels[x + 1, y]
                pixel_esquerda = pixels[x - 1, y]
                pixel_abaixo = pixels[x, y + 1]

                maior_val = max([pixel_esquerda, pixel_abaixo, pixel_acima, pixel_direita])

                novos_pixels[x, y] = maior_val

    return nova_img

def erodir_GS(img):
    """
        Utiliza o conceito de erosão de imagens para erodir imagens em tons de cinza.
        Elemento estruturante utilizado é análogo a 4-vizinhança.

        :param img: imagem recebida para manipulação;

        :return nova_img: retorna imagem após a dilatação;
    """
    if img.mode != 'L':
        img = img.convert('L')

    largura, altura = img.size

    nova_img = Image.new("L", (largura, altura))
    pixels = img.load()
    novos_pixels = nova_img.load()

    for x in range(largura):
        for y in range(altura):
            if (x > 0 and y > 0) and (x < largura - 1 and y < altura - 1):
                pixel_acima = pixels[x, y - 1]
                pixel_direita = pixels[x + 1, y]
                pixel_esquerda = pixels[x - 1, y]
                pixel_abaixo = pixels[x, y + 1]

                maior_val = min([pixel_esquerda, pixel_abaixo, pixel_acima, pixel_direita])

                novos_pixels[x, y] = maior_val

    return nova_img

def main():
    imagens = {'radiação': 'radiacao.jpg', 'gato': 'gato.jpg', 'aguia': 'aguia.jpg', 'superman':'superman.png', 
               'raiox': 'raiox.jpeg', 'moedas': 'moedas.jpg', 'pessoas': 'pessoas.jpg', 'objetos': 'objetos.jpg', 'texto': 'texto.png'}

    imagem_manipulada = imagens['gato']

    img = Image.open(f"input/{imagem_manipulada}")

    nova_img = dilatar_GS(img)
    
    # Salva a nova imagem
    try:
        nova_img.save(f'output/{imagem_manipulada}')
        print('Imagem salva')
    except:
        print('Erro ao salvar a imagem')


if __name__ == '__main__':
    main()