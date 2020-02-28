# TecHackRoteiro1

| Diario de bordo | |
| -------------------------- | -------------------------- |
| Data: | 27/02/2020 | 
| Dados de endereçamento do(s) alvo(s): | IP: 192.168.50.67 (obtido com o "sudo nmap -p 192.168.50.*") | 

| | Dados | Comando utilizado |
| -------------------------- | -------------------------- | -------------------------- |
| Coletados de Rede (Portas/serviços, topologia) | Foram obtidas quais portas estavam abertas: 21, 22, 80, 111, 139 e 445 com os respectivos servicos: ftp, ssh, http, rpcbind, netbios-ssn, microsoft-ds | telnet 192.168.50.67 \\\<porta> | 
| Coletados de aplicação (SO, versões de serviços..) | SO: Linux, Versao: entre 3.2 e 4.8 (O comando nao deu as informacoes corretas) | sudo nmap -sV -O 192.168.50.67

| Outros |
| -------------------------- |
| Vulnerabilidades | 
| Exploração |
Outras informações úteis |
