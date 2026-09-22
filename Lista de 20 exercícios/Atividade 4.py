def calcular_media():
    print("--- Sistema de Cálculo de Média ---")
    
    # Solicita a quantidade de notas
    quantidade = int(input("Digite a quantidade de notas: "))

    # Validação para impedir a divisão por zero
    if quantidade == 0:
        print("Erro: A quantidade de notas não pode ser zero. Operação cancelada.")
    elif quantidade < 0:
        print("Erro: A quantidade de notas não pode ser negativa.")
    else:
        # Se a quantidade for válida, o programa prossegue
        nota1 = float(input("Digite a primeira nota: "))
        nota2 = float(input("Digite a segunda nota: "))
        
        soma = nota1 + nota2
        media = soma / quantidade
        
        print(f"Soma das notas: {soma}")
        print(f"A média final é: {media:.2f}")

# Executa a função
calcular_media()def calcular_media():
    print("--- Sistema de Cálculo de Média ---")
    
    # Solicita a quantidade de notas
    quantidade = int(input("Digite a quantidade de notas: "))

    # Validação para impedir a divisão por zero
    if quantidade == 0:
        print("Erro: A quantidade de notas não pode ser zero. Operação cancelada.")
    elif quantidade < 0:
        print("Erro: A quantidade de notas não pode ser negativa.")
    else:
        # Se a quantidade for válida, o programa prossegue
        nota1 = float(input("Digite a primeira nota: "))
        nota2 = float(input("Digite a segunda nota: "))
        
        soma = nota1 + nota2
        media = soma / quantidade
        
        print(f"Soma das notas: {soma}")
        print(f"A média final é: {media:.2f}")

# Executa a função
calcular_media()
