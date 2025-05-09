from app import create_app


app = create_app("development", "sqlite:///db/main.sqlite")

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080)
