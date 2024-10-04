from flask import Flask
from dotenv import load_dotenv
from flask_cors import CORS
import os

load_dotenv()

# ENV Vars
PORT = os.environ['PORT']

# Blueprints
from blueprints.treeEnum.treeEnum import treeEnum
from routes.user_routes import register_user

app = Flask(__name__)
CORS(app,origins=["http://localhost:5173"])
app.register_blueprint(treeEnum)
app.register_blueprint(register_user)

if __name__ == "__main__":
    app.run(port=PORT, debug=True)