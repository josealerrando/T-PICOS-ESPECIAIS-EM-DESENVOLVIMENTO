def validar_e_calcular_preco(entrada_preco):
    # Passo 2: Remove espaços em branco nas pontas (.strip())
    preco_limpo = entrada_preco.strip()
    
    # Passo 3: Verifica se o campo ficou vazio
    if preco_limpo == "":
        return "Erro: O preço do produto não foi informado (campo vazio)."
        
    # Passo 4 e 5: Tenta converter e calcular
    try:
        preco_num = float(preco_limpo)
        
        if preco_num < 0:
            return "Erro: O preço não pode ser um valor negativo."
            
        # Exemplo de cálculo: simulando um acréscimo de 10% de imposto
        preco_final = preco_num * 1.10
        return f"Sucesso! Preço final calculado (com 10% de taxa): R$ {preco_final:.2f}"
        
    except ValueError:
        return "Erro: O valor digitado é inválido. Insira apenas números."

# Bloco de execução interativa (Ponto para uso)
if __name__ == "__main__":
    print("--- VALIDADOR DE PREÇOS DE PRODUTOS ---")
    
    entrada_usuario = input("Digite o preço do produto para cálculo:\n> ")
    
    # Executa a validação e exibe o resultado
    resultado_analise = validar_e_calcular_preco(entrada_usuario)
    print(f"\n[Status] {resultado_analise}")
