def percentual_representacao(dados):
    soma = sum(estado['faturamento'] for estado in dados)
    percentual = [(estado['estado'], (estado['faturamento'] / soma) * 100) for estado in dados]
    return percentual

if __name__ == "__main__":
    list_states = [
    {"estado": "SP", "faturamento": 67836.43},
    {"estado": "RJ", "faturamento": 36678.66},
    {"estado": "MG", "faturamento": 29229.88},
    {"estado": "ES", "faturamento": 27165.48},
    {"estado": "Outros", "faturamento": 19849.53}
    ]

    percentuais = percentual_representacao(list_states)
    for estado, perc in percentuais:
        print(f"{estado}: {perc:.2f}%")