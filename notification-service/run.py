from api import create_app
from flask_mail import Mail


app = create_app()
mailObj = Mail()
app.config['APIFAIRY_TITLE'] = 'Notification API'
app.config['APIFAIRY_VERSION'] = '1.0'

if __name__ == '__main__':
    app.run()