from PIL import Image


def filtro_media(img):
    largura, altura = img.size

    nova_img = Image.new("RGB", (largura, altura))
    pixels = img.load()
    novos_pixels = nova_img.load()

    for x in range(largura):
        novos_pixels[x, 0] = (0, 0, 0)
        novos_pixels[x, altura - 1] = (0, 0, 0)
    
    for x in range(altura):
        novos_pixels[0, x] = (0, 0, 0)
        novos_pixels[largura - 1, x] = (0, 0, 0)

    for x in range(1, largura - 1):
        for y in range(1, altura - 1):
            pixel11 = pixels[x - 1, y - 1][0]
            pixel12 = pixels[x, y - 1][0]
            pixel13 = pixels[x + 1, y - 1][0]
            pixel21 = pixels[x - 1, y][0]
            pixel22 = pixels[x, y][0]
            pixel23 = pixels[x + 1, y][0]
            pixel31 = pixels[x - 1, y + 1][0]
            pixel32 = pixels[x, y + 1][0]
            pixel33 = pixels[x + 1, y + 1][0]
            novo_r = int((pixel11 + pixel12 + pixel13 + pixel21 + pixel22 + pixel23 + pixel31 + pixel32 + pixel33) / 9)

            pixel11 = pixels[x - 1, y - 1][1]
            pixel12 = pixels[x, y - 1][1]
            pixel13 = pixels[x + 1, y - 1][1]
            pixel21 = pixels[x - 1, y][1]
            pixel22 = pixels[x, y][1]
            pixel23 = pixels[x + 1, y][1]
            pixel31 = pixels[x - 1, y + 1][1]
            pixel32 = pixels[x, y + 1][1]
            pixel33 = pixels[x + 1, y + 1][1]
            novo_g = int((pixel11 + pixel12 + pixel13 + pixel21 + pixel22 + pixel23 + pixel31 + pixel32 + pixel33) / 9)

            pixel11 = pixels[x - 1, y - 1][2]
            pixel12 = pixels[x, y - 1][2]
            pixel13 = pixels[x + 1, y - 1][2]
            pixel21 = pixels[x - 1, y][2]
            pixel22 = pixels[x, y][2]
            pixel23 = pixels[x + 1, y][2]
            pixel31 = pixels[x - 1, y + 1][2]
            pixel32 = pixels[x, y + 1][2]
            pixel33 = pixels[x + 1, y + 1][2]
            novo_b = int((pixel11 + pixel12 + pixel13 + pixel21 + pixel22 + pixel23 + pixel31 + pixel32 + pixel33) / 9)

            novos_pixels[x, y] = (novo_r, novo_g, novo_b)

    return nova_img

def main():
    imagens = {'radiação': 'radiacao.jpg', 'gato': 'gato.jpg', 'aguia': 'aguia.jpg', 'superman':'superman.png',
               'raiox': 'raiox.jpeg', 'moedas': 'moedas.jpg', 'objetos': 'objetos.jpg'}

    imagem_manipulada = imagens['aguia']

    img = Image.open(f"input/{imagem_manipulada}")

    nova_img = filtro_media(img)
    
    # Salva a nova imagem
    try:
        nova_img.save(f'output/{imagem_manipulada}')
        print('Imagem salva')
    except:
        print('Erro ao salvar a imagem')


if __name__ == '__main__':
    main()