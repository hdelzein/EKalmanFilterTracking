
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

### Step Three. Implement the Measurement Module

The implementation of the file student\measurement.py functions followed the lectures and the excercise homework as a template:

The function 'fov' followed the lesson-4-MTT as a template
The function 'get_hx' followed the lesson-3-EKF file meanurment.py as a template
x
The results is shown below as an image of the RMSE values and as a video file below:

<img src="results/StepFour_RMSE.png"/>

The video is shown as a icon below. Due to size restrictions it cannot be displayed. Please click the icon and download to view it.

<img src="results/StepFour_my_tracking_results.avi"/>
