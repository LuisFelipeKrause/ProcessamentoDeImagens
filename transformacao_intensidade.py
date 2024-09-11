from PIL import Image


def transformar_negativa(img):
    largura, altura = img.size

    nova_img = Image.new("RGB", (largura, altura))
    pixels = img.load()
    novos_pixels = nova_img.load()

    for x in range(largura):
        for y in range(altura):
            if pixels[x, y] < (127, 127, 127):
                novos_pixels[x, y] = (255, 255, 255)
            elif pixels[x, y] >= (127, 127, 127):
                novos_pixels[x, y] = (0, 0, 0)
    
    return nova_img


def main():
    imagens = {'radiação': 'radiacao.jpg', 'gato': 'gato.jpg', 'aguia': 'aguia.jpg', 
               'raiox': 'raiox.jpeg', 'moedas': 'moedas.jpg', 'pessoas': 'pessoas.jpg', 'objetos': 'objetos.jpg'}

    imagem_manipulada = imagens['raiox']

    img = Image.open(f"input/{imagem_manipulada}")

    nova_img = transformar_negativa(img)
    
    # Salva a nova imagem
    try:
        nova_img.save(f'output/{imagem_manipulada}')
        print('Imagem salva')
    except:
        print('Erro ao salvar a imagem')


if __name__ == '__main__':
    main()