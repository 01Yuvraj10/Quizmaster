from app import create_app

app = create_app()

@app.route("/")
def home():
    return "Welcome to Quiz Master !"