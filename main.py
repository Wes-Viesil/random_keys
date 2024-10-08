# Chave aleatória web integrado com o banco de dados Access (Tabela1, Chaves)

import flet as ft
import secrets
import string
import pyodbc

# Função principal
def main(page: ft.Page):

    # Função login
    def login(event):
        username = username_input.value
        password = password_input.value
        if username == "admin" and password == "admin":
            page.update()
            page.clean()
            page.add(
                ft.Column(
                    controls=[
                        ft.ElevatedButton("Gerar chave", on_click=generate_key),
                        key_text
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                )
            )
        else:
            page.update()
            page.add(ft.Text("Invalid username or password"))

    # Função gerar chave
    def generate_key(event):
        key = ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(10))
        key_text.value = f"Chave: {key}"
        page.update()
        save_key_to_db(key)

    # Função salvar chave no banco de dados Access
    def save_key_to_db(key):
        conn_str = "DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\\Users\\Wesley\\Documents\\BancosDeDados\\Database1.accdb"
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Tabela1 (Chaves) VALUES (?)", key)
        conn.commit()
        conn.close()

    # Página
    page.title = "Random Key"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER 
    page.theme_mode = ft.ThemeMode.LIGHT # Deixa a página clara
    # Campos de texto
    username_input = ft.TextField(label="Username", width=300)
    password_input = ft.TextField(label="Password", width=300, password=True)
    # Botão
    login_button = ft.ElevatedButton("Login", on_click=login)

    key_text = ft.Text("")
    
    page.add(
        ft.Column(
            controls=[
                username_input,
                password_input,
                login_button,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

# Abre o sistema no browser padrão
ft.app(target=main, view=ft.WEB_BROWSER, port=8000)

