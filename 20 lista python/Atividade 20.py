# CÓDIGO COM BUGS PROPOSITAIS (NÃO UTILIZAR EM PRODUÇÃO)
def cadastrar_com_erros():
    print("--- CADASTRO ACADÊMICO (VERSÃO BUGADA) ---")
    
    # 1. Problema de Validação: Não checa se o nome está vazio
    nome = input("Nome do aluno: ") 
    
    # 2. Problema de Entrada/Exceção: Se digitar letras, o programa quebra
    idade = int(input("Idade:")) 
    
    print("Digite as 3 notas:")
    n1 = float(input("Nota 1: "))
    n2 = float(input("Nota 2: "))
    n3 = float(input("Nota 3: "))
    
    # 3. Erro de Lógica: Erro de precedência de operadores matemáticos
    media = n1 + n2 + n3 / 3 
    
    # 4. Condição de Fronteira Incorreta: Quem tira 7.0 cai na recuperação injustamente
    if media > 7.0:
        situacao = "Aprovado"
    else:
        situacao = "Recuperação"
        
    print(f"\nAluno: {nome} | Média Calculada: {media} | Situação: {situacao}")

if __name__ == "__main__":
    cadastrar_com_erros()
