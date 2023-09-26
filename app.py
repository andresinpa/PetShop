from flask import Flask, redirect, render_template, request, url_for
from config import *


con_bd = EstablecerConexion()

app = Flask(__name__)
def crearTablaAnimales():
    cursor = con_bd.cursor()
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS animales(
                       id serial NOT NULL,
                       nombre character varying(30),
                       categoria character varying(30),
                       raza character varying,
                       edad character varying,
                       CONSTRAINT pk_animales_id PRIMARY KEY (id));
                   """)
    con_bd.commit()
@app.route('/')
def index():
    cursor = con_bd.cursor()
    sql = "SELECT*FROM animales"
    cursor.execute(sql)
    AnimalesRegistrados = cursor.fetchall()
    return render_template('index.html',datos=AnimalesRegistrados)

@app.route('/eliminar_animales/<string:id>')
def eliminar(id):
    cursor = con_bd.cursor()
    sql = """
            DELETE FROM animales WHERE id=%s;"""
    cursor.execute(sql,(id))
    return redirect(url_for('index'))

@app.route('/guardar_animales', methods=['POST'])
def agregarAnimal():
 
 cursor = con_bd.cursor()
 nombre = request.form['nombre']
 categoria = request.form['categoria']
 raza = request.form['raza']
 edad = request.form['edad']
 if nombre and categoria and raza and edad:
     sql="""INSERT INTO animales (nombre , categoria , raza, edad) VALUES (%s,%s,%s,%s);"""
     cursor.execute(sql,(nombre,categoria,raza,edad))
     con_bd.commit() 
     return redirect(url_for('index'))
 else:
     return "Error"
 
@app.route('/editar_animal/<string:id>', methods=['POST'])
def editar(id):
    cursor = con_bd.cursor()
    nombre = request.form['nombre']
    categoria = request.form['categoria']
    raza = request.form['raza']
    edad = request.form['edad']
    
    if nombre and categoria and raza and edad:
        sql= """UPDATE animales SET nombre= %s, categoria=%s, raza=%s, edad=%s WHERE id=%s"""
        cursor.execute(sql,(nombre,categoria,raza,edad,id))
        con_bd.commit()
    return redirect(url_for('index'))
if __name__== '__main__':
    crearTablaAnimales()
    app.run(debug=True)
    