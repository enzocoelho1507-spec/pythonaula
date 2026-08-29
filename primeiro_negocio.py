print("Meu primeiro programa aplicado a negócios")

# Dados
produto = "Notebook"
preco = 3500.00
quantidade = 4
cliente_ativo = True
percentual_desconto = 10
percentual_comissao = 4
custo_unitario = 2600

# Processamento
total_venda = preco * quantidade
valor_desconto = total_venda * percentual_desconto / 100
valor_final = total_venda - valor_desconto
valor_comissao = valor_final * percentual_comissao / 100
custo_total = custo_unitario * quantidade
lucro_bruto = valor_final - custo_total

# Saída
print("Produto:", produto)
print("Preço unitário:", preco)
print("Quantidade:", quantidade)
print("Total da venda:", total_venda)
print("Desconto:", valor_desconto)
print("Valor final:", valor_final)
print("Comissão:", valor_comissao)
print("Custo total:", custo_total)
print("Lucro bruto:", lucro_bruto)