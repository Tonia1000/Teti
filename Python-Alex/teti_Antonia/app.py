 #a partir do pacote flask import o Flask
from flask import Flask, render_template
meu_app = Flask(__name__)


@meu_app.route('/home')
def home():
    return render_template('home.html')

# @''.route indica a rota
#def indica ao python o nome da função ou define coisas
@meu_app.route('/abobrinha')
def principal():
    #return '<h2>Integração de HTML e FLASK</h2>'
    return render_template('abobrinha.html')


@meu_app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@meu_app.route('/form')
def form():
    lista_nomes=['Stela', 'Caio', 'Maurício']
    return render_template('form.html', lista_nomes)


@meu_app.route('/test')
def test():
    listaNomes = {''}
    return render_template('test.html', listaNomes)

@meu_app.route('/atv4')
def calc():
    n1 = 0
    n2 = 0
    
    return render_template('atv4.html', n1, n2)

@meu_app.route('/atv5')
def atv5():
    
    return render_template('atv5.html')

@meu_app.route('/ativ5')
def ativ5():
    
    return render_template('ativ5.html')

@meu_app.route('/atv6')
def atv6():
    
    return render_template('atv6.html')

@meu_app.route('/atv7')
def atv7():
    
    return render_template('atv7.html')

@meu_app.route('/atv8')
def atv8():

#    cosd=cosseno de delta e send= seno de delta / delta= o angulo de rotação
#    x' = (x)*cosd-(y)*send
#    y'=(x)*send+(y)*cosd
    
    return render_template('atv8.html')

# @meu_app.route('/atv9')
# def atv9():
    
#     return render_template('atv9.html')