def classificar_desempenho():
    print("--- Classificador de Desempenho Escolar ---")
    
    # Entrada simulando nota já validada entre 0 e 10
    nota = float(input("Digite a nota do aluno: "))
    
    # Estrutura condicional corrigida e coerente (sem brechas nas fronteiras)
    if nota < 5.0:
        desempenho = "Insuficiente"
    elif nota < 7.0:   # Captura automaticamente de 5.0 até 6.99
        desempenho = "Regular"
    elif nota < 9.0:   # Captura automaticamente de 7.0 até 8.99
        desempenho = "Bom"
    else:              # Captura automaticamente de 9.0 até 10.0
        desempenho = "Excelente"
        
    print(f"Nota: {nota:.1f} | Classificação: {desempenho}")

# Executa o programa
classificar_desempenho()
