# 1) Solicita ao usuário que digite seu nome

nome = input("Digite seu nome: ")

# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante

salario = float(input("Digite seu salário: "))

# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante

bonus_recebido = float(input("Digite o valor do bônus recebido: "))

# 4) Calcule o valor do bônus final

kpi = 1000

valor_do_bonus = kpi + salario * bonus_recebido

# 5) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus

print(f"O usuário {nome} possui o bonus de {valor_do_bonus}")

# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?