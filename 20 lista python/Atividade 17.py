from datetime import datetime

# Banco de dados em memória para armazenar os alunos válidos
banco_dados_alunos = []

def validar_dados_aluno(nome, idade, curso, ano):
    """Função interna que valida todos os critérios de aceitação"""
    erros = []
    ano_atual = datetime.now().year
    
    if not nome.strip():
        erros.append("O nome do aluno não pode ficar vazio.")
    if idade <= 0 or idade > 120:
        erros.append(f"Idade inválida ({idade}). Deve estar entre 1 e 120 anos.")
    if not curso.strip():
        erros.append("O curso não pode ficar vazio.")
    if ano < 1900 or ano > ano_atual:
        erros.append(f"Ano inválido ({ano}). Deve estar entre 1900 e {ano_atual}.")
        
    if erros:
        return False, erros
    return True, "Dados validados com sucesso!"

def menu_cadastro():
    while True:
        print("\n=======================================")
        print("    SISTEMA DE CADASTRO ACADÊMICO")
        print("=======================================")
        print("1. Cadastrar Novo Aluno")
        print("2. Listar Alunos Cadastrados")
        print("3. Sair do Sistema")
        print("=======================================")
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1":
            print("\n--- NOVO CADASTRO ---")
            nome = input("Nome do Aluno: ").strip()
            
            # Captura protegida da idade
            try:
                idade = int(input("Idade: "))
            except ValueError:
                print("❌ Erro: A idade deve ser um número inteiro. Cadastro cancelado.")
                continue
                
            curso = input("Curso: ").strip()
            
            # Captura protegida do ano
            try:
                ano = int(input("Ano de Ingresso: "))
            except ValueError:
                print("❌ Erro: O ano deve ser um número inteiro. Cadastro cancelado.")
                continue
            
            # Executa a validação antes de aceitar
            valido, resultado = validar_dados_aluno(nome, idade, curso, ano)
            
            if valido:
                # Se válido, monta o dicionário e salva na lista
                novo_aluno = {
                    "nome": nome.title(),
                    "idade": idade,
                    "curso": curso.title(),
                    "ano": ano
                }
                banco_dados_alunos.append(novo_aluno)
                print(f"\n✅ Sucesso: {resultado}")
                print(f"Aluno(a) '{novo_aluno['nome']}' foi adicionado(a) ao sistema.")
            else:
                print("\n❌ Cadastro Rejeitado! Erros encontrados:")
                for erro in resultado:
                    print(f" -> {erro}")
                    
        elif opcao == "2":
            print("\n--- ALUNOS CADASTRADOS ---")
            if not banco_dados_alunos:
                print("Nenhum aluno cadastrado até o momento.")
            else:
                for i, aluno in enumerate(banco_dados_alunos, 1):
                    print(f"{i}. Nome: {aluno['nome']} | Idade: {aluno['idade']} | Curso: {aluno['curso']} | Ano: {aluno['ano']}")
                    
        elif opcao == "3":
            print("\nEncerrando o sistema. Até logo!")
            break
        else:
            print("❌ Opção inválida! Escolha 1, 2 ou 3.")

# Ponto de uso para execução imediata
if __name__ == "__main__":
    menu_cadastro()
