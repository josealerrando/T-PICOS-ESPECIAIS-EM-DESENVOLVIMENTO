def verificar_duplicados(lista_estudantes):
    vistos = set()
    duplicados = set()
    
    for nome in lista_estudantes:
        # Padroniza tirando espaços extras e convertendo para minúsculas
        nome_limpo = nome.strip().title()
        
        if nome_limpo in vistos:
            duplicados.add(nome_limpo)
        else:
            vistos.add(nome_limpo)
            
    return list(duplicados)

# Bloco de execução interativa (Ponto para uso)
if __name__ == "__main__":
    print("--- DETECTOR DE ESTUDANTES DUPLICADOS ---")
    
    # Lista para teste manual ou você pode preencher aqui
    entrada = input("Digite os nomes dos estudantes separados por vírgula:\n> ")
    
    # Converte a entrada de texto em uma lista de nomes
    estudantes = [nome.strip() for nome in entrada.split(",") if nome.strip()]
    
    if not estudantes:
        print("Nenhum nome foi inserido.")
    else:
        nomes_repetidos = verificar_duplicados(estudantes)
        
        print("\n--- RESULTADO DA ANÁLISE ---")
        if nomes_repetidos:
            print("⚠️ ATENÇÃO! Registros duplicados encontrados para verificação:")
            for nome in nomes_repetidos:
                print(f" - {nome}")
        else:
            print("✅ Sucesso! Nenhum nome repetido foi encontrado.")
