salario_fixo = float(input("Digite o salário fixo do vendedor: "))
total_vendas = float(input("Digite o total de vendas do vendedor: "))
percentual_comissao = float(input("Digite o percentual de comissão : "))

comissao = (total_vendas * percentual_comissao)/100
remuneracao_total = salario_fixo + comissao

print(f"A comissão do vendedor é: R$ {comissao:.2f}")
print(f"A remuneração total do vendedor é: R$ {remuneracao_total:.2f}")
