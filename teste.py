"""
git rm --cached Teste.txt
git add .gitignore
git commit -m "Ignorando Teste.txt"
  
"""
import requests
import json


teste = requests.get("https://api.linketrack.com/track/json?user=cinbertolo@gmail.com&token=8aad50835e9d24544e38010d3c50285cc1b37838bcf961818d9ab29a891dfa19&codigo=NA976937556BR")
todos = json.loads(teste.content)

for i in todos['eventos']:
  print(todos['codigo'],i['local'],i['status'])

"""
{'codigo': 'NA976937556BR', 'servico': '', 'host': 'rd', 'quantidade': 7, 'eventos': [
{'data': '09/03/2023', 'hora': '16:55', 'local': 'SAO PAULO/SP', 'status': 'Objeto entregue ao destinatário', 'subStatus': []}, 
{'data': '09/03/2023', 'hora': '09:16', 'local': 'SAO PAULO/SP', 'status': 'Objeto saiu para entrega ao destinatário', 'subStatus': []}, 
{'data': '28/02/2023', 'hora': '04:29', 'local': 'CAJAMAR/SP', 'status': 'Objeto encaminhado', 'subStatus': ['Origem: Unidade de Tratamento - CAJAMAR/SP', 'Destino: Unidade de Distribuição - SAO PAULO/SP']}, 
{'data': '22/02/2023', 'hora': '09:40', 'local': 'CURITIBA/PR', 'status': 'Objeto encaminhado', 'subStatus': ['Origem: Unidade de Logística Integrada - CURITIBA/PR', 'Destino: Unidade de Tratamento - CAJAMAR/SP']},
{'data': '22/02/2023', 'hora': '09:40', 'local': 'CURITIBA/PR', 'status': 'Fiscalização aduaneira finalizada', 'subStatus': []}, 
{'data': '17/02/2023', 'hora': '23:07', 'local': 'CURITIBA/PR', 'status': 'Objeto recebido pelos Correios do Brasil', 'subStatus': ['<span class="minhasImportacoes">Acesse o ambiente <a href="https://www.correios.com.br/encomendas-logistica/minhas-importacoes/minhas-importacoes" target="_blank">Minhas Importações</a></span>']}, 
{'data': '13/02/2023', 'hora': '00:56', 'local': 'País', 'status': 'Objeto postado', 'subStatus': []}
], 'time': 0.032, 'ultimo': '2023-03-09T19:55:00.000Z'}"""