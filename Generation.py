from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

def generate_password():
    length = random.randint(8, 16)  # Случайная длина пароля от 8 до 16 символов
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

@app.route('/', methods=['GET', 'POST'])
def index():
    password = ''
    if request.method == 'POST':
        password = generate_password()  # Генерация пароля при нажатии кнопки
    return render_template('index.html', password=password)

if __name__ == '__main__':
    app.run(debug=True)
