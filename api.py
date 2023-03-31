from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app, methods=['GET','POST'], origins=['http://localhost:3000'])

# API endpoint to take video input, return video (format of what's return tbd)
@app.route('/api/video', methods=['POST'])
def video():
    video_file = request.files.get('file')
    
    # Pass video file to Python model and return the segmented data
    
    return {'name': 'John', 'age': 30}

if __name__ == '__main__':
    app.run(debug=True)

