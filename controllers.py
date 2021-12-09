from flask import Flask, render_template, request, redirect
from db import mydb, mycursor


app = Flask(__name__)


@app.route('/')
def index():
    mycursor.execute("SELECT * FROM Plants")
    plants = mycursor.fetchall()
    return render_template('index.html', plants = plants)




@app.route('/gotoadmin')
def gotoadmin():
    mycursor.execute("SELECT * FROM Plants")
    plants = mycursor.fetchall()
    return render_template('admin.html', plants = plants)




@app.route('/add', methods=['GET', 'POST'])
def add_customer():
    if request.method == 'GET':
        return render_template('addplant.html')
    if request.method == 'POST':
        _plantname = request.form['plantname']
        _species = request.form['species']
        _manufacturer = request.form['manufacturer']
        _manufacturerlocation = request.form['manufacturerlocation']
        _price = request.form['price']
        _amountremaining = request.form['amountremaining']
        sql = 'INSERT INTO Plants (plantname, species, manufacturer, manufacturerlocation,price,amountremaining) VALUES (%s, %s, %s,%s, %s, %s)'
        val = (_plantname, _species, _manufacturer, _manufacturerlocation,_price, _amountremaining)
        mycursor.execute(sql, val)
        mydb.commit()
        mycursor.execute("SELECT * FROM Plants")
        plants = mycursor.fetchall()
        return render_template('addplant.html', plants = plants)




@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_plant(id):
    if request.method == 'GET':
        mycursor.execute(f'SELECT * FROM Plants WHERE ID={id}')
        plants = mycursor.fetchone()
        return render_template('edit.html', plants = plants)
    if request.method == 'POST':
        _plantname = request.form['plantname']
        _species = request.form['species']
        _manufacturer = request.form['manufacturer']
        _manufacturerlocation = request.form['manufacturerlocation']
        _price = request.form['price']
        _amountremaining = request.form['amountremaining']
        sql = f'UPDATE Plants SET plantname = %s, species = %s, manufacturer=%s, manufacturerlocation = %s, price = %s, amountremaining = %s  WHERE ID = %s'
        values = (_plantname, _species, _manufacturer, _manufacturerlocation,_price, _amountremaining,id)
        mycursor.execute(sql, values)
        mydb.commit()
        mycursor.execute("SELECT * FROM Plants")
        plants = mycursor.fetchall()
        return render_template('admin.html', plants = plants)


@app.route('/delete/<int:id>')
def delete_plant(id):
    sql = f'DELETE FROM Plants WHERE ID={id}'
    mycursor.execute(sql)
    mydb.commit()
    mycursor.execute("SELECT * FROM Plants")
    plants = mycursor.fetchall()
    return render_template('admin.html', plants = plants)


if __name__ == '__main__':
    app.run()