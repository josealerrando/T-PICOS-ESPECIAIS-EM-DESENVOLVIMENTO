def calcular_media_tres_notas():
    print("--- Calculadora de Média (Correção Lógica) ---")
    
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))
    
    # ERRADO (Como o sistema antigo fazia):
    # media_errada = nota1 + nota2 + nota3 / 3
    
    # CORRETO: Os parênteses garantem que a soma aconteça antes da divisão
    media_correta = (nota1 + nota2 + nota3) / 3
    
    print("\n--- Resultados ---")
    print(f"Média calculada corretamente: {media_correta:.2f}")

# Executa o programa
calcular_media_tres_notas()
