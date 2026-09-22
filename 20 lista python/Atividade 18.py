def calcular_compra_com_desconto(valor_compra):
    # Validação preliminar para valores inesperados (negativos)
    if valor_compra < 0:
        return "Erro: O valor da compra não pode ser negativo."
        
    # Aplicação estrita da regra de negócio
    if valor_compra > 100.00:
        valor_final = valor_compra * 0.90  # 10% de desconto
    else:
        valor_final = valor_compra  # Sem desconto para até R$ 100.00
        
    return round(valor_final, 2)

# Bloco de execução interativa e automação dos testes de caixa-preta
if __name__ == "__main__":
    print("--- SIMULADOR DE TESTES: CAIXA-PRETA ---")
    
    # Matriz de Casos de Teste (Entrada, Categoria, Resultado Esperado)
    casos_teste = [
        {"entrada": 50.00,  "categoria": "Normal (Até R$ 100)",      "esperado": 50.00},
        {"entrada": 150.00, "categoria": "Normal (Acima de R$ 100)",  "esperado": 135.00},
        {"entrada": 100.00, "categoria": "Fronteira (Limite Exato)",  "esperado": 100.00},
        {"entrada": 100.01, "categoria": "Fronteira (Início Desconto)","esperado": 90.01},
        {"entrada": 0.00,   "categoria": "Fronteira (Valor Zero)",    "esperado": 0.00},
        {"entrada": -20.00, "categoria": "Inesperado (Negativo)",     "esperado": "Erro: O valor da compra não pode ser negativo."}
    ]
    
    # Execução e exibição comparativa dos testes
    print(f"{'CATEGORIA':<28} | {'ENTRADA':<8} | {'ESPERADO':<15} | {'OBTIDO':<15} | STATUS")
    print("-" * 80)
    
    for caso in casos_teste:
        resultado_obtido = calcular_compra_com_desconto(caso["entrada"])
        status = "✅ OK" if resultado_obtido == caso["esperado"] else "❌ FALHA"
        
        # Formatação de exibição de valores textuais ou numéricos
        esp = f"R$ {caso['esperado']:.2f}" if isinstance(caso['esperado'], (int, float)) else caso['esperado']
        obt = f"R$ {resultado_obtido:.2f}" if isinstance(resultado_obtido, (int, float)) else resultado_obtido
        
        print(f"{caso['categoria']:<28} | R$ {caso['entrada']:<5.2f} | {esp:<15} | {obt:<15} | {status}")

    # Menu interativo opcional para uso livre
    print("\n--- TESTE MANUAL ---")
    try:
        usuario_valor = float(input("Digite um valor de compra para testar o sistema: R$ "))
        print(f"Resultado do processamento: {calcular_compra_com_desconto(usuario_valor)}")
    except ValueError:
        print("Resultado do processamento: Erro: Entrada inválida (deve ser um número).")
