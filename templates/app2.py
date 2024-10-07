from flask import Flask, render_template, request, send_file
import os

app = Flask(__name__)

# Укажите путь к файлам для знаков тары
glass_signs_file = 'Знаки_для_тары_Стекло.txt'  # Замените на ваш путь
doypack_signs_file = 'Знаки_для_тары_Дойпак.txt'  # Замените на ваш путь

@app.route('/')
def index():
    templates = ['Кетчуп', 'Соус', 'Борщ', 'Солянка', 'Щи', 'Сок', 'Томатная паста', 'Дойпак с ягодами']
    return render_template('index.html', templates=templates)

@app.route('/generate', methods=['POST'])
def generate_label():
    # Получаем данные из формы
    manufacturer = request.form.get('manufacturer')
    product_name = request.form.get('product_name')
    composition = request.form.get('composition')
    container_type = request.form.get('container_type')  # Получаем выбранный тип тары

    # Создаем текст этикетки
    label_text = f"Изготовитель: {manufacturer}\nПродукт: {product_name}\nСостав: {composition}\n"

    # Сохраняем текст этикетки как файл
    label_filename = "label.txt"
    with open(label_filename, "w", encoding="utf-8") as label_file:
        label_file.write(label_text)

    # Определяем файл знаков для выбранной тары
    if container_type == 'glass':
        signs_file = glass_signs_file
        signs_filename = "Знаки_для_тары_Стекло.txt"
    elif container_type == 'doypack':
        signs_file = doypack_signs_file
        signs_filename = "Знаки_для_тары_Дойпак.txt"

    # Возвращаем файл знаков для скачивания
    return send_file(signs_file, as_attachment=True, download_name=signs_filename)

if __name__ == "__main__":
    app.run(debug=True)
