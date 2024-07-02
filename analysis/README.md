The files ending in *gnss_test_raw_data_XXXX.XXXX_features.pickle* are the output from the *reading_gnss_data* notebook. They contain only the features of interest extracted from the messages in the raw files.

# Usage example from research
- All raw files in the *data* folder can be passed to the *reading_gnss_data* notebook.
- The following files are used to make a comparison between outside and near indoors in the *processing_gnss_features* notebook:
    - *gnss_test_raw_data_1713259013.4408054_features*
    - *gnss_test_raw_data_1713259484.0477698_features*
    - The other files with *_features* can also run in the notebook. The difference is that some fields will be blanks or require some validation to ensure the features exist or need to be removed from the code.
- The following files are used with the *exploring_cno_io_transition* notebook:
    - *gnss_test_raw_data_1716472705.1320515_features*
    - *gnss_test_raw_data_1716473898.1400812_features*
    - *gnss_test_raw_data_1716475018.8516796_features*
    - *gnss_test_raw_data_1716535003.8263893_features*
    - The notebook is tailored for these files, although it should be possible to run the others but it might require some checking to see if they contain the features.
- The notebook *exploring_trajectories* uses raw data to extract the information. The files for this notebook are:
    - *gnss_test_raw_data_1716472705.1320515*
    - *gnss_test_raw_data_1716473898.1400812*
    - *gnss_test_raw_data_1716535003.8263893*
    - These are the only files that contain the data from the Camera IMU, the other files that don't contain these messages might have problem with the first section (or all the notebook)