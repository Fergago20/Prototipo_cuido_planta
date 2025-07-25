import requests

class N8nLogica:
    def __init__(self):
        self.base_url = "https://grupoowc-dev-n8n.h9fjgm.easypanel.host/webhook/iaecobot"
    
    def enviar_datos(self, datos: dict):
        
        try:
            response = requests.post(self.base_url, json=datos)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Erro ao enviar dados para n8n: {e}")
            return None
        
    def obtener_datos(self, workflow_id: str):
        try:
            response = requests.get(self.base_url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Erro ao obter dados do workflow {workflow_id}: {e}")
            return None
    
