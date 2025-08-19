import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox

def processar_planilha(caminho_entrada, caminho_saida):
    try:
        df = pd.read_csv(caminho_entrada, encoding='utf-8', delimiter=';')
        
        if 'CELULAR' not in df.columns:
            messagebox.showerror("Erro", "Coluna 'CELULAR' não encontrada no arquivo.")
            return
        
        df = df.applymap(lambda x: str(x).replace("�", "X") if isinstance(x, str) else x)
        df['CELULAR'] = df['CELULAR'].astype(str)
        df['ID'] = range(1, len(df) + 1)
        
        def validar_celular(celular):
            return "SIM" if isinstance(celular, str) and 9 <= len(celular) <= 13 and celular.isdigit() else "NÃO"
        
        df['VALIDO'] = df['CELULAR'].apply(validar_celular)
        
        df['DUPLICADO'] = 'ÚNICO'
        celulares_vistos = set()
        for i, celular in enumerate(df['CELULAR']):
            if celular in celulares_vistos:
                df.at[i, 'DUPLICADO'] = 'DUPLICADO'
            else:
                celulares_vistos.add(celular)
        
        df.to_csv(caminho_saida, index=False)
        messagebox.showinfo("Sucesso", f"Planilha exportada para: {caminho_saida}")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao processar a planilha: {str(e)}")

def selecionar_arquivo_entrada():
    caminho = filedialog.askopenfilename(filetypes=[("Arquivos CSV", "*.csv")])
    entrada_var.set(caminho)

def selecionar_arquivo_saida():
    caminho = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("Arquivos CSV", "*.csv")])
    saida_var.set(caminho)

def iniciar_processamento():
    caminho_entrada = entrada_var.get()
    caminho_saida = saida_var.get()
    if not caminho_entrada or not caminho_saida:
        messagebox.showwarning("Aviso", "Selecione os arquivos de entrada e saída.")
        return
    processar_planilha(caminho_entrada, caminho_saida)

root = tk.Tk()
root.title("Processador de Planilhas")

tk.Label(root, text="Arquivo de Entrada:").pack()
entrada_var = tk.StringVar()
tk.Entry(root, textvariable=entrada_var, width=50).pack()
tk.Button(root, text="Selecionar", command=selecionar_arquivo_entrada).pack()

tk.Label(root, text="Arquivo de Saída:").pack()
saida_var = tk.StringVar()
tk.Entry(root, textvariable=saida_var, width=50).pack()
tk.Button(root, text="Selecionar", command=selecionar_arquivo_saida).pack()

tk.Button(root, text="Processar", command=iniciar_processamento).pack()

root.mainloop()
