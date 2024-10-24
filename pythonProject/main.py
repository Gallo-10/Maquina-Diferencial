#Gera a tabela de diferenças finitas
def diferencas_finitas(valores):
    tabela = [valores]
    for i in range(len(valores) - 1):
        nova_linha = [tabela[i][j + 1] - tabela[i][j] for j in range(len(tabela[i]) - 1)]
        tabela.append(nova_linha)
    return tabela

#Calcula o valor de um polinômio dado os coeficientes
def valor_polinomio(x, coef):
    return sum(c * x**i for i, c in enumerate(coef)) #aqui é feito a soma dos coeficientes multiplicados por x^i, onde i é o grau do coeficiente. enumerate(coef) 
                                                                        #retorna o índice e o valor do coeficiente, que é usado para calcular o valor do polinômio
                                                                        
#Função recursiva que calcula a interpolação para polinômios de qualquer grau
def interpolar_recursivo(tabela, s, grau, ordem=1):
    if ordem > grau:
        return 0
    fator = tabela[ordem][0]
    for i in range(ordem):
        fator *= (s - i) / (i + 1)
    return fator + interpolar_recursivo(tabela, s, grau, ordem + 1)

#Função que controla a interpolação e o grau do polinômio
def interpolar(tabela, x_vals, x, grau=None):
    h = x_vals[1] - x_vals[0]  # Espaçamento constante (0,1 no enunciado)
    s = (x - x_vals[0]) / h    # Fator de interpolação
    if grau is None or grau >= len(x_vals):
        grau = len(x_vals) - 1  # Grau máximo permitido
    return tabela[0][0] + interpolar_recursivo(tabela, s, grau)



# Exemplo usando valores de x com intervalo de 0.1

# x = [0, 0.1, 0.2, 0.3, 0.4, 0.5]
x_vals = [i * 0.1 for i in range(6)]      
coef = [1, 0, -1]  # Coeficientes para o polinômio
y_vals = [valor_polinomio(x, coef) for x in x_vals]

# Gerar a tabela de diferenças
tabela_dif = diferencas_finitas(y_vals)


# Exibir a tabela de diferenças com os níveis
print("Tabela de diferenças finitas:")
for nivel, linha in enumerate(tabela_dif):
    # Arredondar e substituir valores pequenos por 0
    linha_arredondada = [round(valor, 10) if abs(valor) > 1e-10 else 0.0 for valor in linha]
    print(f"Nível {nivel}: {linha_arredondada}")


# Calcular o próximo valor para x = 0.6
x_novo = 0.6
grau_2 = 2
resultado_grau_2 = interpolar(tabela_dif, x_vals, x_novo, grau_2)
print(f"\nValor interpolado para x = {x_novo} com grau 2: {resultado_grau_2:.4f}")

# Calcular valor interpolado para x = 0.9 
x_novo_geral = 0.9
resultado_geral = interpolar(tabela_dif, x_vals, x_novo_geral)
print(f"Valor interpolado para x = {x_novo_geral}: {resultado_geral:.4f}")
