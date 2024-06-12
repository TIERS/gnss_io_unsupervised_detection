from serial import Serial
from time import time
import pickle

from pyubx2 import UBXReader

# GNSS Receiver communication config
stream = Serial('/dev/ttyACM0', 38400, timeout=0.1)
ubr = UBXReader(stream)

# Test reading the data from the device
# Parsed data contains the attributes storing the information
(raw_data, parsed_data) = ubr.read()
# Print examples
print(f"Raw data: {raw_data} \n")
print(f"Parsed data: {parsed_data} \n")

# Create list to store all the messages from the receiver
GNSS_DATA_RAW = []
# Save the time the files is being created
file_ts = time()

# Create list to store the extracted lat, lon, and alt from the receiver
GNSS_DATA_POS = []

while True:
    try:
        # Retrive GNSS reciever messages
        (raw_data, parsed_data) = ubr.read()

        if parsed_data:
            # print(f'Raw Data: {raw_data}')
            meas_ts = time()
            GNSS_DATA_RAW.append(
                (parsed_data, meas_ts)
            )

            # Only pay attention to this specific message (contains position)
            if parsed_data.identity == 'NAV-PVT':
                meas_lon = parsed_data.lon
                meas_lat = parsed_data.lat
                meas_height = parsed_data.height
                meas_heighAboveSeaLvl = parsed_data.hMSL
                # Position tuple to store lat and lon
                position = (
                    meas_lat,
                    meas_lon,
                    meas_height,
                    meas_heighAboveSeaLvl,
                    meas_ts
                )
                # Save the tuple in the lat, lon list
                GNSS_DATA_POS.append(position)

    except KeyboardInterrupt:  # capture Ctrl-C
        print("\n\nTerminated by user.")
        break

with open(
    f'gnss_test_raw_data_{file_ts}.pickle',
    'wb'
) as handle:
    pickle.dump(
        GNSS_DATA_RAW,
        handle,
        protocol=pickle.HIGHEST_PROTOCOL
    )
print("\nMeasurements without processing file saved")

with open(
    f'gnss_extracted_pos_data_{file_ts}.pickle',
    'wb'
) as handle:
    pickle.dump(
        GNSS_DATA_POS,
        handle,
        protocol=pickle.HIGHEST_PROTOCOL
    )
print("\nPosition solution file saved")

