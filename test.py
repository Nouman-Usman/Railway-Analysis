from flask import Flask, redirect, url_for, session, request
from flask_oauthlib.client import OAuth

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my_secret_key'
oauth = OAuth(app)

# Replace these values with your own client ID and client secret from Google Developer Console
google = oauth.remote_app(
    'google',
    consumer_key='1001459857047-h269q1pgg1k51dhchebpu1vcr1qtc09o.apps".googleusercontent.com',
    consumer_secret='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',
    request_token_params={
        'scope': 'https://www.googleapis.com/auth/userinfo.profile'
    },
    base_url='https://www.googleapis.com/oauth2/v1/',
    request_token_url=None,
    access_token_method='POST',
    access_token_url='https://accounts.google.com/o/oauth2/token',
    authorize_url='https://accounts.google.com/o/oauth2/auth',
)

@app.route('/')
def index():
    if 'google_token' in session:
        me = google.get('userinfo')
        return f"Hello, {me.data['name']}! <a href='/logout'>Logout</a>"
    else:
        return '<a href="/login">Google Login</a>'

@app.route('/login')
def login():
    return google.authorize(callback=url_for('authorized', _external=True))

@app.route('/logout')
def logout():
    session.pop('google_token', None)
    return redirect(url_for('index'))

@app.route('/login/authorized')
def authorized():
    resp = google.authorized_response()
    if resp is None:
        return 'Access denied: reason=%s error=%s' % (
            request.args['error_reason'],
            request.args['error_description']
        )
    session['google_token'] = (resp['access_token'], '')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(port=8080)