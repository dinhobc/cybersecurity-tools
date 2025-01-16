import shodan

def shodan_lookup(api_key, ip):
    api = shodan.Shodan(api_key)
    try:
        print(f"[+] Coletando informações sobre {ip}...")
        host = api.host(ip)
        print(f"IP: {host['ip_str']}")
        print(f"Organização: {host.get('org', 'N/A')}")
        print(f"País: {host['country_name']}")
        print("Portas abertas:")
        for port in host['ports']:
            print(f"  - Porta {port}")
    except shodan.APIError as e:
        print(f"Erro na API: {e}")

if __name__ == "__main__":
    print("Script de consulta ao Shodan")
    shodan_api_key = input("Digite sua API Key do Shodan: ")
    target_ip = input("Digite o endereço IP para consulta: ")
    shodan_lookup(shodan_api_key, target_ip)