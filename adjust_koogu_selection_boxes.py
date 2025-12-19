import os
import pandas as pd
import soundfile as sf


def get_wav_duration(path):
    audio_info = sf.info(path)
    return audio_info.duration


if __name__ == '__main__':

    audio_folder = '' # Enter audio directory
    audio_files = sorted([f for f in os.listdir(audio_folder) if f.endswith('.wav')])

    # Build a timeline map of audio file offsets
    file_durations = {}
    for fname in audio_files:
        filepath = os.path.join(audio_folder, fname)
        try:
            file_durations[fname] = get_wav_duration(filepath)
        except RuntimeError:
            print(f"Could not read {fname}")

    # Build cumulative offset (filename -> total time from start)
    file_offsets = {}
    cumulative = 0.0
    for fname in audio_files:
        file_offsets[fname] = cumulative
        cumulative += file_durations.get(fname, 0)

    # Load Koogu detection file
    detection_file = '' # Enter file directory
    df = pd.read_csv(detection_file, sep='\t')
    df['dur'] = df['End Time (s)'] - df['Begin Time (s)']

    # Add offset time to each row based on 'Begin File'
    df['File Offset (s) 1'] = df['Begin File'].map(file_offsets)

    # Check if any files missing
    missing = df[df['File Offset (s) 1'].isna()]['Begin File'].unique()
    if len(missing) > 0:
        print("Warning: These files were not found in audio folder:")
        print(missing)

    # Update Begin/End times
    df['Begin Time (s)'] = df['File Offset (s)'] + df['File Offset (s) 1']
    df['End Time (s)'] = df['Begin Time (s)'] + df['dur']

    # Save the corrected table
    df.to_csv(':/Pathway/To/Your/Directory/AdjustedSelections.txt', sep='\t', index=False) #Edit this to your file directory
