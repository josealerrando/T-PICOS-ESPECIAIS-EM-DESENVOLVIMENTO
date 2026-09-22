def consultar_aluno():
    # Lista com 3 alunos (Índices válidos: 0, 1 e 2)
    alunos = ["Ana", "Bruno", "Carlos"]
    tamanho = len(alunos)
    
    print("--- Consulta de Alunos ---")
    print(f"Existem {tamanho} alunos cadastrados (Posições válidas: 0 a {tamanho - 1}).")
    
    # Solicita a posição desejada
    indice = int(input("Digite o número da posição que deseja consultar: "))
    
    # Validação para impedir o erro de índice inexistente
    if 0 <= indice < tamanho:
        # Se estiver no intervalo correto, exibe o aluno
        aluno_encontrado = alunos[indice]
        print(f"Aluno na posição {indice}: {aluno_encontrado}")
    else:
        # Se estiver fora do intervalo, impede o travamento do sistema
        print(f"Erro: A posição {indice} é inválida! Escolha um número entre 0 e {tamanho - 1}.")

# Executa a função
consultar_aluno()
