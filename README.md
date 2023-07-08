Hand gesture recognition

libraries used till now :
1)pickle
2)mediapipe
3)cv2
4)matplotlib

Steps:
1) Firstly we have started by collecting the data needed for training , this is done by using cv2 library we have created frames of 6 different labels each label having 500 frames of dataset.
2) To do above we have written python script with filename frames.py and data collected is stored in rawdata folder.
3) Then we have done data preprocessing on the collected data by extracting the landmarks from each frame and plotted on a graph
4) Above training is done and the model is stored using 'data' pickle
# changes made by feature branch


