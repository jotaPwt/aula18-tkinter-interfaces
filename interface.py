import tkinter as tk

janela = tk.Tk()

janela.geometry('700x700')
janela.title('Hello, World')

#widgets

titulo = tk.Label(janela, text = 'Isso é um texto')
titulo.grid(row=1, column=4)

# titulo1 = tk.Label(janela, text = 'Isso é um texto pt2')
# titulo1.grid(row=2, column=2, padx=200)


# botao

btn = tk.Button(janela, text = 'Botão')
btn.grid(row=2, column=4)

janela.mainloop()