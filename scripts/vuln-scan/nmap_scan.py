import os

def run_nmap_scan(target):
    print(f"[+] Iniciando varredura em {target}...")
    command = f"nmap -sV --script=vuln {target}"
    os.system(command)

if __name__ == "_main_":
    print("Script de varredura de vulnerabilidades com Nmap")
    target_ip = input("Digite o endereço IP ou domínio para escanear: ")
    run_nmap_scan(target_ip)