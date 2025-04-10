from flask import Flask, render_template, request, redirect, url_for
import pymysql

app = Flask(__name__)

# Configure MySQL connection
db_config = {
    'host': 'suranardsdemo.cdtqd6jgia7i.ap-south-1.rds.amazonaws.com',
    'user': 'admin',
    'password': 'test1234',
    'database': 'mysqldemo'
}


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/customers')
def view_customers():
    print("view customers")
    connection = pymysql.connect(**db_config)
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM customers")
            customers = cursor.fetchall()
            for customer in customers:
                print(customer[0], customer[1], customer[2], customer[3])
    finally:
        connection.close()
    return render_template('view_customers.html', customers=customers)

@app.route('/add_customer', methods=['GET', 'POST'])
def add_customer():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']       


        connection = pymysql.connect(**db_config)
        try:
            with connection.cursor() as cursor:
                sql = "INSERT INTO customers (name, email, phone) VALUES (%s, %s, %s)"
                cursor.execute(sql, (name, email, phone))
            connection.commit()
        finally:
            connection.close()

        return redirect(url_for('view_customers'))
    return render_template('add_customer.html')

@app.route('/edit_customer/<int:id>', methods=['GET', 'POST'])
def edit_customer(id):
    print("edit customer::",id)

    
    connection = pymysql.connect(**db_config)

    if request.method == 'GET':
        with connection.cursor() as cursor:

            cursor.execute("SELECT * FROM customers WHERE id=%s", (id,))
            customer = cursor.fetchone()
            print("customer::",customer)
        return render_template('edit_customer.html', customer=customer)
    try:
        with connection.cursor() as cursor:
            if request.method == 'POST':
                name = request.form['name']
                email = request.form['email']
                phone = request.form['phone']
                sql = "UPDATE customers SET name=%s, email=%s, phone=%s WHERE id=%s"
                cursor.execute(sql, (name, email, phone, id))
                connection.commit()
                return redirect(url_for('view_customers'))
            else:
                cursor.execute("SELECT * FROM customers WHERE id=%s", (id,))
                customer = cursor.fetchone()
                print("customer::",customer)
    finally:
        connection.close()
    return render_template('edit_customer.html', customer=customer)
    

@app.route('/delete_customer/<int:id>', methods=['GET','POST'])
def delete_customer(id):
    print("delete customer::",id)
    connection = pymysql.connect(**db_config)
    try:
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM customers WHERE id=%s", (id,))
            connection.commit()
    finally:
        connection.close()
    return redirect(url_for('view_customers'))

if __name__ == '__main__':
    app.run(debug=True)