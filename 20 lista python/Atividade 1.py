print("--- SISTEMA DE VERIFICAÇÃO DE IDADE ---")

# Recebe a entrada do usuário
entrada = input("Digite a idade do estudante: ")

# Remove espaços em branco nas pontas
entrada_limpa = entrada.strip()

try:
    # Tenta converter a string para número inteiro
    idade = int(entrada_limpa)
    
    # Validação lógica: idade não pode ser zero, negativa ou absurda
    if idade <= 0:
        print("Erro: A idade deve ser um número maior que zero.")
    elif idade > 120:
        print("Erro: Idade inválida (limite máximo excedido).")
    else:
        # Se passou em todas as validações, a idade é válida
        print(f"Idade {idade} anos registrada com sucesso!")
        
        # Exemplo de regra da atividade (ex: atividade para maiores de 12 anos)
        if idade >= 12:
            print("Resultado: O estudante PODE participar da atividade.")
        else:
            print("Resultado: O estudante NÃO PODE participar (idade insuficiente).")

except ValueError:
    # Executado se o usuário digitou letras, símbolos ou deixou vazio
    if entrada_limpa == "":
        print("Erro: A entrada não pode estar vazia. Por favor, digite um número.")
    else:
        print("Erro: Entrada inválida! Digite apenas números inteiros (sem letras ou símbolos).")
      
