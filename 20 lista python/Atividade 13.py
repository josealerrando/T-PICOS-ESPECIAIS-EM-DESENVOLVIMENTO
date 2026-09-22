def analisar_temperaturas(lista_temps):
    # Proteção: se a lista estiver vazia, retorna None
    if not lista_temps:
        return None, None
        
    # Inicialização correta usando o PRIMEIRO elemento da lista [0]
    maior = lista_temps[0]
    menor = lista_temps[0]
    
    # Percorre toda a lista comparando os valores
    for temp in lista_temps:
        if temp > maior:
            maior = temp
        if temp < menor:
            menor = temp
            
    return maior, menor

# Bloco de execução interativa (Ponto para uso)
if __name__ == "__main__":
    print("--- ANALISADOR DE TEMPERATURAS RURAIS (CORRIGIDO) ---")
    
    entrada = input("Digite as temperaturas separadas por espaço (ex: 23.5 -5 12 -5 30):\n> ")
    
    try:
        # Divide o texto e converte cada parte em número decimal
        temperaturas = [float(t) for t in entrada.split()]
        
        # Executa a busca manual dos extremos
        maior_temp, menor_temp = analisar_temperaturas(temperaturas)
        
        if maior_temp is None:
            print("Erro: Nenhuma temperatura válida foi digitada.")
        else:
            print("\n--- RESULTADO DA ANÁLISE ---")
            print(f"☀️ Maior temperatura registrada: {maior_temp}°C")
            print(f"❄️ Menor temperatura registrada: {menor_temp}°C")
            
    except ValueError:
        print("\n❌ Erro: Digite apenas números válidos separados por espaços. Não use letras ou vírgulas (use ponto para decimais).")
