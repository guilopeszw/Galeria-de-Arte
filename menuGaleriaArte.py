import bibGaleriaArte

listaObras = [["Leonardo da Vinci", "Mona Lisa", 850000000],
              ["Vincent van Gogh", "Noite Estrelada", 100000000],
              ["Pablo Picasso", "As Senhoritas de Avignon", 140000000],
              ["Claude Monet", "Ninféias", 50000000],
              ["Salvador Dalí", "A Persistência da Memória", 60000000],
              ["Rembrandt", "A Ronda Noturna", 500000000],
              ["Michelangelo", "A Criação de Adão", 900000000],
              ["Edvard Munch", "O Grito", 120000000],
              ["Gustav Klimt", "O Beijo", 150000000],
              ["Johannes Vermeer", "A Moça com Brinco de Pérola", 70000000],
              ["Francisco Goya", "O Três de Maio de 1808", 200000000],
              ["Jackson Pollock", "Nº 5, 1948", 140000000],
              ["Andy Warhol", "Díptico de Marilyn", 200000000],
              ["Henri Matisse", "A Dança", 300000000],
              ["Georges Seurat", "Tarde de Domingo na Ilha de Grande Jatte", 650000000],
              ["Wassily Kandinsky", "Composição VII", 100000000],
              ["Paul Cézanne", "Os Jogadores de Cartas", 250000000],
              ["Grant Wood", "Gótico Americano", 50000000],
              ["Diego Velázquez", "As Meninas", 600000000],
              ["Édouard Manet", "Olympia", 60000000],
              ["Marc Chagall", "Eu e a Aldeia", 50000000],
              ["Rene Magritte", "O Filho do Homem", 100000000],
              ["Piet Mondrian", "Composição com Vermelho, Azul e Amarelo", 50000000],
              ["Caravaggio", "A Vocação de São Mateus", 150000000],
              ["Ticiano", "A Assunção da Virgem", 700000000],
              ["Jean-Michel Basquiat", "Sem Título", 110500000],
              ["Georgia O'Keeffe", "Flor Branca Nº 1", 44000000],
              ["Frida Kahlo", "Auto-retrato com Colar de Espinhos e Beija-flor", 50000000],
              ["Diego Rivera", "Homem nas Encruzilhadas", 50000000],
              ["Jan van Eyck", "O Casal Arnolfini", 150000000],
              ["Gustave Courbet", "Um Enterro em Ornans", 40000000],
              ["Edgar Degas", "A Aula de Balé", 50000000],
              ["Albrecht Dürer", "Melancolia I", 100000000],
              ["Sandro Botticelli", "O Nascimento de Vênus", 500000000],
              ["El Greco", "Vista de Toledo", 80000000],
              ["Thomas Gainsborough", "O Menino Azul", 200000000],
              ["Raphael", "A Escola de Atenas", 500000000],
              ["Camille Pissarro", "O Boulevard Montmartre à Noite", 32000000],
              ["Joan Miró", "O Campo Lavrado", 26000000],
              ["Jean Auguste Dominique Ingres", "Grande Odalisca", 250000000],
              ["Caspar David Friedrich", "Caminhante Sobre o Mar de Névoa", 100000000],
              ["Paul Gauguin", "Quando Você Vai Casar?", 300000000],
              ["Élisabeth Vigée Le Brun", "Auto-retrato com Chapéu de Palha", 40000000],
              ["Hans Holbein, o Jovem", "Os Embaixadores", 300000000],
              ["John Constable", "A Carroça de Feno", 30000000],
              ["John Singer Sargent", "Retrato de Madame X", 20000000],
              ["Winslow Homer", "Vento a Favor", 15000000],
              ["Georges Braque", "Violino e Castiçal", 20000000],
              ["Egon Schiele", "A Morte e a Donzela", 40000000],
              ["Leonardo da Vinci", "A Última Ceia", 450000000],
              ["Vincent van Gogh", "Girassóis", 39000000],
              ["Pablo Picasso", "Guernica", 200000000],
              ["Claude Monet", "Impressão, Nascer do Sol", 110000000],
              ["Salvador Dalí", "Metamorfose de Narciso", 25000000],
              ["Rembrandt", "Auto-retrato com Dois Círculos", 400000000],
              ["Michelangelo", "Davi", 1000000000],
              ["Edvard Munch", "Madonna", 50000000],
              ["Gustav Klimt", "Retrato de Adele Bloch-Bauer I", 135000000],
              ["Johannes Vermeer", "A Leiteira", 75000000],
              ["Francisco Goya", "Saturno Devorando Seu Filho", 200000000],
              ["Jackson Pollock", "Blue Poles", 200000000],
              ["Andy Warhol", "Oito Elvises", 100000000],
              ["Henri Matisse", "O Caracol", 30000000],
              ["Georges Seurat", "Banhistas em Asnières", 600000000],
              ["Wassily Kandinsky", "Improvisação 28", 200000000],
              ["Paul Cézanne", "Montanha Sainte-Victoire", 100000000],
              ["Grant Wood", "Filhas da Revolução", 30000000],
              ["Diego Velázquez", "Retrato de Inocêncio X", 300000000],
              ["Édouard Manet", "Um Bar no Folies-Bergère", 80000000],
              ["Marc Chagall", "A Crucificação Branca", 100000000],
              ["Rene Magritte", "Os Amantes", 150000000],
              ["Piet Mondrian", "Broadway Boogie Woogie", 40000000],
              ["Caravaggio", "Judite e Holofernes", 170000000],
              ["Ticiano", "Baco e Ariadne", 700000000],
              ["Jean-Michel Basquiat", "Africanos em Hollywood", 99000000],
              ["Georgia O'Keeffe", "Íris Negra III", 40000000],
              ["Frida Kahlo", "As Duas Fridas", 80000000],
              ["Diego Rivera", "Murais da Indústria de Detroit", 15000000],
              ["Jan van Eyck", "Retábulo de Ghent", 500000000],
              ["Gustave Courbet", "A Origem do Mundo", 300000000],
              ["Edgar Degas", "A Pequena Bailarina de Quatorze Anos", 100000000],
              ["Albrecht Dürer", "Cavaleiro, a Morte e o Diabo", 80000000],
              ["Sandro Botticelli", "Primavera", 400000000],
              ["El Greco", "O Despojamento de Cristo", 250000000],
              ["Thomas Gainsborough", "Mrs. Siddons", 150000000],
              ["Raphael", "Madona do Prado", 600000000],
              ["Camille Pissarro", "O Hermitage em Pontoise", 24000000],
              ["Joan Miró", "Carnaval de Arlequim", 60000000]]


