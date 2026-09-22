total_compra = 0
print("--- SISTEMA DE CAIXA AUTOMÁTICO ---")
print("Instruções: Digite o valor de cada produto. Para encerrar, digite '0' ou 'resultando'.\n")

while True:
    entrada = input("Digite o valor do produto: ")
    
    # Tratamento preliminar da entrada
    entrada_limpa = entrada.strip().lower().replace(',', '.')
    
    # Condição de parada (critério de saída do laço "infinito")
    if entrada_limpa == '0' or entrada_limpa == 'resultando':
        break
        
    try:
        # Tenta converter a entrada atual para número decimal
        preco = float(entrada_limpa)
        
        if preco < 0:
            print("Erro: O preço não pode ser negativo. Tente novamente.")
            continue
            
        # Soma o preço validado ao total da compra
        total_compra += preco
        print(f"Subtotal: R$ {total_compra:.2f}")
        
    except ValueError:
        # Se o usuário digitar letras ou símbolos inválidos, o programa não quebra
        print("Erro: Entrada inválida! Digite apenas números ou 'fim' para encerrar.")

print("\n-----------------------------------")
print(f"COMPRA FINALIZADA! Valor Total: R$ {total_compra:.2f}")
print("-----------------------------------")
