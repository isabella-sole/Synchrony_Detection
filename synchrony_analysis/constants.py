import os

# functions related to directories (folders) and files
# Structure of pose detection folders:
# Parent dir
#  - Video dir 1
#     - csv_files
#     - json file
#     - output_videos
#       + vid.avi
#     - video_info
#     - ...
#  - Video dir 2
#  - ...

# INPUT_FOLDER is the "Parent dir" as shown above
INPUT_FOLDER = ""
YOLO_INPUT_FOLDER = INPUT_FOLDER
# OUTPUT_FOLDER is normally the same "Parent dir"
OUTPUT_FOLDER = INPUT_FOLDER
# "C:\\Users\\Home - Jupiter\\Desktop\\DATA_HUB\\output_files_leap\\LP012_SyncCam_STT_Demo"

ORIGINAL_VIDEO_NAME = os.path.basename(INPUT_FOLDER)  # 'Camcorder 1_Eval room_STT.avi'  #  Note: include the
# file extension #
PREFIX = os.path.basename(INPUT_FOLDER) + '-'  # ORIGINAL_VIDEO_NAME[:ORIGINAL_VIDEO_NAME.rindex('.')] + '_'
JSON_FILE = 'PD-output.json'
JSON_SCORE_FILE = 'PD-per_frame_score.json'
JSON_SCORE_FILE_2 = 'PD-per_frame_score_2.json'
JSON_SCORE_FILE_3 = 'PD-per_frame_score_3.json'
JSON_COMBINED_FILE = 'PD-combined_output.json'
JSON_FILE_TEST = 'PD-output----test.json'
JSON_RELATIVE_1 = 'PD-relative_1.json'
JSON_RELATIVE_2 = 'PD-relative_2.json'
JSON_RELATIVE_3 = 'PD-relative_3.json'
JSON_SCORE_RELATIVE = 'PD-relative-per_frame_score.json'
JSON_SCORE_RELATIVE_2 = 'PD-relative-per_frame_score_2.json'
JSON_SCORE_RELATIVE_3 = 'PD-relative-per_frame_score_3.json'
JSON_COMBINED_RELATIVE = 'PD-relative-combined_output.json'

MATLAB_RAW_DATA_FILE = 'PD-raw_data.mat'
MATLAB_RAW_DATA_REMOVE_ZERO_DATA = 'PD-raw_data_remove_zero.mat'
MATLAB_INTERPOLATED_DATA = 'PD-interpolated_data.mat'
MATLAB_PREPROCESSED_DATA_FILE_EARLY = 'PD-preprocessed_data_early.mat'
MATLAB_PREPROCESSED_DATA_REMOVE_SHORT_NUM = 'PD-preprocessed_data_ready.mat'
MATLAB_PREPROCESSED_DATA_FILTERED = 'PD-preprocessed_data_filtered.mat'
MATLAB_PREPROCESSED_DATA_FINAL = 'PD-preprocessed_data_filtered.mat'  # preprocessed_data_final.mat'
MATLAB_MOVING_AVERAGE_DATA = 'PD-raw_data_moving_average.mat'
MATLAB_MOVING_AVERAGE_DATA_AFTER_PREPROCESS_EARLY = 'PD-preprocessed_early_moving_average.mat'
MATLAB_REMOVE_SUDDEN_AFTER_MA = 'PD-remove_sudden_after_ma.mat'
MATLAB_FACE_TO_OPENPOSE = 'PD-face_to_openpose.mat'

MATLAB_DATA_CHANGE = 'PD-data_change.mat'
MATLAB_BODY_PART_CHANGE_L2 = 'PD-body_part_change_l2.mat'

ANIMATION_VIDEO_POINTS = 'animation_vid_points.mp4'
ANIMATION_VIDEO_SKELETON = 'animation_vid_skeleton.mp4'

JSON_NAN_LIST = 'preprocessed_data_keypoints_nan_list.jsonl'
JSON_NONAN_LIST = 'preprocessed_data_keypoints_nonan_list.jsonl'

