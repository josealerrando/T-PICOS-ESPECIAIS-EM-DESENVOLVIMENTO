def verificar_atividade():
    # 1. Leitura da entrada de dados
    entrada = input("Digite a idade do estudante: ").strip()

    # 2. Teste de entrada vazia
    if not entrada:
        print("Erro: A entrada não pode estar vazia.")
        return

    # 3. Tentativa de conversão e validação do tipo
    try:
        idade = int(entrada)
    except ValueError:
        print("Erro: Entrada inválida. Por favor, digite um número inteiro.")
        return

    # 4. Validação de número negativo ou zero
    if idade < 0:
        print("Erro: A idade não pode ser um número negativo.")
        return
    elif idade == 0:
        print("Erro: A idade não pode ser zero.")
        return

    # 5. Fluxo normal (Idade válida) - Exemplo: atividade para maiores de 12 anos
    idade_minima = 12
    if idade >= idade_minima:
        print(f"Sucesso! Com {idade} anos, o estudante PODE participar da atividade.")
    else:
        print(f"Desculpe, com {idade} anos o estudante NÃO PODE participar (Idade mínima: {idade_minima} anos).")

# Executar a função
verificar_atividade()
