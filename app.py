# app.py

from flask import Flask, request, render_template, redirect, url_for, session
from authlib.integrations.flask_client import OAuth
import os

app = Flask(__name__)

app.secret_key = os.urandom(24)

# OAuth configuration
oauth = OAuth(app)
google = oauth.register(
    name='google',
    client_id='1054102825696-g7qu0to291e1chetm7sc4q0g9nave00a.apps.googleusercontent.com',  # Replace with your client ID
    client_secret='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',  # Replace with your client secret
    #access_token_url='https://accounts.google.com/o/oauth2/token',
    #access_token_params=None,
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    #authorize_params=None,
    api_base_url='https://www.googleapis.com/oauth2/v1/',
    client_kwargs={'scope': 'openid email profile'},
    server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
    claims_options={'iss': {'essential': True, 'values': ['https://accounts.google.com']}}
)

app_env = os.getenv('APP_ENV', 'local')  # Default to 'local' if not set



@app.route('/', methods=['GET', 'POST'])
def index_page():
    return render_template('index.html', title='Home')

@app.route('/reverse', methods=['GET', 'POST'])
def reverse_word():
    reversed_word = ''
    if request.method == 'POST':
        word = request.form['word']
        reversed_word = word[::-1]
    return render_template('reverse.html', reversed_word=reversed_word)

@app.route('/login')
def login():
    # Redirect the user to Google's OAuth 2.0 consent page
    scheme = 'http' if app_env == 'local' else 'https'
    redirect_uri = url_for('auth_callback', _external=True, _scheme=scheme)
    return google.authorize_redirect(redirect_uri)


@app.route('/callback')
def auth_callback():
    # Handle the response from Google's OAuth 2.0 server
    token = google.authorize_access_token()
    user_info = google.get('userinfo').json()
    session['profile'] = user_info
    return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    # Show the user's profile information if they are logged in
    user_info = session.get('profile')
    if user_info:
        return render_template('dashboard.html', user_info=user_info)
    return redirect('/')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
