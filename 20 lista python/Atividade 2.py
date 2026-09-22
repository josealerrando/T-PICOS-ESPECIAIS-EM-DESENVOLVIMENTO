from datetime import datetime, timedelta

# Banco de dados de livros (fixo para o teste)
livros = {
    "1": ["Algoritmos", True], 
    "2": ["Cálculo I", False]
}

# Banco de dados de alunos (começa vazio)
alunos = {}

print("=== SISTEMA DE BIBLIOTECA UNIVERSITÁRIA ===")

while True:
    print("\n==================================================")
    print(" 🚪 TELA INICIAL / ACESSO")
    print("==================================================")
    print("1. Cadastrar Novo Aluno (Primeira Vez)")
    print("2. Entrar na Conta (Já Possui Registro)")
    print("3. Sair do Sistema")
    print("--------------------------------------------------")
    print("💡 [Dica]: Digite 'admin' para abrir o Painel Dev")
    print("==================================================")
    
    opcao_inicial = input("\nEscolha uma opção: ").strip()
    
    if opcao_inicial == "3":
        break
        
    # --- PAINEL DO DESENVOLVEDOR (SENHA SEGRETA) ---
    elif opcao_inicial.lower() == "admin":
        senha = input("Digite a senha do desenvolvedor: ").strip()
        if senha != "admin":
            print("❌ Senha incorreta!"); continue
            
        while True:
            print("\n⚙️ PAINEL DO DESENVOLVEDOR (EDITAR CENÁRIOS)")
            print("1. Listar Alunos e Editar Pendências (Multa/Livros)")
            print("2. Voltar para a Tela Inicial")
            
            op_dev = input("\nEscolha uma opção: ").strip()
            if op_dev == "2": break
            
            elif op_dev == "1":
                print("\n📋 ALUNOS NO BANCO DE DADOS:")
                if not alunos: 
                    print("❌ Nenhum aluno cadastrado no sistema ainda. Cadastre um na tela inicial primeiro.")
                    continue
                
                for m, d in alunos.items():
                    print(f"  • Matrícula: {m} | Nome: {d[0]} | Multa: {d[1]} | Livros em posse: {d[2]}/5")
                
                matr_edit = input("\nDigite a matrícula do aluno que deseja EDITAR: ").strip()
                if matr_edit not in alunos:
                    print("❌ Matrícula não encontrada!"); continue
                
                print(f"\n✏️ Editando status de: {alunos[matr_edit][0]}")
                multa = input("Definir multa pendente para este aluno? (S/N): ").strip().upper() == "S"
                qtd = int(input("Alterar quantidade de livros em posse dele para quanto? (0 a 5): "))
                
                # Salva as alterações mantendo o nome original do aluno
                alunos[matr_edit][1] = multa
                alunos[matr_edit][2] = qtd
                print(f"✅ Status do aluno atualizado com sucesso!")
                    
    # --- FLUXO DE CADASTRO NORMAL (Aluno Regular) ---
    elif opcao_inicial == "1":
        print("\n📝 NOVO CADASTRO DE ALUNO")
        matr = input("Defina o número da sua Matrícula (Código): ").strip()
        
        if matr in alunos:
            print("❌ Esta matrícula já está cadastrada no sistema!")
            continue
            
        nome = input("Digite o seu nome completo: ").strip()
        
        # Aluno se cadastrando sozinho sempre entra zerado e regular
        alunos[matr] = [nome, False, 0]
        print(f"\n✅ Aluno '{nome}' cadastrado! Agora você já pode entrar na conta.")
        
    # --- FLUXO DE LOGIN (Entrar no Registro) ---
    elif opcao_inicial == "2":
        if not alunos:
            print("\n⚠️ Nenhum aluno cadastrado no sistema ainda."); continue
            
        print("\n🔑 ENTRAR NO SEU REGISTRO")
        matr = input("Digite o código da sua matrícula: ").strip()
        
        if matr not in alunos:
            print("❌ Código de matrícula não encontrado!"); continue
            
        # --- ÁREA LOGADA DO ALUNO ---
        nome, tem_multa, qtd_livros = alunos[matr]
        
        while True:
            # Atualiza as variáveis locais caso o admin tenha mudado elas no fundo
            nome, tem_multa, qtd_livros = alunos[matr]
            
            print(f"\n--------------------------------------------------")
            print(f"👤 CONTA LOGADA: {nome}")
            print(f"📊 Livros em posse: {qtd_livros}/5 | Possui Multa: {'Sim ❌' if tem_multa else 'Não ✅'}")
            print(f"--------------------------------------------------")
            print("1. Solicitar Empréstimo de Livro")
            print("2. Desconectar / Sair da Conta")
            
            opcao_menu = input("\nEscolha uma opção: ").strip()
            
            if opcao_menu == "2":
                print("🚪 Desconectando da conta...")
                break
                
            elif opcao_menu == "1":
                # Validações das Regras de Negócio e Fluxos Alternativos
                if tem_multa:
                    print("\n❌ Empréstimo Bloqueado: Você possui multa diária pendente.")
                    continue
                if qtd_livros >= 5:
                    print("\n❌ Empréstimo Bloqueado: Limite máximo de 5 livros atingido.")
                    continue
                    
                # Exibe catálogo
                print("\n📚 LIVROS NO CATÁLOGO:")
                for cod, dados in livros.items():
                    status = "Disponível" if dados[1] else "Indisponível"
                    print(f"  [{cod}] {dados[0]} - ({status})")
                    
                cod = input("\nDigite o código do livro desejado: ").strip()
                if cod not in livros:
                    print("❌ Código de livro inválido!"); continue
                    
                titulo, disponivel = livros[cod]
                
                # Fluxo Alternativo 2A: Livro Indisponível -> Fila de Espera
                if not disponivel:
                    print(f"\n⚠️ O livro '{titulo}' está indisponível.")
                    if input("Deseja entrar na fila de espera? (S/N): ").upper() == "S":
                        print(f"✅ Sucesso! Você foi inserido na fila de espera de '{titulo}'.")
                    continue
                    
                # Fluxo Principal: Registro do Empréstimo
                if input(f"Confirmar empréstimo de '{titulo}'? (S/N): ").upper() == "S":
                    alunos[matr][2] += 1  # Aumenta no banco de dados simulado
                    livros[cod][1] = False # Torna o livro indisponível
                    
                    data_dev = (datetime.now() + timedelta(days=7)).strftime("%d/%m/%Y")
                    print(f"\n✅ EMPRÉSTIMO REGISTRADO!")
                    print(f"Livro: {titulo} | Devolução até: {data_dev}.")
                else:
                    print("❌ Operação cancelada.")
            else:
                print("❌ Opção inválida.")
    else:
        print("❌ Opção inválida.")

print("\n👋 Sistema encerrado.")
