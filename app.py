
from flask import Flask, render_template, redirect, request
from bd import nova_classe, atualizar_classe, listar_classe, remove_classe, detalha_classe
from bd import nova_arma, atualizar_arma, listar_arma, remove_arma, detalha_arma
from bd import nova_armadura, atualizar_armadura, listar_armadura, remove_armadura, detalha_armadura
from bd import nova_magia, atualizar_magia, listar_magia, remove_magia, detalha_magia

from bd import tabela

# Garantir que as tabelas sejam criadas
tabela()

app = Flask(__name__)

#########################################################

@app.route('/classes')
def classes_list():
    todas_classes = listar_classe()
    return render_template("/classes.html", Classes=todas_classes)

@app.route("/remover_classe/<int:chave>")
def apagar_classe(chave):
    remove_classe(chave)
    return redirect('/classes')

@app.route("/nova_classe", methods=['GET', 'POST'])
def cadastrar_classe():
    if request.method == 'POST':
        dados = request.form.to_dict()
        nova_classe(dados.get('nome'), dados.get('atr_conjuracao'))
        return redirect('/classes')
    return render_template('classes_forms.html', classe=None, title='Nova Classe')

@app.route("/editar_classe/<int:chave>", methods=['GET', 'POST'])
def editar_classe(chave):
    if request.method == 'POST':
        dados = request.form.to_dict()
        atualizar_classe(chave, dados.get('nome'), dados.get('atr_conjuracao'))
        return redirect('/classes')
    classe = detalha_classe(chave)
    return render_template('classes_forms.html', classe=classe, title='Editar Classe')

#########################################

@app.route('/armaduras')
def armaduras_list():
    todas_armaduras = listar_armadura()
    return render_template("/armaduras.html", Armaduras=todas_armaduras)

@app.route("/remover_armadura/<int:chave>")
def apagar_armadura(chave):
    remove_armadura(chave)
    return redirect('/armaduras')

@app.route("/nova_armadura", methods=['GET', 'POST'])
def cadastrar_armadura():
    if request.method == 'POST':
        dados = request.form.to_dict()
        nova_armadura(dados.get('nome'), dados.get('defesa'), dados.get('tipo'))
        return redirect('/armaduras')
    return render_template('armaduras_forms.html', armadura=None, title='Nova Armadura')

@app.route("/editar_armadura/<int:chave>", methods=['GET', 'POST'])
def editar_armadura(chave):
    if request.method == 'POST':
        dados = request.form.to_dict()
        atualizar_armadura(chave, dados.get('nome'), dados.get('defesa'), dados.get('tipo'))
        return redirect('/armaduras')
    armadura = detalha_armadura(chave)
    return render_template('armaduras_forms.html', armadura=armadura, title='Editar Armadura')

########################################

@app.route('/armas')
def armas_list():
    todas_armas = listar_arma()
    return render_template("armas.html", Armas=todas_armas)

@app.route("/remover_arma/<int:chave>")
def apagar_arma(chave):
    remove_arma(chave)
    return redirect('/armas')

@app.route("/nova_arma", methods=['GET', 'POST'])
def cadastrar_arma():
    if request.method == 'POST':
        dados = request.form.to_dict()
        nova_arma(dados.get('nome'), dados.get('propriedade'), dados.get('tipo'))
        return redirect('/armas')
    return render_template('armas_forms.html', arma=None, title='Nova Arma')

@app.route("/editar_arma/<int:chave>", methods=['GET', 'POST'])
def editar_arma(chave):
    if request.method == 'POST':
        dados = request.form.to_dict()
        atualizar_arma(chave, dados.get('nome'), dados.get('propriedade'), dados.get('tipo'))
        return redirect('/armas')
    arma = detalha_arma(chave)
    return render_template('armas_forms.html', arma=arma, title='Editar Arma')

################################

@app.route('/magias')
def magias_list():
    todas_magias = listar_magia()
    return render_template("magias.html", Magias=todas_magias)

@app.route("/remover_magia/<int:chave>")
def apagar_magia(chave):
    remove_magia(chave)
    return redirect('/magias')

@app.route("/nova_magia", methods=['GET', 'POST'])
def cadastrar_magia():
    if request.method == 'POST':
        dados = request.form.to_dict()
        nova_magia(dados.get('nome'), dados.get('nivel'), dados.get('alcance'))
        return redirect('/magias')
    return render_template('magias_forms.html', magia=None, title='Nova Magia')

@app.route("/editar_magia/<int:chave>", methods=['GET', 'POST'])
def editar_magia(chave):
    if request.method == 'POST':
        dados = request.form.to_dict()
        atualizar_magia(chave, dados.get('nome'), dados.get('nivel'), dados.get('alcance'))
        return redirect('/magias')
    magia = detalha_magia(chave)
    return render_template('magias_forms.html', magia=magia, title='Editar Magia')

if __name__ == '__main__':
    app.run()