MATLAB_VECTORS = 'PD-vector_matrix.mat'
MATLAB_ANGLES = 'PD-angle_features.mat'
MATLAB_DISTANCES = 'PD-distance_features.mat'

MATLAB_TRAINING_INPUT_NO_NAN = "reaching_training_input_no_nan.mat"
MATLAB_TRAINING_OUTPUT_NO_NAN = 'reaching_training_labels_no_nan.mat'
MATLAB_TEST_INPUT_NO_NAN = 'reaching_test_input_no_nan.mat'
MATLAB_TEST_OUTPUT_NO_NAN = 'reaching_test_labels_no_nan.mat'

MATLAB_TRAINING_INPUT_NAN = "reaching_training_input_nan.mat"
MATLAB_TRAINING_OUTPUT_NAN = 'reaching_training_labels_nan.mat'
MATLAB_TEST_INPUT_NAN = 'reaching_test_input_nan.mat'
MATLAB_TEST_INPUT_NAN_ADD_NAN = 'reaching_test_input_nan_add_nan_at_col13.mat'
MATLAB_TEST_OUTPUT_NAN = 'reaching_test_labels_nan.mat'

MATLAB_TRAINING_INPUT_ANGLE_NAN_MONO = "PD-training_input-angle-nan-mono.mat"
MATLAB_TRAINING_INPUT_NAN_MONO = "PD-training_input-nan-mono.mat"
MATLAB_TRAINING_OUTPUT_NAN_MONO = 'PD-training_labels-nan-mono.mat'
MATLAB_TEST_INPUT_NAN_MONO = 'PD-test_input-nan-mono.mat'
MATLAB_TEST_OUTPUT_NAN_MONO = 'PD-test_labels-nan-mono.mat'

MATLAB_TRAINING_INPUT_NAN_STEREO = "reaching_training_input_nan_stereo.mat"
MATLAB_TRAINING_OUTPUT_NAN_STEREO = 'reaching_training_labels_nan_stereo.mat'
MATLAB_TEST_INPUT_NAN_STEREO = 'reaching_test_input_nan_stereo.mat'
MATLAB_TEST_OUTPUT_NAN_STEREO = 'reaching_test_labels_nan_stereo.mat'

MATLAB_TRAINING_INPUT_ALL_NUMBER_ANGLE_MONO = "PD-training_input-angle-all_number-mono.mat"
MATLAB_TRAINING_INPUT_ALL_NUMBER_MONO = "PD-training_input-all_number-mono.mat"
MATLAB_TRAINING_OUTPUT_ALL_NUMBER_MONO = 'PD-training_labels-all_number-mono.mat'
MATLAB_TEST_INPUT_ALL_NUMBER_MONO = 'PD-test_input-all_number-mono.mat'
MATLAB_TEST_OUTPUT_ALL_NUMBER_MONO = 'PD-test_labels-all_number-mono.mat'

MATLAB_TRAINING_INPUT_ALL_NUMBER_STEREO = "reaching_training_input_all_number_stereo.mat"
MATLAB_TRAINING_OUTPUT_ALL_NUMBER_STEREO = 'reaching_training_labels_all_number_stereo.mat'
MATLAB_TEST_INPUT_ALL_NUMBER_STEREO = 'reaching_test_input_all_number_stereo.mat'
MATLAB_TEST_OUTPUT_ALL_NUMBER_STEREO = 'reaching_test_labels_all_number_stereo.mat'

XGB_MODEL = 'xgb_reaching.json'
XGB_MODEL_NAN = 'xgb_reaching_nan.json'

