def ler_ate_zero():
    print("--- Coletor de Números (Loop Seguro) ---")
    
    # Lê o primeiro número antes de entrar no laço
    numero = int(input("Digite um número (ou 0 para sair): "))
    soma = 0
    
    # O laço continua enquanto o número for diferente de zero
    while numero != 0:
        soma += numero
        print(f"Número {numero} adicionado! Total acumulado: {soma}")
        
        # ATUALIZAÇÃO DA VARIÁVEL: Crucial para evitar o loop infinito!
        numero = int(input("Digite o próximo número (ou 0 para sair): "))
        
    print("\n[Encerrado] Você digitou 0. Programa finalizado com sucesso!")

# Executa o programa
ler_ate_zero()
