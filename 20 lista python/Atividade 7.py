def validar_estrutura_cpf():
    print("--- Validador Estrutural de CPF ---")
    entrada = input("Digite o CPF (apenas números ou formatado): ")
    
    # 1. Tratamento e Limpeza (remove pontos e traços comuns)
    cpf_limpo = entrada.replace(".", "").replace("-", "").strip()
    
    # 2. Validação Estrutural
    if not cpf_limpo.isdigit():
        # Se contiver letras ou símbolos que não foram removidos na limpeza
        print(f"Erro: O identificador contém caracteres inválidos. Digite apenas números.")
    
    elif len(cpf_limpo) < 11:
        # Se for menor que o esperado
        print(f"Erro: Identificador muito curto! Possui {len(cpf_limpo)} dígitos. O correto são 11.")
        
    elif len(cpf_limpo) > 11:
        # Se for maior que o esperado
        print(f"Erro: Identificador muito longo! Possui {len(cpf_limpo)} dígitos. O correto são 11.")
        
    else:
        # Tamanho exato de 11 dígitos numéricos
        print(f"Sucesso! O identificador estrutural está correto: {cpf_limpo}")

# Executa a validação
validar_estrutura_cpf()
