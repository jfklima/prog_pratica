# arquivo de endereços ip
# arquivo de endereços ip validados

# enderecos de ip valido são aqueles que tem quatro números sepados por ponto e
# que cada número não pode ultrapassar o valor de 255 ou seja não pode ser
# maior que 255

def validar(ip):
    numeros = ip.split('.')

    if len(numeros) !=4:
        return False

    for n in numeros:
        if not (0 <= int(n) <= 255):
            return False

    return True

ips_validos = []
ips_invalidos = []

with open("enderecos_ip.txt", 'r') as arquivo:
    for linha in arquivo:
        ip = linha.strip()
        if validar(ip):
            ips_validos.append(ip)
        else:
            ips_invalidos.append(ip)

with open("enderecos_ip_validado.txt", 'w') as arquivo:
    arquivo.writelines('[Endereços válidos:]\n')
    for ip_valido in ips_validos:
        arquivo.writelines(f"{ip_valido}\n")

    arquivo.writelines('\n')
    arquivo.writelines('\n')

    arquivo.writelines('[Endereços inválidos:]\n')
    for ip_invalido in ips_invalidos:
        arquivo.writelines(f"{ip_invalido}\n")
