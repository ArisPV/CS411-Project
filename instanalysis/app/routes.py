from flask import render_template, request
from flask_uploads import UploadSet, configure_uploads, IMAGES
from app import app
#from json_parse import json_parse_labels
from google_cloud_interface import analyze_file

photos = UploadSet('photos', IMAGES)

#test = analyze_file('static/img/mangoBobHD.png')
#print(test)
# it worked yo

app.config['UPLOADED_PHOTOS_DEST'] = 'static/img'
configure_uploads(app, photos)

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