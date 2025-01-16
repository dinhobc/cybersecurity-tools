# Cenário de Análise com Wireshark

## Cenário:
Você recebeu um arquivo .pcap com suspeitas de atividade maliciosa. Sua tarefa é identificar:  
1. O endereço IP do atacante.  
2. As portas utilizadas na comunicação.  
3. Se há tráfego de arquivos suspeitos.  

## Passos:
1. Abra o Wireshark e carregue o arquivo suspect_traffic.pcap.
2. Use os filtros:
   - http para tráfego HTTP.
   - tcp.port == 21 para tráfego FTP.  
3. Responda às perguntas no relatório final.