def menu(listaObras):
    direcao = 1

    while direcao != 0:
        print("Aperte [1] para descobrir o nome do artista de uma obra")
        print("Aperte [2] para descobrir todas as obras de um artista")
        print("Aperte [3] para descobrir o valor de uma obra")
        print("Aperte [4] para descobrir o valor total do acervo de um artista")
        print("Aperte [5] para adicionar uma obra ao acervo")
        print("Aperte [6] para remover uma obra do acervo")
        print("Aperte [0] para sair.")
        direcao = int(input("Digite aqui: "))
        # if´s
        if direcao == 1:
            nomeObra = str(
                input("Informe o nome da obra cujo queira saber o artista: "))
            print(f"O artista da obra é: {
                  bibGaleriaArte.encontrarArtista(listaObras, nomeObra)}.")
       
        elif direcao == 2:
            nomeArtista = str(
                input("Informe o nome do artista cujo queira saber as obras: "))
            if bibGaleriaArte.obrasArtista == list:
                print(f"Todas as obras de {nomeArtista.title()} sâo: {
                    bibGaleriaArte.obrasArtista(listaObras, nomeArtista)}.")
            else:
                print(bibGaleriaArte.obrasArtista(listaObras, nomeArtista))
       
        elif direcao == 3:
            nomeObra = str(
                input("Informe o nome da obra cujo queira saber o valor: "))
            print(f"O valor da obra é: {
                  bibGaleriaArte.valorObra(listaObras, nomeObra)}.")
        
        elif direcao == 4:
            nomeArtista = str(input(
                "Informe o nome do artista cujo queira saber o valor total de seu acervo: "))
            print(f"O valor total do acervo de {nomeArtista} é R$: {
                  bibGaleriaArte.valorTotalObras(listaObras, nomeArtista):.2f}.")
       
        elif direcao == 5:
            nomeArtista = str(input("Insira o nome do(a) autor(a): ")).title()
            nomeObra = str(input("Insira o nome da obra: ")).title()
            valorObra = float(input("Insira o valor da obra: "))
            bibGaleriaArte.adicionarObra(
                listaObras, nomeArtista, nomeObra, valorObra)
            print(f"A obra {nomeObra.title()} foi adicionada ao acervo.")
        
        elif direcao == 6:
            obraDelete = str(input("Informe qual obra você deseja apagar: "))
            bibGaleriaArte.deletarObra(listaObras, obraDelete)
            print(f"A obra {obraDelete.title()} foi removida do acervo.")
      
        elif direcao >= 7:
            print("Não entendi. Tente novamente.")
        print(" ")
    return print("Obrigado por visitar nosso acervo digital!")

# menu
print("-" * 20)
print("Seja bem-vindo(a) à galeria de arte! ")
print("-" * 20)
print(" ")
menu(listaObras)