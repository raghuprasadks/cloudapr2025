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

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        # Save to MySQL database using pymysql
        connection = pymysql.connect(**db_config)
        try:
            with connection.cursor() as cursor:
                sql = "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)"
                cursor.execute(sql, (name, email, password))
            connection.commit()
        finally:
            connection.close()

        return redirect(url_for('home'))
    return render_template('signup.html')

if __name__ == '__main__':
    app.run(debug=True)