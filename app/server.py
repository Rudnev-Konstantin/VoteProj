from flask import Flask, render_template, redirect
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def home():
    return redirect("/login")


@app.route("/login")
def login():
    return "<h1>Страница входа</h1><p>В разработке</p>"


@app.route("/registration")
def registration():
    return "<h1>Страница регистрации</h1><p>В разработке</p>"


@app.route("/catalog")
def catalog():
    return render_template(
        "catalog.html",
        title="Вход",
        nav={
            'authorized': True,
            'name': "Фамилия Имя Отчество",
            'avatar': None,
            'is_user': True
        },
        main={
            'section_name': 'Каталог',
            'buttons': [
                {
                    'name': 'Изменить',
                    'id': 'edit'
                },
                {
                    'name': 'Добавить',
                    'id': 'add'
                }
            ],
            'contests': [
                {
                    'picture': None,
                    'name': 'Название',
                    'status': 0,
                    'location': 'г. Владикавказ, ул. Владикавказская 69Г',
                    'datetime': datetime.now().strftime('%Y-%m-%d %H:%M'),
                    'description': 'Описание'
                }
            ]
        }
    )


def main():
    app.run()


if __name__ == "__main__":
    main()
