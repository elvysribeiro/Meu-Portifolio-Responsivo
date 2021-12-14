from flask import Flask, config, render_template, redirect, request,flash
from flask.scaffold import F
from flask_mail import Mail, mensage
from werkzeug.wrappers import request
from config import email,senha

app = Flask(__name__)
app.secret_key = "devweb"

mail_settings = { 
    "MAIL_SERVER": "smtp.gmail.com",
    "MAIL_PORT":  465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": email,
    "MAIL_PASSWORD": mail_senha
}

app.config.update(mail_settings)
mail = Mail(app)

class contato:
    def __init__(self,nome,email,mensagem):
        self.nome = nome,
        self.email= email,
        self.mensagem = mensagem,
        
@app.route('/')
def index():
    return render_template('index.html')

@app.route("/send", methods=["GET", "POST"]) 
def send():
    if request.method == "POST":
        formaContato = contato(
            request.form["nome"],
            request.form["email"],
            request.form["mensagem"]
        )
        msg = Message(
            subject = f"{formContato.nome} te enviou uma mensagem no potifólio",
            sender = app.config.get("MAIL_USERNAME"),
            recipients = ["elvyssribeiro@gmail.com"],
            body = f'''
            
            {formContato.nome} com o e-mail {formContato.email}, te enviou a seguinte mensagem:

            {formContato.mensagem} 
            
            '''
        )
        mail.send(msg)
        flash("mensagem enviada com sucesso!")
    return redirect('/')    

if __name__ == '__main__':
    app.run(debug=True)