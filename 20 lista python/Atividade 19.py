def avaliar_credito(idade, renda, situacao_cadastral):
    # Padroniza o texto da situação cadastral
    situacao = situacao_cadastral.strip().title()
    
    # CAMINHO 1: Validação de Segurança Cadastral
    if situacao != "Regular":
        return "Rejeitado: Situação cadastral irregular."
        
    # CAMINHO 2: Validação de Idade
    elif idade < 18:
        return "Rejeitado: Menor de idade."
        
    # CAMINHO 3: Renda Alta (Aprovado Especial)
    elif renda > 5000.00:
        return "Aprovado: Crédito especial com limite alto."
        
    # CAMINHO 4: Renda Padrão (Aprovado Comum)
    else:
        return "Aprovado: Crédito padrão."

# Bloco de execução interativa e automação dos testes de cobertura
if __name__ == "__main__":
    print("--- ANÁLISADOR DE CRÉDITO: COBERTURA DE CAMINHOS ---")
    
    # Definição dos cenários para forçar a execução de cada if/elif/else
    cenarios_teste = [
        {
            "id": "Caminho 1",
            "dados": {"idade": 30, "renda": 8000.0, "situacao_cadastral": "Irregular"},
            "esperado": "Rejeitado: Situação cadastral irregular.",
            "cobertura": "Filtro inicial de restrição no nome (Situação != 'Regular')"
        },
        {
            "id": "Caminho 2",
            "dados": {"idade": 16, "renda": 2000.0, "situacao_cadastral": "Regular"},
            "esperado": "Rejeitado: Menor de idade.",
            "cobertura": "Filtro de menoridade jurídica (Idade < 18)"
        },
        {
            "id": "Caminho 3",
            "dados": {"idade": 25, "renda": 6500.0, "situacao_cadastral": "Regular"},
            "esperado": "Aprovado: Crédito especial com limite alto.",
            "cobertura": "Critério de elegibilidade VIP (Renda > 5000.00)"
        },
        {
            "id": "Caminho 4",
            "dados": {"idade": 40, "renda": 3000.0, "situacao_cadastral": "Regular"},
            "esperado": "Aprovado: Crédito padrão.",
            "cobertura": "Fluxo residual/padrão do sistema (Else)"
        }
    ]
    
    # Execução e relatório detalhado dos testes mínimos
    for cenario in cenarios_teste:
        d = cenario["dados"]
        resultado_obtido = avaliar_credito(d["idade"], d["renda"], d["situacao_cadastral"])
        status = "✅ PASSOU" if resultado_obtido == cenario["esperado"] else "❌ FALHOU"
        
        print(f"\n📌 {cenario['id']} -> {cenario['cobertura']}")
        print(f"   Entrada: Idade={d['idade']}, Renda=R$ {d['renda']:.2f}, Cadastro='{d['situacao_cadastral']}'")
        print(f"   Esperado: {cenario['esperado']}")
        print(f"   Obtido:   {resultado_obtido}")
        print(f"   Status:   {status}")
