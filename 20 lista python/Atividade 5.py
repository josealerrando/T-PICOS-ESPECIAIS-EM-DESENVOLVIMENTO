def validar_e_classificar_nota():
    print("--- Sistema de Validação de Notas ---")
    entrada = input("Digite a nota do aluno (0 a 10): ")
    
    try:
        # 1. Trata a entrada (remove espaços e ajusta vírgula se houver)
        nota_limpa = entrada.strip().replace(",", ".")
        nota = float(nota_limpa)
        
        # 2. Valida o intervalo numérico (0 a 10)
        if nota < 0 or nota > 10:
            print(f"Erro: A nota {nota} é inválida. Digite um valor de 0 a 10.")
        else:
            # 3. Classifica a nota válida
            # Regra adotada: Reprovado (< 5) | Recuperação (5 a 6.9) | Aprovado (>= 7)
            if nota >= 7.0:
                situacao = "APROVADO(A)"
            elif nota >= 5.0:
                situacao = "EM RECUPERAÇÃO"
            else:
                situacao = "REPROVADO(A)"
                
            print(f"Nota válida: {nota:.1f} -> Situação: {situacao}")
            
    except ValueError:
        # Captura o erro caso o usuário digite palavras ou símbolos inválidos
        print(f"Erro: '{entrada}' não é uma nota válida. Use apenas números de 0 a 10.")

# Executa a função

validar_e_classificar_nota()
