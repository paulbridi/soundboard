from flask import Flask, request, Response
from flask_cors import CORS, cross_origin

api = Flask(__name__)
cors = CORS(api, resources={r"/*": {"origins": "*"}})
api.config['CORS_HEADERS'] = 'Content-Type'

# API endpoint to take video input, return video (format of what's return tbd)
@api.route('/video', methods=['POST','GET'])
@cross_origin()
def video():
    if request.method == "POST":
        video = request.files['webcam'].stream.read()
        return Response(video, mimetype='video/x-matroska')
    
if __name__ == '__main__':
    api.run(debug=True)

