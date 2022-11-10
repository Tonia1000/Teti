 #a partir do pacote flask import o Flask
#from matplotlib.pyplot import get
#from requests import post, request
from flask import Flask, render_template, request
meu_app = Flask(__name__)


@meu_app.route('/home')
def home():
    return render_template('home.html')

# ----------------------------------------------------------------

# @''.route indica a rota
#def indica ao python o nome da função ou define coisas
@meu_app.route('/abobrinha')
def principal():
    #return '<h2>Integração de HTML e FLASK</h2>'
    return render_template('abobrinha.html')

# ----------------------------------------------------------------
@meu_app.route('/sobre')
def sobre():
    return render_template('sobre.html')

# ----------------------------------------------------------------
@meu_app.route('/form')
def form():
    lista_nomes=['Stela', 'Caio', 'Maurício']
    return render_template('form.html', lista_nomes)

# ----------------------------------------------------------------
@meu_app.route('/test')
def test():
    listaNomes = {''}
    return render_template('test.html', listaNomes)

# ----------------------------------------------------------------
@meu_app.route('/atv4')
def calc():
    n1 = 0
    n2 = 0
    
    return render_template('atv4.html', n1, n2)

# ----------------------------------------------------------------
@meu_app.route('/atv5')
def atv5():
    
    return render_template('atv5.html')

# ----------------------------------------------------------------
@meu_app.route('/ativ5')
def ativ5():
    
    return render_template('ativ5.html')

# ----------------------------------------------------------------
@meu_app.route('/atv6')
def atv6():
    
    return render_template('atv6.html')

# ----------------------------------------------------------------
@meu_app.route('/atv7')
def atv7():
    
    return render_template('atv7.html')

# ----------------------------------------------------------------
@meu_app.route('/atv8')
def atv8():
    
    return render_template('atv8.html')

# ----------------------------------------------------------------
@meu_app.route('/api_teti', methods=['POST','GET'])
def blabla():
    token = 'ABC'
    if(request.method=='GET'):
        return render_template('blabla.html')        
    if(request.method=='POST'):
        token_for=request.form.get('token')
        if token_for==token:
            return render_template('blabla.html', msn='success')
        return render_template('blabla.html', msn='fail')
    
# ----------------------------------------------------------------
@meu_app.route('/api-teti', methods=['POST','GET'])
def api():
    
    return render_template('api.html')

# ----------------------------------------------------------------
@meu_app.route('/user', methods=['GET', 'POST'])
def user():
    name = "Ze"
    password = "123"
    if(request.method=='GET'):
        return render_template('user.html')        
    if(request.method=='POST'):
        name_for=request.form.get('name')
        password_for=request.form.get('password')
        if name_for=="Ze" and password_for=="123":
            return render_template('user.html', msn='success')
        return render_template('user.html', msn='fail')
    
    return render_template('user.html')

# ----------------------------------------------------------------
if __name__== "__main__":
    meu_app.run(debug=True)