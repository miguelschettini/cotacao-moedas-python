import requests

def pegar_cotacao(moeda_origem):
    """
    Função que busca a cotação de qualquer moeda em relação ao Real (BRL)
    Exemplo: USD, EUR, BTC, GBP
    """
    # Deixamos em letras maiúsculas para evitar erros da API
    moeda = moeda_origem.upper()
    url = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"
    
    try:
        resposta = requests.get(url)
        # Se a moeda não existir, a API retorna erro 404
        if resposta.status_code == 404:
            return f"Erro: A moeda '{moeda}' não foi encontrada."
            
        dados = resposta.json()
        chave = f"{moeda}BRL"
        
        nome = dados[chave]['name']
        valor = float(dados[chave]['bid'])
        data = dados[chave]['create_date']
        
        return f"{nome}\nValor: R$ {valor:.2f}\nData da consulta: {data}"
        
    except Exception as e:
        return f"Ocorreu um erro de conexão: {e}"

# --- Interface Simples no Terminal ---
print("="*30)
print(" CONSULTOR DE MOEDAS 3.0 ")
print("="*30)

while True:
    escolha = input("\nDigite a moeda (ex: USD, EUR, BTC) ou 'sair' para encerrar: ").strip()
    
    if escolha.lower() == 'sair':
        print("Encerrando o programa... Até logo!")
        break
    
    resultado = pegar_cotacao(escolha)
    print("-" * 20)
    print(resultado)
    print("-" * 20)