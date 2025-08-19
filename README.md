# Processador de Planilhas CSV 📊

Este projeto é um utilitário em **Python** que permite processar planilhas CSV contendo números de celular, validando e identificando duplicatas de forma simples. Utilizando uma interface gráfica para seleção dos arquivos de entrada e saída.

## 🚀 Funcionalidades
- Leitura de arquivos **CSV** com separador `;`.
- Validação de números de celular (entre **9 e 13 dígitos numéricos**).
- Identificação de duplicados, onde a **primeira ocorrência é marcada como "ÚNICO"** e as subsequentes como **"DUPLICADO"**.
- Substituição automática de caracteres inválidos `�` por `X`.
- Adição de coluna `ID` numerando todas as linhas.
- Exportação do resultado para um novo arquivo CSV.
- Interface gráfica feita com **Tkinter** para facilitar a escolha dos arquivos.

## 🖥️ Interface Gráfica
O programa abre uma janela onde o usuário pode:
1. Selecionar o arquivo de entrada (`.csv`).
2. Escolher o local e o nome do arquivo de saída.
3. Processar os dados com um clique.

## 📦 Instalação
Clone o repositório:
```bash
git clone https://github.com/seu-usuario/processador-planilhas.git
cd processador-planilhas
```

Instale as dependências:
```bash
pip install pandas
```

## ▶️ Uso
Execute o script com:
```bash
python processador.py
```

A interface será aberta e você poderá selecionar os arquivos.

## 📂 Estrutura do Projeto
```
📦 processador-planilhas
 ┣ 📜 processador.py   # Código principal
 ┣ 📜 README.md        # Este arquivo
```

## 🔧 Exemplo de Saída
Após o processamento, o arquivo de saída conterá as colunas adicionais:
- `ID`
- `VALIDO`
- `DUPLICADO`

Exemplo:
| ID | CELULAR     | VALIDO | DUPLICADO |
|----|-------------|--------|-----------|
| 1  | 11999999999 | SIM    | ÚNICO     |
| 2  | 11999999999 | SIM    | DUPLICADO |

## 📜 Licença
Este projeto está sob a licença MIT. Sinta-se livre para usar e modificar.