KEYPOINTS_DICT = {0: "Nose",
                  1: "Neck",
                  2: "RShoulder",
                  3: "RElbow",
                  4: "RWrist",
                  5: "LShoulder",
                  6: "LElbow",
                  7: "LWrist",
                  8: "MidHip",
                  9: "RHip",
                  10: "RKnee",
                  11: "RAnkle",
                  12: "LHip",
                  13: "LKnee",
                  14: "LAnkle",
                  15: "REye",
                  16: "LEye",
                  17: "REar",
                  18: "LEar",
                  19: "LBigToe",
                  20: "LSmallToe",
                  21: "LHeel",
                  22: "RBigToe",
                  23: "RSmallToe",
                  24: "RHeel"}

CSV_HEADER_LST = []
for id, data in KEYPOINTS_DICT.items():
    CSV_HEADER_LST.append(data + ': X')
    CSV_HEADER_LST.append(data + ': Y')
    CSV_HEADER_LST.append(data + ': conf')
CSV_HEADER_LST.insert(0, 'IDs')
CSV_HEADER = ','.join(CSV_HEADER_LST)

TRACK_ID = False
SKELETON = False
KEYPOINT_ONLY = False
NO_HEADER = False
OUTPUT_TYPE = '.mp4'

LIST_OF_KEYPOINTS = ["Nose", "Neck", "RShoulder", "RElbow", "RWrist", "LShoulder", "LElbow", "LWrist",
                     "MidHip", "RHip", "RKnee", "RAnkle", "LHip", "LKnee", "LAnkle", "REye", "LEye", "REar",
                     "LEar", "LBigToe", "LSmallToe", "LHeel", "RBigToe", "RSmallToe", "RHeel"]

LIST_OF_LINKS = [["Nose", "Neck"], ["Neck", "RShoulder"], ["Neck", "LShoulder"],
                 ["RShoulder", "RElbow"], ["LShoulder", "LElbow"], ["RElbow", "RWrist"], ["LElbow", "LWrist"],
                 ["Neck", "MidHip"], ["MidHip", "RHip"], ["MidHip", "LHip"],
                 ["RHip", "RKnee"], ["LHip", "LKnee"], ["RKnee", "RAnkle"], ["LKnee", "LAnkle"],
                 ["REar", "REye"], ["LEar", "LEye"], ["REye", "Nose"], ["LEye", "Nose"],
                 ["RAnkle", "RBigToe"], ["LAnkle", "LBigToe"], ["RBigToe", "RSmallToe"], ["LBigToe", "LSmallToe"],
                 ["RAnkle", "RHeel"], ["LAnkle", "LHeel"]
                 ]

LIST_OF_KEYPOINTS_RELATIVE = ["Nose_Neck", "Neck", "RShoulder", "RElbow_RShoulder", "RWrist_RShoulder",
                              "LShoulder", "LElbow_LShoulder", "LWrist_LShoulder",
                              "MidHip", "RHip", "RKnee_RHip", "RAnkle_RHip",
                              "LHip", "LKnee_LHip", "LAnkle_LHip",
                              "REye_Neck", "LEye_Neck", "REar_Neck", "LEar_Neck"]

BODY_25_COLORS = [(255, 0, 85), (255, 0, 0), (255, 85, 0), (255, 170, 0), (255, 255, 0), (170, 255, 0), (85, 255, 0),
                  (0, 255, 0), (255, 0, 0), (0, 255, 85), (0, 255, 170), (0, 255, 255), (0, 170, 255), (0, 85, 255),
                  (0, 0, 255), (255, 0, 170), (170, 0, 255), (255, 0, 255), (85, 0, 255), (0, 0, 255), (0, 0, 255),
                  (0, 0, 255), (0, 255, 255), (0, 255, 255), (0, 255, 255)]
# CSV_FOLDER = OUTPUT_FOLDER + 'csv_files\\'
#
# if not os.path.exists(CSV_FOLDER):
#     os.makedirs(CSV_FOLDER)
#
# NO_CSV_FILES = len([name for name in os.listdir(CSV_FOLDER)
#                     if os.path.isfile(os.path.join(CSV_FOLDER, name))]) // 2
FRAME_RANGE = None

