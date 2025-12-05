import requests
import time
import json
from pathlib import Path

def load_config():
    config_path = Path(__file__).resolve().parent / "config.json"
    with open(config_path, "r", encoding="utf-8") as f:
        return json.load(f)

config = load_config()


produto = config["produto"]
webhook_url = config["webhook_url"]


def enviar_webhook(sku):
    data = {
        "content": f"O produto teve alteração no preço!\n🔗 {produto}"
    }
    try:
        response = requests.post(webhook_url, json=data)
        if response.status_code == 204:
            print(f"[🚀] Webhook enviado com sucesso para {sku}")
        else:
            print(f"[⚠️] Falha ao enviar webhook: {response.status_code}")
    except Exception as e:
        print(f"[⚠️] Erro ao enviar webhook: {e}")



def monitor():
    response = requests.get(produto)

    while True:
        if '"price":399.99' in response.text:
            print("Segue preço antigo")
        else:
            print("Preço alterado, confirmar!")
            print("Enviando webhook e encerrando...")
            enviar_webhook(produto)
            break
        time.sleep(5)

monitor()