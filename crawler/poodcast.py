from google.oauth2 import service_account
from googleapiclient.discovery import build

# Carrega as credenciais de autenticação
SCOPES = ['https://www.googleapis.com/auth/podcasts']
SERVICE_ACCOUNT_FILE = '/path/to/credentials.json'
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# Cria o objeto da API do Google Podcasts
podcasts = build('podcasts', 'v1', credentials=credentials)

# Define o termo de busca (neste caso, 'christian')
query = 'cristão'

# Faz a busca dos podcasts mais recentes
results = podcasts.podcasts().episodes().search(q=query, orderBy='newest', limit=10).execute()

# Imprime as informações dos podcasts encontrados
for episode in results['episodes']:
    print('Título:', episode['title'])
    print('Descrição:', episode['description'])
    print('Data de publicação:', episode['published'])
    print('Link:', episode['listenNotesAudioUrl'])
    print()
