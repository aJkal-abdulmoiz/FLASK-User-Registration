from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

users = []

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        membership_length = int(request.form['membership_length'])
        
        if membership_length > 5:
            flash('Membership length cannot exceed 5 years.')
            return redirect(url_for('register'))
        
        price = 100 * membership_length
        
        users.append({'first_name': first_name, 'last_name': last_name, 'email': email, 'membership_length': membership_length, 'price': price})
        
        return render_template('registration_success.html', first_name=first_name, last_name=last_name, email=email, membership_length=membership_length, price=price)
        
    return render_template('register.html')

@app.route('/registration_success')
def registration_success():
    return render_template('registration_success.html')

@app.route('/')
def display_users():
    return render_template('users.html', users=users)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=56789, debug=True)
