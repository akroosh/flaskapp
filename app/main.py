from app import app
from app import db
import view

from movies.blueprint import movies

app.register_blueprint(movies, url_prefix = '/movies')

if __name__ == '__main__':
    app.run()
