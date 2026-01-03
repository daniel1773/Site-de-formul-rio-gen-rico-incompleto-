from flask import Flask, render_template, request
from conexao_banco import conectar

app = Flask(__name__)

