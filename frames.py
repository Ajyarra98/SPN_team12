import os
import cv2

DATA_DIR = './rawdata'
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

labels = 4
dataset_size = 150
captured = cv2.VideoCapture(0)

def creating_frames():
    print('Collecting data for class {}'.format(j))
    done = False
    while True:
        ret, frame = captured.read()
        cv2.putText(frame, 'Press Q to begin new label collection)', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3,
                    cv2.LINE_AA)
        height, width, channels = frame.shape
        if width > 0 and height > 0: #checking for the height and width of the image
            cv2.imshow('frame', frame)
            if cv2.waitKey(25) == ord('q'):
                break
        else:
            print('Invalid image dimensions')

def creating_labels():
    counter = 0
    while counter < dataset_size:
        ret, frame = captured.read()
        cv2.imshow('frame', frame)
        cv2.waitKey(25)
        cv2.imwrite(os.path.join(DATA_DIR, str(j), '{}.jpg'.format(counter)), frame)

        counter += 1






for j in range(labels):
    if not os.path.exists(os.path.join(DATA_DIR, str(j))):
        os.makedirs(os.path.join(DATA_DIR, str(j)))

    creating_frames()  
    creating_labels()

    

 

captured.release()
cv2.destroyAllWindows()
