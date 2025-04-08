from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Get form data
        username = request.form.get('username')
        email = request.form.get('email')
        return f'Signup successful! Welcome, {username} with email {email}.'
    
    # Render the signup form
    return render_template('signup.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)