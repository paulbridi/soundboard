import librosa
import os
from pydub import AudioSegment

def crop_save_oneshot(filepath, destpath, length=1, sr=44100):
    
    """
    Saves audio clip from first significant onset.

    Args:
        filepath (str): Path to the input video file.
        destpath (str): Path to where the output will be saved (ends in/)
        length (int, optional): Desired length in seconds of the audio clip (defaults to 1)
        sr (int, optional): Sampling rate of the input audio (defaults to 44100)
        
    """
    
    # Load the audio file
    audio, sr = librosa.load(filepath, sr=sr)

    # Calculate onset strength
    onset_env = librosa.onset.onset_strength(y=audio, sr=sr)

    # Get the index of the first significant onset
    onset_frames = librosa.onset.onset_detect(onset_envelope=onset_env, sr=sr, units='time')
    first_onset = onset_frames[0]

    # Convert the frame index to time (in seconds)
    start_time = librosa.frames_to_time(first_onset, sr=sr)


    # Convert start time to milliseconds
    start_time_0 = int(start_time * 1000)

    # Load the audio using pydub
    audio_segment = AudioSegment.from_file(filepath)

    # Extract the relevant portion of the audio
    relevant_audio = audio_segment[start_time_0:int(1000*length)]
    
    dest_string = destpath + os.path.basename(filepath)

    # Export the extracted audio to a new file
    relevant_audio.export(dest_string, format="wav")
