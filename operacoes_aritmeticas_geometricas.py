"""
2 operações aritméticas: adição, subtração, divisão,
multiplicação.
 1 operação geométrica: rotação, translação, espelhamento ou
reflexão.
"""

from PIL import Image


def subtracao(img_1, img_2, offset=30):
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
            r = max(pixels_img_1[x, y][0] - pixels_img_2[x, y][0] + offset, 0)
            g = max(pixels_img_1[x, y][1] - pixels_img_2[x, y][1] + offset, 0)
            b = max(pixels_img_1[x, y][2] - pixels_img_2[x, y][2] + offset, 0)

            # Atribuindo o novo valor de cor ao pixel resultante
            pixels_img_resultante[x, y] = (r, g, b)

    return img_resultante

def multiplicacao(img_1, img_2):
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
            r = min(pixels_img_1[x, y][0] * pixels_img_2[x, y][0], 255)
            g = min(pixels_img_1[x, y][1] * pixels_img_2[x, y][1], 255)
            b = min(pixels_img_1[x, y][2] * pixels_img_2[x, y][2], 255)

            # Atribuindo o novo valor de cor ao pixel resultante
            pixels_img_resultante[x, y] = (r, g, b)

    return img_resultante

def main():
    imagens = {'cidade1': 'cidade_1.jpg', 'cidade2': 'cidade_2.jpg'}

    imagem_manipulada_1 = imagens['cidade1']
    imagem_manipulada_2 = imagens['cidade2']

    img_1 = Image.open(f"input/{imagem_manipulada_1}")
    img_2 = Image.open(f'input/{imagem_manipulada_2}')

    #nova_img = subtracao(img_1, img_2, offset=80)
    nova_img = multiplicacao(img_1, img_2)
    
    # Salva a nova imagem
    try:
        nova_img.save(f'output/imagem_nova.png')
        print('Imagem salva')
    except:
        print('Erro ao salvar a imagem')


if __name__ == '__main__':
    main()