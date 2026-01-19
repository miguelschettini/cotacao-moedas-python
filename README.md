# Consulta de Cotação via API

Este projeto é um script Python automatizado que consulta a cotação em tempo real do Dólar (USD) para o Real (BRL). 

Originalmente, o projeto foi planejado como um Web Scraper, mas evoluiu para o consumo de uma **API REST** (AwesomeAPI), garantindo maior estabilidade, velocidade e evitando bloqueios de segurança (Captchas) de grandes buscadores.

## Funcionalidades
- **Consulta em tempo real:** Obtém os dados mais recentes do mercado financeiro.
- **Consumo de API:** Utiliza requisições HTTP para buscar dados estruturados em JSON.
- **Tratamento de Erros:** Lógica de exceções para garantir que o script informe falhas de conexão de forma clara.
- **Formatação:** Exibição dos valores tratados com duas casas decimais.
-**Interatividade:** Menu de busca dinâmico que permite ao usuário consultar qualquer par de moedas disponível na API em tempo real.


## Tecnologias Utilizadas
- **Python 3.11**
- **Requests:** Biblioteca para chamadas HTTP.
- **JSON:** Formato de troca de dados entre a API e o script.

## Evolução Técnica
Durante o desenvolvimento, identifiquei que o scraping via Google Search apresentava instabilidades. A migração para uma API oficial demonstrou:
1. **Performance:** Respostas muito mais rápidas por não carregar HTML/CSS/JS.
2. **Confiabilidade:** Dados padronizados que não dependem da estrutura visual de um site.

##  Como Executar
1. Instale a biblioteca necessária:
   pip install requests

2. Execute o script:
python cotacao.py