
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

The implementation of the file student\trackingmanagement.py functions followed the instructions from the lectures and the template
from Lesson-4-MTT file initialization.py.
The functions '__init__' in the class 'Track' and the function 'manage_tracks' and 'handle_updated_track' successfully were created and 
it generated the following outcome for the RMSE graph:

<img src="results/stepTwo_RMSE.png"/>

