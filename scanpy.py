# se você está aqui parabéns e cuidado com o que você executa

import re
import json
import threading
import time
import os
import platform

try:
    import nmap
except ImportError:
    import subprocess
    subprocess.call(["pip", "install", "python-nmap"])
    import nmap
    
try:
    from colorama import Fore, Style
except ImportError:
    import subprocess
    subprocess.call(["pip", "install", "colorama"])
    from colorama import Fore, Style


args = ''
level = ''
target = ''
allports = []
tom_da_cor = ""
nm = nmap.PortScanner()

def banner():
    print("\n")
    print("         ▄███████▄")
    print("        █▀▀█████▀▀█")
    print("        █▄  ███  ▄█")
    print("        ▀████▄████▀")
    print("          ▀ ▀ ▀ ▀")
    print("  █▀▀ █▀▀ █▀█ █▄ █ █▀█ █ █")
    print("  ▀▀█ █   █▀█ █ ▀█ █▀▀ ▀█▀")
    print("  ▀▀▀ ▀▀▀ ▀ ▀ ▀  ▀ ▀    ▀")
    print("           █▄█▄█")
    print("Documentação Scanpy: https://github.com/santosfabin/scanpy")
    print("Ajuda: https://github.com/santosfabin/scanpy/blob/main/README.md\n")
    


def frufru_cor(num, descri):
    cor = ""
    if num ==1:
        cor = Fore.BLUE
    elif num == 2:
        cor = Fore.GREEN
    elif num == 3:
        cor = Fore.YELLOW
    elif num == 4:
        cor = Fore.MAGENTA
    elif num in (5, 6):
        cor = Fore.RED
        
    return cor + descri + Style.RESET_ALL

    
def frufru(num):
    if num == 1:
        print('-----------------------')
        print('Digite um valor válido')
        print('-----------------------')


def formatLevel(level):
    if level == 1:
        arg = "-sn"
    elif level == 2:
        arg = ""
    elif level == 3:
        arg = "-sV"
    elif level == 4:
        arg = "-sV -p-"
    elif level == 5:
        arg = "-A -sV -p-"
    elif level == 6:
        print("Digite seu parâmetro ou comando nmap: ")
        arg = input("> ")
        if arg.startswith("nmap "):
            arg = arg[len("nmap "):]
    global args
    args = arg

def reconInfo():
    global target
    print('Digite seu alvo')
    host_target = input('> ')
    target = host_target
    while True:
        print("\n" + frufru_cor(1, '1 Básico') + '\t[Somente ping no alvo]\n' + frufru_cor(2, '2 Leve') + '\t\t[Verificar portas conhecidas]\n' + frufru_cor(3, '3 Moderado') + '\t[Verificar versão]\n' + frufru_cor(4, '4 Rigoroso') + '\t[Verifica todas as portas]\n' + frufru_cor(5, '5 Impiedoso') + '\t[Verificação extras]\n' + frufru_cor(6, '6 Digite seu comando') + '\n')
        global level
        print('Digite a força: ')
        level = input('> ')
        try:
            level = int(level)
            if level in (1, 2, 3, 4, 5, 6):
                formatLevel(level)
                break
            else:
                frufru(1)
        except:
            frufru(1)


def verify_services():
    try:
        with open('dados.json', 'r') as arquivo:
            dados = json.load(arquivo)
    except:
        print("Tente executar na pasta do programa")
    
    menssages = []
    
    for programa, portas in dados.items():
        check = True
        for porta in portas:
            if porta not in allports:
                check = False
                break
        if check:
            menssages.append(f"Provavel que exista o programa '{programa}' rodando com as portas: {portas}")
    
    return menssages

def save_file():
    print("\nDeseja salvar o resultado?")
    print("Sim [S]")
    print("Não [N]")
    save = input("> ")
    try:
        save = save[0].lower()
    except:
        save = "n"
    if(save in ("s","y")):
        print("Digite o nome do arquivo")
        name_file = input("> ")
        if(name_file == ""):
            name_file = "Default.txt"
        return True, name_file
    else:
        return False, None

def remove_ansi_colors(text):
    ansi_escape = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')
    return ansi_escape.sub('', text)

def get_level():
    
    try:
        nm.scan(target, arguments=args)
    except:
        print("error")

def start(save_to_file, file_name):
    global level
    output = [] 

    for host in nm.all_hosts():
        output.append(f"Host: " + frufru_cor(level, f"{host}"))
        for proto in nm[host].all_protocols():
            output.append(f"Protocolo: " + frufru_cor(level, f"{proto}"))
            ports = nm[host][proto].keys()
            for port in ports:
                service = nm[host][proto][port]['name']
                state = nm[host][proto][port]['state']
                version = nm[host][proto][port]['version']
                extrainfo = nm[host][proto][port]['extrainfo']
                product = nm[host][proto][port]['product']
                output.append("\tPorta: " + frufru_cor(level, f"{port}") + " \n\t\tServiço: " + frufru_cor(level, f"{service}") + "\n\t\tEstado: " + frufru_cor(level, f"{state}") + "\n\t\tVersão: " + frufru_cor(level, f"{version}") + f"\n\t\tInformações Extras: " + frufru_cor(level, f"{extrainfo}") + f"\n\t\tBanner: " + frufru_cor(level, f"{product}"))
                allports.append(port)

    mensagens = verify_services()
    try:
        if not mensagens:
            output.append("\nNenhuma aplicação detectada\n")
        else:
            for mensagem in mensagens:
                output.append(mensagem)
    except:
        output.append("\nErro desconhecido")

    if save_to_file:
        with open(file_name, "w") as arquivo:
            for linha in output:
                linha_sem_cores = remove_ansi_colors(linha)
                arquivo.write(linha_sem_cores + "\n")
    else:
        for linha in output:
            print(linha)

def get_save_info():
    result = save_file()
    save_to_file = result[0]
    file_name = result[1]
    return save_to_file, file_name


def clear():
    sistema_operacional = platform.system()
    
    if sistema_operacional == "Windows":
        os.system('cls')  # Para Windows
    else:
        os.system('clear')

def loading_animation():
    time.sleep(0.1)
    while not done_flag.is_set():
        i = 0
        for i in range(0, 20):
            clear()

            print("\n")
            print("         ▄███████▄  S")
            print("        █▀▀█████▀▀█ C")
            print("        █▄  ███  ▄█ A")
            print("        ▀████▄████▀ N")
            print("          ▀ ▀ ▀ ▀")
            if (i % 2 == 0):
                print()
            print("           █▄█▄█\n")
            if (i % 2 != 0):
                print()
            time.sleep(0.3)
        
def fineshed_program():
    clear()
    print("\n" + frufru_cor(level, "Escaneamento completo") + "\n")
    print("\nEscaner com nível de força: " + frufru_cor(level, f"{level}") + "...")
    print(f"Comando nmap usado: " + frufru_cor(level, f"nmap {args}\n"))

def start_program():
    banner()
    
    reconInfo()
    
    save_to_file, file_name = get_save_info()

    global done_flag
    done_flag = threading.Event()

    loading_thread = threading.Thread(target=loading_animation)
    
    loading_thread.start()

    get_level()

    done_flag.set()  # Sinaliza que a função get_level() terminou

    loading_thread.join()  # Aguarda a thread de animação de loading terminar
    
    fineshed_program()
    
    start(save_to_file, file_name)
    
    print("Finalizado")

start_program()

