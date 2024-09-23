from PIL import Image


def transformar_negativa_RGB(img):
    largura, altura = img.size

    # Converter as imagens para o modo RGB se estiver em grayscale
    if img.mode != 'RGB':
        img = img.convert('RGB')

    nova_img = Image.new("RGB", (largura, altura))
    pixels = img.load()
    novos_pixels = nova_img.load()

    for x in range(largura):
        for y in range(altura):
            r = 255 - int(pixels[x, y][0])
            g = 255 - int(pixels[x, y][1])
            b = 255 - int(pixels[x, y][2])
            novos_pixels[x, y] = (r, g, b)
    
    return nova_img

def transformar_negativa_GS(img):
    largura, altura = img.size

    if img.mode != 'L':
        img = img.convert('L')

    nova_img = Image.new("L", (largura, altura))
    pixels = img.load()
    novos_pixels = nova_img.load()

    for x in range(largura):
        for y in range(altura):
            novos_pixels[x, y] = 255 - pixels[x, y]

    return nova_img

def main():
    imagens = {'radiação': 'radiacao.jpg', 'gato': 'gato.jpg', 'aguia': 'aguia.jpg', 'superman':'superman.png',
               'raiox': 'raiox.jpeg', 'moedas': 'moedas.jpg', 'pessoas': 'pessoas.jpg', 'objetos': 'objetos.jpg'}

    imagem_manipulada = imagens['raiox']

    img = Image.open(f"input/{imagem_manipulada}")

    nova_img = transformar_negativa_GS(img)
    
    # Salva a nova imagem
    try:
        nova_img.save(f'output/{imagem_manipulada}')
        print('Imagem salva')
    except:
        print('Erro ao salvar a imagem')


if __name__ == '__main__':
    main()