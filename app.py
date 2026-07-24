from flask import Flask, render_template

# Inicializa a aplicação
app = Flask(__name__)

# Rota principal (Home)
@app.route("/")
def home():
    # render_template busca o arquivo obrigatoriamente dentro da pasta /templates
    return render_template("index.html")

# Rota secundária (Sobre)
@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

# Rota de verificação de saúde da aplicação (Healthcheck útil para o CI/CD depois)
@app.route("/health")
def health():
    return {"status": "ok", "service": "flask-app"}, 200

if __name__ == "__main__":
    # debug=True recarrega o servidor automaticamente ao alterar o código
    app.run(host="0.0.0.0", port=5000, debug=True)