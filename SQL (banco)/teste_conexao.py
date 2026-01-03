from conexao_banco import conectar

try:
    conectar()
    print("Conexão deu certo!")
    conectar().close()
except Exception as e:
    print("Erro ao conectar com o banco.", e)