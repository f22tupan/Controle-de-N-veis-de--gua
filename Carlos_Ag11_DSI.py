from colorama import Fore, Style

# Lista com mensagens e cores para cada nível
niveis = [
    ("Muito baixo (crítico)", Fore.RED),
    ("Baixo", Fore.YELLOW),
    ("Médio", Fore.GREEN),
    ("Alto", Fore.CYAN),
    ("Muito alto (alerta)", Fore.BLUE)
]

# Função que exibe a mensagem colorida conforme o nível
def exibir_alerta(nivel):
    if 1 <= nivel <= len(niveis):
        mensagem, cor = niveis[nivel - 1]
        print(cor + f"Nível {nivel}: {mensagem}" + Style.RESET_ALL)
    else:
        print(Fore.MAGENTA + "Nível inválido!" + Style.RESET_ALL)

# Simulação: percorre todos os níveis do reservatório
for i in range(1, 6):
    exibir_alerta(i)

