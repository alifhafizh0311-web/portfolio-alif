from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    button_python = False
    button_discord = False
    button_html = False
    button_db = False

    email = ""
    text = ""

    if request.method == 'POST':

        if request.form.get('button_python'):
            button_python = True

        if request.form.get('button_discord'):
            button_discord = True

        if request.form.get('button_html'):
            button_html = True

        if request.form.get('button_db'):
            button_db = True

        email = request.form.get('email')
        text = request.form.get('text')

        print("Email:", email)
        print("Pesan:", text)

    return render_template(
        'index.html',
        button_python=button_python,
        button_discord=button_discord,
        button_html=button_html,
        button_db=button_db
    )

if __name__ == "__main__":
    app.run(debug=True)