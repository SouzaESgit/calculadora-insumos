import os 
 # A primeira função calcula a área base em metros quadrados:
def calcular_area_base(largura, comprimento):
    return largura * comprimento

# A segunda função calcula a quantidade de sacas de sementes necessárias:
def calcular_sementes(populacao, germinacao, hectares, sementes_por_saca):
    qtd_total_sementes = ((populacao * 100) / germinacao) * 1.1
    sacas_por_hectare = qtd_total_sementes / sementes_por_saca
    return sacas_por_hectare * hectares

 # Função para calcula semente de soja:
def seedsoja(espacamento, populacao, germinacao, hec):
    espaco_cm = espacamento/100
    hect_metros = hec * 10000
    metros_linea = hect_metros * espaco_cm
    plantas_metros = populacao / metros_linea
    germina = (plantas_metros * 100) / germinacao
    qtd_semente = ((populacao*100)/germinacao)*1.1
    sacas = qtd_semente / 300000
    sacas02 = hect_metros*sacas
    return sacas02  

# Menu principal
def menu_principal():
    os.system("cls" if os.name == "nt" else "clear")
    print("--- CALCULADORA AGRÍCOLA ---")
    print("1 - Calcular Área")
    print("2 - Calcular Sementes")
    print("0 - Sair")
    return input("\nEscolha uma opção: ")


# Sistema while onde permite a pessoa escolher as opções do menu
while True:
    opcao = menu_principal()

    if opcao == "1":
        print("\n[ CÁLCULO DE ÁREA ]")
        largura = float(input("Qual a largura (m)? "))
        comprimento = float(input("Qual o comprimento (m)? "))
        area_m2 = calcular_area_base(largura, comprimento)
        
        #Os resultados dos calculos de area: 

        print(f"Hectares: {area_m2/10000:.2f}")
        print(f"Alqueire Paulista: {area_m2/24200:.2f}")
        print(f"Alqueire Mineiro: {area_m2/48400:.3f}")
        print(f"Alqueire Baiano: {area_m2/96800:.3f}")

        input("\nPressione Enter para voltar ao menu...")
#Caso a opção 2 seja selecionada sera enviada a uma pagina para escolher o tipo de semente:
    elif opcao == "2":
        print("\n[ CÁLCULO DE SEMENTES ]")
        print("1 - Milho | 2 - Soja")
        tipo_semente = input("Qual semente? ")
        
        if tipo_semente in ["1", "2"]:
            pop = float(input("População desejada (plantas/ha): "))
            germ = float(input("Taxa de germinação (%): "))
            hec = float(input("Quantos hectares? "))
            espacamento = float(input("Qual o espaçamento entre sementes?Em centímetros(cm) "))
            #
            #A saca de milho tem 60.000 sementes em media e a de soja 300.000 sementes em media
            por_saca = 60000 if tipo_semente == "1" else 300000
            nome = "Milho" if tipo_semente == "1" else "Soja"
            n = 1 
            p = 0.5
            k = 0.5
            # Se o valor for 1 ele fara o calculo para milho se for 2 para soja assim como a resposta do nome e da quantidade por saca
            total_sacas = calcular_sementes(pop, germ, hec, por_saca)
            totaladubo = (total_sacas * n) + (total_sacas * p) + (total_sacas * k )
            print(f"\n>>> Você precisará de {total_sacas:.2f} sacas de {nome}.")
            print(f"\n>>> Você precisará de {totaladubo:.2f} sacas de adubo NPK para {nome}.")
#caso a opção seja inválida ele retornara uma mensagem de erro
        else:
            print("Opção de semente inválida.")
        input("\nPressione Enter para voltar ao menu...")
# Caso a opção 0 seja selecionada o sistema encerrará
    elif opcao == "0":
        print("Saindo...")
        break #onde ocorre a quebra do loop
    else:
        print("Opção inválida!")
        input("\nPressione Enter...")