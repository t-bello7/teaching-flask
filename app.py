from flask import Flask, render_template

# To change the defualt template folder we use the argument template_folder='<name_of_folder>'
# To change the default static folder we use the argument static_folder='<name_of_folder>'
app = Flask(__name__)

@app.route('/')
def index():
    # return 'Hello World Class Developers'
    return render_template('index.html')

@app.route('/whereami')
def whereami():
    return 'I am in ghana'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
