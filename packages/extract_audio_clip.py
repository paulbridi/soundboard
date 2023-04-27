from moviepy.video.io.VideoFileClip import VideoFileClip

def extract_audio_clip(video_path, file_name, start_time=None, end_time=None):
    ''' Take video path, start and end times as input and output .wav audio clip to the specified path'''
       
    # Load the video file
    video_clip = VideoFileClip(video_path)

    # Set the start and end times
    start_time = start_time or 0
    end_time = end_time or video_clip.duration

    # Get the audio from the video for the specified time interval
    audio_clip = video_clip.subclip(start_time, end_time).audio

    # Write the audio to a WAV file
    audio_clip.write_audiofile('../tmp_sliced_audio/'+ file_name)

    # Close the video and audio clips
    video_clip.close()
    audio_clip.close()
