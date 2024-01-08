from api import create_app
from flask import g
import os

app = create_app()

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'mongo_db_client'):
        g.mongo_db_client.close()

if __name__ == '__main__':
    app.run(port=app.config['PORT'])