import requests

class N8nLogica:
    def __init__(self, base_url: str):
        self.base_url = base_url
    
    def enviar_datos(self, datos: dict):
        url = f"{self.base_url}/webhook"
        try:
            response = requests.post(url, json=datos)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Erro ao enviar dados para n8n: {e}")
            return None
        
    def obtener_datos(self, workflow_id: str):
        url = f"{self.base_url}/workflow/{workflow_id}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Erro ao obter dados do workflow {workflow_id}: {e}")
            return None
    
