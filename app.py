from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if request.method == 'POST':
        username = request.form['username']
        # Handle login logic here
        return render_template('dashboard.html', username=username)
    return render_template('dashboard.html', username="Guest")

@app.route('/orders')
def orders():
    return render_template('orders.html')

@app.route('/positions')
def positions():
    return render_template('positions.html')

@app.route('/funds')
def funds():
    return render_template('funds.html')

@app.route('/redirect')
def redirect_to_index():
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
