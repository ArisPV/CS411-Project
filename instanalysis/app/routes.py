from flask import url_for, render_template, request
from flask_uploads import UploadSet, configure_uploads, IMAGES
from app import app
#from json_parse import json_parse_labels
from google_cloud_interface import analyze_file
#from authlib.flask.client import OAuth
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from secrets import give_secrets
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
#configuring photo stuff
photos = UploadSet('photos', IMAGES)
app.config['UPLOADED_PHOTOS_DEST'] = 'static/img'
configure_uploads(app, photos)

secrets = give_secrets()

@app.route('/')
@app.route('/index')
def index():
	user = {'username': 'Kiran'}
	return render_template('index.html', title='Home', user=user)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
	user = {'username': 'Kiran'}
	if request.method == 'POST' and 'photo' in request.files:
		filename = photos.save(request.files['photo'])
		results = analyze_file('static/img/' + filename)
		return render_template('upload.html', title='Upload', user=user, file=filename, data=results)
	return render_template('upload.html', title='Upload', user=user)

@app.route('/login')
def login():
	redirect = {'url':"https://api.instagram.com/oauth/authorize/?client_id=" + secrets['client_id'] + "&redirect_uri=http://localhost:5000/auth&response_type=code"}
	return render_template('redirect.html', link=redirect)

@app.route('/auth', methods=['GET'])
def auth():
	#get and store code
	code = request.args['code']
	secrets['code'] = code
	#make post request to get token
	url = "https://api.instagram.com/oauth/access_token"
	fields = {
		'client_id'     : secrets['client_id'],
		'client_secret' : secrets['client_secret'],
		'grant_type'    : 'authorization_code',
		'redirect_uri'  : 'http://localhost:5000/auth',
		'code'          : code}
	postRequest = Request(url, urlencode(fields).encode())
	json = urlopen(postRequest).read().decode()
	obj = open('access_token.json', 'w')
	obj.write(json)
	obj.close()
	#go to homepage
	user = {'username': 'Kiran'}
	return render_template('index.html', title='Home', user=user)


