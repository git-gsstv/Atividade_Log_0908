def tituloEleitor(idade):
    if idade >= 16:
        return "você está apto(a) a votar nas eleições deste ano."
    else:
        return "você NÃO está apto(a) a votar nas eleições deste ano."

nome = input("Digite seu nome: ")    
idade = int(input("Digite sua idade: "))
print(f'{nome},',tituloEleitor(idade))