import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Carrega o arquivo de chave como um objeto JSON
with open('podcasts.json') as f:
    keyfile_dict = json.loads(f.read())

# Obtém as informações de credenciais a partir do objeto JSON
creds = ServiceAccountCredentials.from_json_keyfile_dict(
    keyfile_dict, ['https://www.googleapis.com/auth/spreadsheets']
)

# Autentica a conta de serviço
client = gspread.authorize(creds)

# Abre a planilha
sheet = client.open('podcasts').sheet1

# Lê os dados do arquivo JSON
with open('podcasts.json') as f:
    data = json.loads(f.read())

# Insere os dados na planilha
for podcast in data:
    row = [podcast['id'], podcast['episodio'], podcast['duração'], podcast['data'], podcast['link'], podcast['descrição']]
    sheet.append_row(row)
