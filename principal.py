import tkinter as tk
from tkinter import messagebox

class Usuario:
    def __init__(self):
        self.usuarios = {}

    def incluir_usuario(self, id_usuario, nome, email):
        if id_usuario in self.usuarios:
            messagebox.showerror("Erro", "Usuário já cadastrado.")
        else:
            self.usuarios[id_usuario] = {"nome": nome, "email": email}
            messagebox.showinfo("Sucesso", "Usuário incluído com sucesso!")

    def alterar_usuario(self, id_usuario, novo_nome=None, novo_email=None):
        if id_usuario in self.usuarios:
            if novo_nome:
                self.usuarios[id_usuario]["nome"] = novo_nome
            if novo_email:
                self.usuarios[id_usuario]["email"] = novo_email
            messagebox.showinfo("Sucesso", "Usuário alterado com sucesso!")
        else:
            messagebox.showerror("Erro", "Usuário não encontrado.")

    def excluir_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            del self.usuarios[id_usuario]
            messagebox.showinfo("Sucesso", "Usuário excluído com sucesso!")
        else:
            messagebox.showerror("Erro", "Usuário não encontrado.")

    def listar_usuarios(self):
        if self.usuarios:
            lista = "\n".join(
                f"ID: {id}, Nome: {dados['nome']}, Email: {dados['email']}" for id, dados in self.usuarios.items()
            )
            messagebox.showinfo("Usuários cadastrados", lista)
        else:
            messagebox.showinfo("Usuários cadastrados", "Nenhum usuário cadastrado.")

class App:
    def __init__(self, root):
        self.master = root
        self.master.title("Cadastro de Usuários")

        self.usuario = Usuario()

        self.label_nome = tk.Label(root, text="nome:")
        self.label_nome.pack()

        self.entry_nome = tk.Entry(root)
        self.entry_nome.pack()

        self.label_endereco= tk.Label(root, text="endereço:", width=25)
        self.label_endereco.pack()

        self.entry_endereco = tk.Entry(root)
        self.entry_endereco.pack()

        self.label_email = tk.Label(root, text="Email:", width=25)
        self.label_email.pack()

        self.entry_email = tk.Entry(root)
        self.entry_email.pack()

        self.label_telefone = tk.Label(root, text="telefone:", width=25)
        self.label_telefone.pack()

        self.entry_telefone = tk.Entry(root)
        self.entry_telefone.pack()


        self.label_cpf = tk.Label(root, text="CPF:", width=25)
        self.label_cpf.pack()

        self.entry_cpf = tk.Entry(root)
        self.entry_cpf.pack()

        self.label_data = tk.Label(root, text="data do nascimento:", width=25)
        self.label_data.pack()

        self.entry_data = tk.Entry(root)
        self.entry_data.pack()

        self.btn_incluir = tk.Button(root, text="Incluir Usuário", command=self.incluir_usuario, bg="pink",width=20)
        self.btn_incluir.pack(pady=10)

        self.btn_alterar = tk.Button(root , text="Alterar Usuário", command=self.alterar_usuario, bg="pink",width=20)
        self.btn_alterar.pack(pady=10)

        self.btn_excluir = tk.Button(root , text="Excluir Usuário", command=self.excluir_usuario, bg="pink",width=20)
        self.btn_excluir.pack(pady=10)

        self.btn_listar = tk.Button(root , text="Listar Usuários", command=self.listar_usuarios, bg="pink",width=20)
        self.btn_listar.pack(pady=10)

    def incluir_usuario(self):
        id_usuario = self.entry_id.get()
        nome = self.entry_nome.get()
        email = self.entry_email.get()
        self.usuario.incluir_usuario(id_usuario, nome, email)

    def alterar_usuario(self):
        id_usuario = self.entry_id.get()
        novo_nome = self.entry_nome.get()
        novo_email = self.entry_email.get()
        self.usuario.alterar_usuario(id_usuario, novo_nome if novo_nome else None, novo_email if novo_email else None)

    def excluir_usuario(self):
        id_usuario = self.entry_id.get()
        self.usuario.excluir_usuario(id_usuario)

    def listar_usuarios(self):
        self.usuario.listar_usuarios()




if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
