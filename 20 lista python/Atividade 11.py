def contar_pares(n):
    i = 1
    total_pares = 0
    
    # O loop vai até o número N inclusive
    while i <= n:
        if i % 2 == 0:
            total_pares += 1
        i += 1
        
    return total_pares

# Bloco de execução interativa (Ponto para uso)
if __name__ == "__main__":
    print("--- CONTADOR DE NÚMEROS PARES ---")
    try:
        # Solicita o número ao usuário
        numero_n = int(input("Digite o valor de N: "))
        
        if numero_n < 1:
            print("Por favor, digite um número maior ou igual a 1.")
        else:
            # Calcula e mostra o resultado
            resultado = contar_pares(numero_n)
            print(f"Resultado: Existem {resultado} número(s) par(es) entre 1 e {numero_n}.")
            
    except ValueError:
        print("Erro: Você deve digitar um número inteiro válido.")
