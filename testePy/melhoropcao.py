#Esse código visará apresentar a melhor opção de compra quando o mesmo porduto em diferentes proporções estiver disponíveis 

def calcular_custo_por_qnt(quantidade, valor):
    return valor / quantidade

# Solicita os dados do primeiro produto
quantidade_produto1 = float(input("Digite a quantidade do primeiro produto: "))
valor_produto1 = float(input("Digite o valor do primeiro produto (em reais): "))

# Solicita os dados do segundo produto
quantidade_produto2 = float(input("Digite a quantidade do segundo produto: "))
valor_produto2 = float(input("Digite o valor do segundo produto (em reais): "))

# Calcula o custo por qnt para cada produto
custo_por_qnt_produto1 = calcular_custo_por_qnt(quantidade_produto1, valor_produto1)
custo_por_qnt_produto2 = calcular_custo_por_qnt(quantidade_produto2, valor_produto2)

# Compara os custos e exibe a melhor opção
if custo_por_qnt_produto1 < custo_por_qnt_produto2:
    print(f"A opção 1 é mais vantajosa: custo por qnt = R$ {custo_por_qnt_produto1:.2f}")
else:
    print(f"A opção 2 é mais vantajosa: custo por qnt = R$ {custo_por_qnt_produto2:.2f}")
