from flask import Flask, request, jsonify, send_file, url_for
from werkzeug.utils import secure_filename
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app, methods=['GET','POST'], origins=['http://localhost:3000', 'http://localhost:5000'])

@app.route('/video', methods=['POST','GET'])
def video():
        
    # check if a file was uploaded
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'})
    
    video_file = request.files['file']
    
    # save the video file to disk
    video_filename = secure_filename(video_file.filename)
    video_path = os.path.join('video_upload/', video_filename)
    video_file.save(video_path)
    
    # return a URL to the video file
    video_url = url_for('serve_video', filename=video_filename, _external=True)
    return jsonify({'url': video_url})

# API endpoint to serve a video file from video uploads
@app.route('/video/<filename>', methods=['POST','GET'])
def serve_video(filename):
    
    video_path = os.path.join('video_upload/', filename)
    return send_file(video_path, mimetype='video/mp4')

if __name__ == '__main__':
    app.run(debug=True)
