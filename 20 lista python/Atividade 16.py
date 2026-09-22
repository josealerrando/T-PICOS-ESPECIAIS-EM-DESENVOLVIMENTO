import os

def ler_arquivo_alunos(nome_arquivo="alunos.txt"):
    try:
        # Tenta abrir o arquivo para leitura
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            conteúdo = arquivo.read()
            return True, conteúdo
            
    except FileNotFoundError:
        # Captura especificamente a exceção de arquivo ausente
        return False, None

# Bloco de execução interativa (Ponto para uso)
if __name__ == "__main__":
    print("--- LEITOR DE CADASTRO DE ALUNOS ---")
    arquivo_alvo = "alunos.txt"
    
    # Executa o teste de leitura protegido
    sucesso, dados = ler_arquivo_alunos(arquivo_alvo)
    
    if sucesso:
        print(f"\n✅ Arquivo '{arquivo_alvo}' aberto com sucesso!")
        print("--- Conteúdo do Arquivo ---")
        if dados.strip() == "":
            print("[O arquivo está vazio]")
        else:
            print(dados)
    else:
        # Orientação clara ao usuário sobre o problema detectado
        print(f"\n⚠️ Ocorreu uma exceção: FileNotFoundError")
        print(f"O arquivo '{arquivo_alvo}' não foi encontrado no diretório atual.")
        print(f"Diretório atual de busca: {os.getcwd()}")
        
        # Ação corretiva interativa
        opcao = input(f"\nDeseja criar o arquivo '{arquivo_alvo}' agora? (s/n): ").strip().lower()
        if opcao == 's':
            with open(arquivo_alvo, "w", encoding="utf-8") as arquivo:
                arquivo.write("Ana Silva\nBruno Souza\n") # Dados iniciais de exemplo
            print(f"✅ Arquivo '{arquivo_alvo}' criado com sucesso! Execute o programa novamente.")
        else:
            print("Operação encerrada pelo usuário.")
