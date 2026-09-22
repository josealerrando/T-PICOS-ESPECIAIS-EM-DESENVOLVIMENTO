# FUNÇÃO CORRIGIDA: Usa 'return' em vez de apenas 'print'
def calcular_media(nota1, nota2):
    media = (nota1 + nota2) / 2
    return media  # Devolve o valor para quem chamou a função

# Bloco de execução interativa (Ponto para uso)
if __name__ == "__main__":
    print("--- CALCULADORA DE MÉDIAS ---")
    
    try:
        # Recebe as notas do usuário
        n1 = float(input("Digite a primeira nota: "))
        n2 = float(input("Digite a segunda nota: "))
        
        # O programa principal captura o valor retornado pela função
        media_final = calcular_media(n1, n2)
        
        print("\n--- PROVA DE USO EM OUTROS CÁLCULOS ---")
        print(f"1. Valor guardado na memória do sistema: {media_final}")
        
        # Teste real: Usando a média para outro cálculo (Adicionando bônus de 1.0 ponto)
        media_com_bonus = media_final + 1.0
        print(f"2. Média recalculada com bônus de participação: {media_com_bonus}")
        
        # Tomando uma decisão com base no retorno
        if media_final >= 7.0:
            print("Status do aluno: Aprovado!")
        else:
            print("Status do aluno: Recuperação.")
            
    except ValueError:
        print("Erro: Digite apenas notas numéricas válidas.")
