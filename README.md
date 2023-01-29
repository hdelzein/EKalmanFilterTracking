
# SDCND : Sensor Fusion and Tracking

## Projects Steps detailed explanations below

### Step One. Implement Extend Kalman Filter

The implementation of the file 'student\filter.py' successfully outcomed the RMSE values shown in the image below:

<img src="results/StepOne_RMSE.png"/>

The image of tracking the vehicle is shown below:

<img src="results/StepOne_FinalImage.png"/>

The implementation was based on the template from the exercises homework lesson-3-EKF in the file filter.py and on the project hint that 
hx = H*x.


### Step Two. Implement the Tracking Module

The implementation of the functions in the  student\trackingmanagement.py file followed the instructions from the lectures and the template
from Lesson-4-MTT file initialization.py.
The functions '__init__' in the class 'Track' and the function 'manage_tracks' and 'handle_updated_track' successfully were created and 
it generated the following outcome for the RMSE graph:

<img src="results/stepTwo_RMSE.png"/>

### Step Three. Implement the Association Module

The implementation of the file student\association.py functions followed the lectures and the excercise homework as a template:

The function 'associate' used the 'associate' function in lesson-4-MTT as a template
The function 'MHD','gating' and 'get_closest_track_and_meas' used the equivalent functions in exercise lesson-4-MTT as a template.

The results is shown below as an image of the RMSE values and as a video file below:


<img src="results/StepThree_RMSE.png"/>

The video is shown as a icon below. Due to size restrictions it cannot be displayed. Please click the icon and download to view it.

<img src="results/Step_Three_my_tracking_results.avi"/>

As shown in the 'AVI' file there is a significant number of false positive when working with Lidar alone. For example the trace below:
````
processing frame #10
loading lidar point-cloud from result file
loading birds-eve view from result file
loading detected objects from result file
loading object labels and validation from result file
loading detection performance measures from file
predict track 0
predict track 1
update track 1 with lidar measurement 1
update track 0 with lidar measurement 0
creating track no. 2
track 0 score = 1
track 1 score = 1
track 2 score = 0.16666666666666666
track 0 score = 1
track 1 score = 1
track 2 score = 0.16666666666666666
Saving frame C:\objectDetProject\results\frameImages\tracking010.png

`````

The image below Shows that a new track shown in red is actaully not a vehicle but a tree even though the Lidar generated a false positive. 

<img src="results/StepThree_tracking010.png"/>

Lidar by itself as the video shows generated a significant number of false positives



### Step Three. Implement the Measurement Module

The implementation of the file student\measurement.py functions followed the lectures and the excercise homework as a template:

The function 'fov' followed the lesson-4-MTT as a template
The function 'get_hx' followed the lesson-3-EKF file meanurment.py as a template
x
The results is shown below as an image of the RMSE values and as a video file below:

<img src="results/StepFour_RMSE.png"/>

The video is shown as a icon below. Due to size restrictions it cannot be displayed. Please click the icon and download to view it.

<img src="results/StepFour_my_tracking_results.avi"/>

As shown in the 'AVI' file the Lidar false positives were removed. For example the trace for the same frame 10 shown above 
with sensor fusion is as follow. The camera fusion deleted the false psoitive.

````
processing frame #10
loading lidar point-cloud from result file
loading birds-eve view from result file
loading detected objects from result file
loading object labels and validation from result file
loading detection performance measures from file
predict track 0
predict track 1
update track 1 with lidar measurement 1
update track 0 with lidar measurement 0
creating track no. 2
track 0 score = 1
track 1 score = 1
track 2 score = 0.16666666666666666
update track 1 with camera measurement 4
update track 0 with camera measurement 3
---no more associations---
deleting track no. 2
track 0 score = 1
track 1 score = 1
Saving frame C:\objectDetProject\results\frameImages\tracking010.png

`````

Shows that a new track shown in red in the image below is actaully not a vehicle but a tree. 

<img src="results/Step4_tracking010.png"/>
