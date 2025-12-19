Antarctic minke whale machine learning detector
Darias-O’Hara et al. (In review)
Overview of the detector 
This detector was developed using Koogu v0.7.2 (Madhusudhana, 2023), an open-source framework for machine learning from bioacoustics datasets, based on TensorFlow 2.9.0 framework (TensorFlow Developers, 2022) and Python 3.10 (Python Software Foundation, 2021). A quasi-DenseNet CNN architecture was selected. 
This detector identifies Antarctic minke whale bio-duck vocalisations. Positive detections are labelled as “BD” under the “Tags” column in the resulting RavenPro selections tables.  
System requirements
This detector can run on Linux, macOS, or Windows with Python 3.8–3.11 and standard scientific libraries (numpy, pandas, scipy, soundfile, plus PyTorch or TensorFlow). Ensure that koogu is installed. Whilst it will work on a CPU, using an NVIDIA GPU with CUDA support is recommended for much faster processing, especially when working with large audio datasets or training models.
Quick start guide 
Koogu documentation and quick start guide is available here (https://shyamblast.github.io/Koogu/en/v0.7.1/quickstart.html). 
Two .py scripts are provided alongside the detector. These include “find_Aminke.py” and “adjust_koogu_selection_boxes.py”. Additionally, a folder “Aminke_DetectorFiles” is provided, containing the model and required documentation. 
For large datasets, it is recommended that the audio be split into monthly folders as the detector will run recursively (when recursive = True in find_Aminke.py) and provide a RavenPro selections table for each month (when combine_outputs = True in find_Aminke.py). 
To use this detector, first set up find_Aminke.py to your directories and settings. 
Post processing of selections tables 
Once the detector run is complete, use “adjust_koogu_selection_boxes.py” to align the Koogu outputs (RavenPro selections tables) with the full audio timeline when detections span across multiple audio files. This script scans the target audio folder, calculates the duration of each file, and builds a cumulative offset map so each file’s start time is correctly placed on the global timeline. The script then loads the selections table .txt file, adjusts the “Begin Time” and “End Time” values by adding the correct file offset, and outputs a new corrected detection table (AdjustedSelections.txt). To use it, specify the audio folder path containing the .wav files and the Koogu detection file path, then run the script. The result ensures that detections line up properly when visualized in RavenPro 1.6.
References 
Madhusudhana, S. (2023). shyamblast/Koogu: v0.7.2. In.
Python Software Foundation. (2021, October 4, 2021). Python Language Reference, version 3.10.0. Python Software Foundation. Retrieved July 7 from https://docs.python.org/3.10/reference/
TensorFlow Developers. (2022, July 7, 2025). Tensorflow version 2.9.0. Zenodo. https://doi.org/10.5281/zenodo.5949120

