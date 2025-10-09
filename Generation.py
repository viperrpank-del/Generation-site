from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

def generate_password(complexity):
    if complexity == 'simple':
        # Простая сложность: только буквы и цифры
        characters = string.ascii_letters + string.digits
    else:
        # Сложная сложность: буквы, цифры и специальные символы
        characters = string.ascii_letters + string.digits + string.punctuation

    length = random.randint(8, 16)  # Случайная длина пароля от 8 до 16 символов
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

@app.route('/', methods=['GET', 'POST'])
def index():
    password = ''
    if request.method == 'POST':
        complexity = request.form.get('complexity')  # Получаем выбранную сложность
        password = generate_password(complexity)  # Генерация пароля в зависимости от сложности
    return render_template('index.html', password=password)

if __name__ == '__main__':
    app.run(debug=True)
