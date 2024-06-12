from serial import Serial
from time import time
import pickle

from pyubx2 import UBXReader
import pyrealsense2

# GNSS Receiver config
stream = Serial('/dev/ttyACM0', 38400, timeout=0.1)
ubr = UBXReader(stream)

# # Declare RealSense pipeline, encapsulating the actual device and sensors
# pipe = pyrealsense2.pipeline()
# # Build config object and request pose data
# cfg = pyrealsense2.config()
# cfg.enable_stream(pyrealsense2.stream.pose)
# # Start streaming with requested config
# pipe.start(cfg)

(raw_data, parsed_data) = ubr.read()
print(f"Raw data: {raw_data} \n")
print(f"Parsed data: {parsed_data} \n")

GNSS_DATA_RAW = []
file_ts = time()

while True:
    try:
        # Retrive GNSS reciever messages
        (raw_data, parsed_data) = ubr.read()

        # # Wait for the next set of frames from the camera
        # frames = pipe.wait_for_frames()
        # # Fetch pose frame
        # pose = frames.get_pose_frame()

        # if pose:
        #     pose_data = pose.get_pose_data().translation

        if parsed_data:
            print(f'G: {raw_data}') # X: {pose_data.x}, Y:{pose_data.y}')
            meas_ts = time()
            GNSS_DATA_RAW.append(
                (parsed_data, meas_ts) #, pose_data.x, pose_data.y)
            )

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

print("\nProcessing complete")