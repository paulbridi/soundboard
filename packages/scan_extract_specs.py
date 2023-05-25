import librosa
import numpy as np

def scan_extract_specs(video_path, clip_length=1, hop_length=0.2, desired_sampling_rate=44100):
    """
    Extracts spectrograms from the audio of a video file using a sliding window approach.

    Args:
        video_path (str): Path to the video file.
        clip_lenth (int, optional): Length in num of seconds of the sampled audio
        hop_length (int, optional): Length in num of seconds of the interval used to slide across the audio
        desired_sampling_rate (int, optional): Sampling rate of the input audio
    
    Returns:
        List of tuples, where each tuple contains the start and end times of an audio clip (in seconds) and its spectrogram.
    """
    
    # Load the audio file
    audio, sr = librosa.load(video_path, sr=desired_sampling_rate)

    # Pad the audio with zeros if necessary
    samples_to_pad = int(clip_length * sr) - (len(audio) % int(clip_length * sr))

    if samples_to_pad > 0:
        audio = np.concatenate((audio, np.zeros(samples_to_pad)))

    # Convert time intervals to samples
    clip_samples = int(clip_length * sr)
    hop_samples = int(hop_length * sr)

    # Calculate the number of clips and the shape of the spectrograms
    n_clips = int(np.ceil(len(audio) / hop_samples)) - int(np.ceil(samples_to_pad / hop_samples))
    spec_shape = librosa.feature.melspectrogram(y=audio[:clip_samples], sr=desired_sampling_rate).T.shape

    # Create arrays to store the spectrograms and clip timestamps
    spectrograms = np.zeros((n_clips, spec_shape[0], spec_shape[1]), dtype=np.float32)
    clip_times = []

    # Iterate over the audio and create spectrograms for each clip
    for i in range(n_clips):
        # Calculate the start and end samples for the clip
        start_sample = i * hop_samples
        end_sample = start_sample + clip_samples

        # Extract the audio clip
        audio_clip = audio[start_sample:end_sample]

        # Calculate the spectrogram for the audio clip
        spectrogram = librosa.feature.melspectrogram(y=audio_clip, sr=desired_sampling_rate).T

        # Store the spectrogram and clip start time
        spectrograms[i, :, :] = spectrogram
        clip_times.append((start_sample / desired_sampling_rate , (start_sample / desired_sampling_rate)+ clip_length))

    return spectrograms, clip_times