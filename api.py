from flask import Flask, request, jsonify, send_file, url_for
from werkzeug.utils import secure_filename
from flask_cors import CORS
import os
from packages.get_splices import get_splices

app = Flask(__name__)
CORS(app, methods=['GET','POST'], origins=['http://localhost:3000', 'http://localhost:5000'])

@app.route('/video', methods=['POST'])
def video():
        
    # check if a file was uploaded
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'})
    
    video_file = request.files['file']
    
    # save the video file to disk
    video_filename = secure_filename(video_file.filename)
    video_path = os.path.join('uploaded_video/', video_filename)
    video_file.save(video_path)
            
    return get_splices()

# API endpoint to serve clips saved from video uploads
@app.route('/video/<filename>', methods=['POST','GET'])
def serve_clip(filename):
    
    video_path = os.path.join('spliced_video/', filename)
    return send_file(video_path, mimetype='video/mp4')

if __name__ == '__main__':
    app.run(debug=True)
