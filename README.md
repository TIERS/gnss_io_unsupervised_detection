# Overview

This repository collects the necessary files to explore the feasibility of building a outdoor to indoor detection system using unsupervised machine learning techniques with the data from a GNSS Receiver.

# Dependencies

Install dependencies:
- poetry install
- pip install -r requirements.txt

The scripts and notebooks have been developed using Python 3.10

# Usage

Order in which the scripts were used during research:

1. Run *extraction/read_gnss_n9m.py*
    1. The code for extracting IMU data is currently commented in this repo.
    2. Without the IMU this will save a list of tuples in a .pickle file. The tuple is (timestamp, message)
2. Read the output of the previous script *(gnss_test_raw_data)* with the notebook *reading_gnss_data.ipynb*
   1. The first sections of the notebook gives information about the content of the pickle. Names and quantity of the messages and batches.
   2. The section **Extracting features ...** uses the result of the first sections to get a new .pickle file.
   3. The *gnss_test_raw_data_X_features* file has rows for each timestamp and the columns are the features extracted from the messages.
   4. The last section of the notebook is an example of extracting only one specific message type.
3. The *gnss_test_raw_data_X_features* is the input for the next notebook: *processing_gnss_features*. This notebook prepares the features for visualization and modelling.
   1. It is recommended to use two files for later comparison in the next sections. 
   2. The first section summarizes the features that are individual for each satellite into features per batch.
   3. The code in this notebooks is explorative, different parameters and settings are run for different features. Initial ideas for training the models and features for classification are also tested.
4. The notebook *exploring_cno_io_transition* also uses the he *gnss_test_raw_data_X_features* file. Here there is a more defined process of using the CNo feature with the OC-SVM model to finally implement the transition detection algorithm.
    1. The procedure explores different trajectories, it expects 4 files.

5. The notebook *exploring_trajectories* uses the coordinates from the camera and the GNSS receiver to draw the trajectories. The input data is the *gnss_test_raw_data* file and expects the messages to contain the solution message, and the file to also have the camera IMU coordinates as part of the tuple for each message (N rows, 4 columns).
    1. The camera x, y coordinates are plotted in a scatter plot. The trajectory from the GNSS solution is drawn over a specific map.


From 1 to 3 (and 4) things need to be in order. But 3 and 4 need the same file. Then 5 can be run separately once the *gnss_test_raw_data* is obtained.