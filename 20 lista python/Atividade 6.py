def sistema_autenticacao():
    SENHA_CORRETA = "Escola123"
    TENTATIVAS_MAXIMAS = 3
    tentativa_atual = 1
    
    print("--- Portal Escolar - Login ---")
    
    # Laço para limitar a quantidade de tentativas
    while tentativa_atual <= TENTATIVAS_MAXIMAS:
        senha_digitada = input(f"Tentativa [{tentativa_atual}/{TENTATIVAS_MAXIMAS}] - Digite a senha: ")
        
        # Validação da senha
        if senha_digitada == SENHA_CORRETA:
            print("\nAcesso liberado! Bem-vindo ao sistema escolar.")
            break # Interrompe o laço imediatamente
        else:
            tentativas_restantes = TENTATIVAS_MAXIMAS - tentativa_atual
            if tentativas_restantes > 0:
                print(f"Senha incorreta! Você ainda tem {tentativas_restantes} tentativa(s).\n")
            
            tentativa_atual += 1
            
    # Se o laço terminou e o contador passou do limite, o acesso é bloqueado
    if tentativa_atual > TENTATIVAS_MAXIMAS:
        print("\n[BLOQUEADO] Excesso de tentativas. Procure a secretaria da escola.")

# Executa o sistema
sistema_autenticacao()
