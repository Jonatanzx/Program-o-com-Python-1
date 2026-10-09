personagem = {
    "nome": "Link",
    "classe": "Lutador",
    "nivel": 1,
    "inventario": []
}

personagem["inventario"].append(input("Digite o 1º item: "))
personagem["inventario"].append(input("Digite o 2º item: "))

print(personagem)
for item in personagem["inventario"]:
    print(item)
