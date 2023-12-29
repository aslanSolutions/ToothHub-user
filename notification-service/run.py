from api import create_app


app = create_app()
app.config['APIFAIRY_TITLE'] = 'Notification API'
app.config['APIFAIRY_VERSION'] = '1.0'

if __name__ == '__main__':
    app.run(port=5003)