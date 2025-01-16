# Script para gerar logs e enviar para o Splunk usando a API HTTP Event Collector

import requests
import json
import random
import time

# URL do HTTP Event Collector do Splunk
splunk_url = "http://localhost:8088"
splunk_token = "Seu_Token_Do_Splunk"  # Substitua com seu token do Splunk

def send_log_to_splunk(log_data):
    headers = {
        'Authorization': f'Splunk {splunk_token}',
        'Content-Type': 'application/json'
    }
    response = requests.post(f"{splunk_url}/services/collector", headers=headers, data=json.dumps(log_data))
    if response.status_code == 200:
        print("Log enviado com sucesso para o Splunk.")
    else:
        print("Falha ao enviar log para o Splunk.")

def generate_log():
    log_data = {
        "event": f"Alerta de segurança: Tentativa de acesso não autorizado da IP {random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.",
        "sourcetype": "access_alert",
        "index": "security_logs"
    }
    return log_data

if _name_ == "_main_":
    while True:
        log_data = generate_log()
        send_log_to_splunk(log_data)
        time.sleep(5)  # Enviar logs a cada 5 segundos