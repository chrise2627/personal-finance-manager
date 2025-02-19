from backend import create_app

# Alternative way - also works but less common
from backend.__init__ import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True) 