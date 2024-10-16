# para encontrar o nome de um artista usando o nome de uma obra: 
def encontrarArtista(listaObras, nomeObra):
    for i in range(len(listaObras)):
        if nomeObra.lower() == listaObras[i][1].lower():
            return listaObras[i][0] 

# para encontrar o nome de todas as obras de um artista: 
def obrasArtista(listaObras, nomeArtista):
    obrasArtista = []
    for i in range(len(listaObras)):
        if nomeArtista.lower() in listaObras[i][0].lower():
            obrasArtista.append(listaObras[i][1])
        else:
            obrasArtista = "O(a) artista não tem obras no acervo."
    return obrasArtista

# para encontrar o valor de uma obra: 
def valorObra(listaObras, nomeObra):
    for i in range(len(listaObras)):
        if nomeObra.lower() == listaObras[i][1].lower():
            return listaObras[i][2]

# para descobrir o valor total do acervo de um artista
def valorTotalObras(listaObras, nomeArtista):
    valorTotal = 0
    for i in range(len(listaObras.artes)):
        if nomeArtista.lower() == listaObras[i][0].lower():
            valorTotal += listaObras[i][2]
    return valorTotal

# para adicionar uma obra ao acervo
def adicionarObra(listaObras, nomeArtista, nomeObra, valorObra):
    obra = [nomeArtista, nomeObra, valorObra]
    listaObras.append(obra)

def deletarObra(listaObras, obraDelete):
    for i in range(len(listaObras)):
        if obraDelete.lower() == listaObras[i][1].lower():
            del listaObras[i]