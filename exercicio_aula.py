nome_produto = input("Digite o nome do produto: ")
preco_produto = float(input("Digite o preço do produto: "))
quantidade_vendida = int(input("Digite a quantidade vendida: "))

total_vendas = preco_produto * quantidade_vendida

print(f"O total de vendas do produto {nome_produto} é: R$ {total_vendas:.2f}")
print(f"O preço do produto {nome_produto} é: R$ {preco_produto:.2f}")
print(f"A quantidade vendida do produto {nome_produto} é: {quantidade_vendida}")
