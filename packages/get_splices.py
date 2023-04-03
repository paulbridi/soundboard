import os
from flask import request, jsonify

def get_splices():
    
    print('splice function called')
    # Try retrieving clips from /spliced_video
    try:
        
        clips = []
        clips_dir = 'spliced_video/'
        print(os.listdir(clips_dir)) 
        
        # Loop through each .mp4 clip in directory
        for filename in os.listdir(clips_dir):
            if filename.endswith('.mp4'):
                print(filename)
                
                # Create a dictionary object for each video clip
                video_clip = {
                    'filename': filename,
                    'url': f'{request.base_url}/{filename}'
                }
                clips.append(video_clip)
                
        # Return the video clips as the response
        return clips, 200
    
    # Return exception error if try fails
    except Exception as e:
        return str(e), 500
