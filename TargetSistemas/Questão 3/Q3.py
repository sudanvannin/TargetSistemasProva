import json
from statistics import mean

def calcular_estatisticas_faturamento(dados):
    faturamento_valido = [dia['valor'] for dia in dados if dia['valor'] > 0]
    menor_valor = min(faturamento_valido)
    maior_valor = max(faturamento_valido)
    media_mensal = mean(faturamento_valido)
    dias_acima_media = sum(1 for valor in faturamento_valido if valor > media_mensal)
    return menor_valor, maior_valor, dias_acima_media

def main():
    with open('Questão 3/dados.json', 'r') as file:
        dados = json.load(file)
    menor, maior, dias_acima = calcular_estatisticas_faturamento(dados)
    
    print(f"Menor valor de faturamento: R$ {menor:.2f}")
    print(f"Maior valor de faturamento: R$ {maior:.2f}")
    print(f"Número de dias acima da média mensal: {dias_acima}")

if __name__ == "__main__":
    main()