from flask import Flask, render_template, redirect

app = Flask(__name__)


@app.route("/")
def home():
    return redirect("/login")


@app.route("/login")
def login():
    return render_template(
        "login.html",
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
            ]
        }
    )


@app.route("/registration")
def registration():
    return render_template("registration.html", title="Регистрация", nav={'authorized': False})


def main():
    app.run()


if __name__ == "__main__":
    main()
