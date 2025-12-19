### Script to run Antarctic minke whale CNN detector presented in Darias-O'Hara et al. (In Review)
from koogu import recognize
import os
import pandas as pd

if __name__ == "__main__":

  Audio = ':\path\to\your\audio\files'
  Detections = ':\path\to\detections\''
  Model = ':\path\to\model'

  threshold = ## Adjust to selected threshold (i.e. 0.85)

  for fname in os.listdir(Audio):

    # build the path to the folder
    folder_path = os.path.join(Audio, fname)

    # build the expected detection file path
    detection_file = os.path.join(Detections, f"{fname}.txt")

    # skip if already processed
    if os.path.exists(detection_file):
      print(f"Skipping {fname} — already processed.")
      continue

    if os.path.isdir(folder_path):
      recognize(
        Model,
        folder_path,
        output_dir=Detections,
        threshold=threshold,
        reject_class=['Other', 'other'],  # Only output target class (i.e. BD)
        clip_advance=0.5,  # Can use different clip advance
        batch_size=32,  # Can increase depending on computational resources
        num_fetch_threads=4, # Parallel-process for speed
        process_subdirectories=True, # Process subdirectories also
        recursive=False,
        show_progress=True,
        combine_outputs=True,
      )

      # Rename and modify the output file
      original_file = os.path.join(Detections, 'results.selections.txt')
      new_file = detection_file

      if os.path.exists(original_file):
        os.rename(original_file, new_file)

        try:
          # Attempt to read and process the detection results
          df = pd.read_csv(new_file, sep='\t', skiprows=1, header=None)

          df.columns = [
            'Selection', 'Channel', 'Begin Time (s)', 'End Time (s)',
            'Low Freq (Hz)', 'High Freq (Hz)', 'Tags', 'Score',
            'File Offset (s)', 'Begin File'
          ]

          df.to_csv(new_file, sep='\t', index=False)

        except pd.errors.EmptyDataError:
          print(f"File is empty after skipping header: {new_file}")
          continue