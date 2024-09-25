import tkinter as tk
from tkinter import ttk


usuarios = [
    { "nome": "geovanna", "email": "geovanna@example.com" , "telefone": 992151682},
    { "nome": "fe", "email": "fe@example.com" , "telefone":993451502},
    {"nome": "anna", "email": "anna@example.com" , "telefone": 992384052 },
]

def selecionar_usuario(event):

    selecionado = tree.selection()
    if selecionado:
        item = tree.item(selecionado)
        dados = item['values']

        entry_nome.delete(0, tk.END)
        entry_nome.insert(0, dados[1])
        entry_email.delete(0, tk.END)
        entry_email.insert(0, dados[2])

root = tk.Tk()
root.title("Consulta de Usuários")

tree = ttk.Treeview(root, columns=("ID", "Nome", "Email"), show='headings')
tree.heading("nome", text="nome")
tree.heading("email", text="email")
tree.heading("telefone", text="telefone")
tree.heading("endereço", text="endereço")


for usuario in usuarios:
    tree.insert("", "end", values=(usuario["nome"], usuario["email"], usuario["telefone"] , usuario["endereço"]))

tree.pack()


tree.bind("<<TreeviewSelect>>", selecionar_usuario)


frame_form = tk.Frame(root)
frame_form.pack(pady=10)

tk.Label(frame_form, text="Nome:").grid(row=0, column=0)
entry_nome = tk.Entry(frame_form)
entry_nome.grid(row=0, column=1)

tk.Label(frame_form, text="Email:").grid(row=1, column=0)
entry_email = tk.Entry(frame_form)
entry_email.grid(row=1, column=1)


root.mainloop()

