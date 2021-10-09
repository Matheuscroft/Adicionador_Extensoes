import os

path = input("Cole o caminho da pasta onde estão os arquivos sem extensão: ")
print(path)
extensao = input("Digite a extensão desejada. Ex: .py: ")

def alteraNome():
    novo_nome = nome + extensao
    os.rename(path + "\\" + nome, path + "\\" + novo_nome)
    print("Arquivo " + nome + " alterado para " + novo_nome+"\n")

for nome in os.listdir(path):

    dados = str(nome).split(".")

    if(len(dados) > 1):
        print("Arquivo " + nome + " já tem extensão.\n")
    else:
        print("Tem um arquivo chamado "+ nome + ". Nesse eu vou adicionar a extensão.\n")
        alteraNome()

input("Pressione Enter para finalizar...")