from flask_manager import Manager,Shell
from app import db
from app import create_app

app = create_app('development')
manager = Manager(app)

if __name__ == "__main__":
    manager.run()
