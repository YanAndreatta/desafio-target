import json 

def abrir_arquivo(file):
    with open(arquivo_caminho, 'r') as file:
        dados = json.load(file)
        return dados
    
def menor_faturamento_dia(dados):
    menor_faturamento = min([dia['valor'] for dia in dados if dia['valor'] > 0])
    return menor_faturamento

def maior_faturamento_dia(dados):
    maior_faturamento = max(dia['valor'] for dia in dados)
    return maior_faturamento

def media_faturamento_mensal(dados):
    faturamentos = [dia['valor'] for dia in dados if dia['valor'] > 0]
    media_faturamento = sum(faturamentos) / len(faturamentos)
    return media_faturamento

def faturamento_maior_media(dados):
    media = media_faturamento_mensal(dados)
    faturamentos = [dia['valor'] for dia in dados if dia['valor'] > media]
    return len(faturamentos)

if __name__ == '__main__':
    arquivo_caminho = "./data/dados.json"
    dados = abrir_arquivo(arquivo_caminho)
    print("Menor faturamento diário:", menor_faturamento_dia(dados))
    print("Maior faturamento diário:", maior_faturamento_dia(dados))
    print("Número de dias em que o faturamento diário foi maior que a média mensal:", faturamento_maior_media(dados))