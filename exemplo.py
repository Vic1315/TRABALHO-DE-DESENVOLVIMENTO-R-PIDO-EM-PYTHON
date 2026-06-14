def linhas(caminho: str, modo: str) -> list:
    arquivo = open(caminho, modo)
    linhas = arquivo.readlines()
    arquivo.close()
    return linhas

def exibe(lista: list) -> None:
    for i, linha in enumerate(lista, start=1):
        print(f'Linha {i}: {linha}')

if __name__ == "__main__":
    caminho_local = "Aula03/nomes.txt"
    modos = ["a", "r", "w"]
    lista = linhas(caminho_local, modos[1])
    exibe(lista)
