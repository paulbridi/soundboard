from moviepy.video.io.VideoFileClip import VideoFileClip

def extract_audio_clip(src_video_path, dest_path, file_name, start_time=None, end_time=None):
    ''' Take source path, destination path, filename (no extension), start and end times as input to save .wav audio clip to the specified path'''
       
    # Load the video file
    video_clip = VideoFileClip(src_video_path)

    # Set the start and end times
    start_time = start_time or 0
    end_time = end_time or video_clip.duration

    # Get the audio from the video for the specified time interval
    audio_clip = video_clip.subclip(start_time, end_time).audio

    # Write the audio to a WAV file
    audio_clip.write_audiofile(dest_path + file_name + '.wav')

    # Close the video and audio clips
    video_clip.close()
    audio_clip.close()

