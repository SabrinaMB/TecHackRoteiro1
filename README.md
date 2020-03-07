# TecHackRoteiro1
## 1.1
| Diario de bordo | |
| -------------------------- | -------------------------- |
| Data: | 27/02/2020 | 
| Dados de endereçamento do(s) alvo(s): | IP: 192.168.50.67 (obtido com o "sudo nmap -p 192.168.50.* " e vendo qual deles era o certo - escrito debian neste caso) | 

| | Dados | Comando utilizado |
| -------------------------- | -------------------------- | -------------------------- |
| Coletados de Rede (Portas/serviços, topologia) | Nome: ProFTPD, Versao: 1.3.5 | telnet 192.168.50.67 \\21 | 
| Coletados de aplicação (SO, versões de serviços..) | SO: Linux, Versao: entre 3.2 e 4.8 (O comando nao deu as informacoes corretas) | sudo nmap -sV -O 192.168.50.67

| Outros | |
| -------------------------- | ------ |
| Vulnerabilidades | Alto :  	Dir. Trav. ;  Medio: DoS Exec, Code, Overflow, Bypass, Sql Bypass | 
| Exploração | |
| Outras informações úteis | |

## 1.2

| HOSTNAME | REQUESTED IP ADDRESS | MAC ADDRESS |
| -------------------------- | -------------------------- | -------------------------- |
| MYHUMPS-PC | 192.168.204.137 | Vmware_9d:b8:6d (00:0c:29:9d:b8:6d) |
| WORKSTATION6 | 192.168.204.146 | Vmware_fc:bc:2e (00:0c:29:fc:bc:2e) |
| ROCKETMAN-PC | 192.168.204.139 | Vmware_61:c1:89 (00:0c:29:61:c1:89) |

IP do host com a conexao maliciosa: 192.168.204.137 <br />
Dominio do site comprometido: epzqy.iphaeba.eu:22780 <br />
URL que agiu como redirecionamento: www.adobe.com/images/shared/download_buttons/get_flash_player.gif <br />
Endereco IP da URL de redirecionamento: 212.152.163.10 <br />


