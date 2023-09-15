# Scanpy - Ferramenta de Varredura de Rede com Nmap

Scanpy é uma ferramenta Python simples que utiliza o Nmap para realizar varreduras de rede e descoberta de serviços. Ele foi projetado para ser fácil de usar e oferece algumas funcionalidades básicas de varredura de rede.

## Recursos Principais

1. Varredura de rede rápida e fácil.
2. Identificação de serviços e versões em execução.
3. Suporte para diferentes níveis de varredura.
4. Capacidade de salvar resultados em um arquivo.
5. Verificação de serviços conhecidos a partir de um arquivo de configuração modificável.

## Pré-requisitos

- Python 3.x
- Nmap (certifique-se de que o Nmap está instalado em seu sistema):
    - [https://nmap.org/download](https://nmap.org/download)

## Instalação

Para instalar as dependências, execute o seguinte comando:

```bash
pip install python-nmap colorama
```

ou

```bash
sudo apt install python3-nmap
sudo apt install python3-colorama
```

Para instalar o scanpy clone este repositório ou faça o download dos arquivos para o seu computador.

```bash
git clone https://github.com/santosfabin/scanpy.git
cd scanpy
```

Execute o programa usando o seguinte comando:

```bash
python3 scanpy.py
```

## Como Usar

1. Formatações aceitas
    1. Alvo
        - IP
        - URL
    2. Parâmetros nmap
        - Você pode montar seu comando sem restrições com a opção `**6**`
        - Qualquer comando aceito pelo nmap o scanpy consegue executar
        - Pode ser colocando nmap na frente se quiser, ou somente digitar os parâmetros
        - Podendo ser como:
            - `nmap -sV -A`
            - `-sV -p-`
            - `nmap -p- 192.168.0.1`
            - `-p-`
    3. Salvar arquivo
        - C:\Users\You\Desktop\Folder\Arquivo.txt
        - /home/You/Desktop/Folder/Arquivo.txt
        - ../Arquivo.txt
        - Arquivo.txt

## Configuração

O programa possui um arquivo chamado `dados.json` que contém informações sobre serviços conhecidos e as portas em que eles podem ser encontrados. Você pode adicionar ou modificar essas informações de acordo com suas necessidades.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir problemas, enviar solicitações de pull ou melhorar a documentação.
