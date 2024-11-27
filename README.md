# Projeto de Otimização Logística com Múltiplos Centros de Distribuição
## Visão Geral
Esse projeto contém o script com a lógica que resolve o problema da otimização da logística com múltiplos centros de distribuições..
### Estrutura do Projeto (Arquitetura MVC)
* src.models.model_data.py: Contém a estruturação dos dados dos caminhões, entrega e Grafo.<br>
* src.services.data_manipulation.py: Contém a lógica de alocar as entregas e gerar cenário.<br>
* src.services.create_sheets.py: Contém a lógica para criar um arquivo de excel para a visualização.<br>
* main.py: Ponto de entrada para a execução do código.<br>
* mais_entregas_caminhoes.xlsx: É o arquivo excel criado com a visualização do cenário com mais entregas.
* menos_entregas_caminhoes.xlsx: É o arquivo excel criado com a visualização do cenário com menos entregas.

### Requisitos do Sistema
* Python 3.12.0.
* Biblioteca pandas.
* Biblioteca geopy.
* Biblioteca math.

### Instalação
* Instale usando "pip install -r requirements.txt".

### Observação
* Certifique-se de instalar corretamente as bibliotecas.