# ---------------------------------------------------------------------
# Project "Track 3D-Objects Over Time"
# Copyright (C) 2020, Dr. Antje Muntzinger / Dr. Andreas Haja.
#
# Purpose of this file : Kalman filter class
#
# You should have received a copy of the Udacity license together with this program.
#
# https://www.udacity.com/course/self-driving-car-engineer-nanodegree--nd013
# ----------------------------------------------------------------------
#

# imports
import numpy as np

# add project directory to python path to enable relative imports
import os
import sys
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
import misc.params as params 

class Filter:
    '''Kalman filter class'''
    def __init__(self):
        pass

    def F(self):
        ############
        # TODO Step 1: implement and return system matrix F
        ############

        ####
        # Copied the template from the exercise lesson 3-EKF in the file filter.py
        dt = params.dt
        return np.matrix([[1, 0, 0, dt, 0,0],
                          [0, 1, 0, 0, dt, 0],
                          [0, 0, 1, 0, 0, dt],
                          [0, 0, 0, 1, 0, 0],
                          [0, 0, 0, 0, 1, 0],
                          [0, 0, 0, 0, 0 ,1]])

        
        ############
        # END student code
        ############ 

    def Q(self):
        ############
        # TODO Step 1: implement and return process noise covariance Q
        ############
        ####
        # Copied the template from the exercise lesson 3-EKF in the file filter.py
        q = params.q
        dt = params.dt
        ### This is a copy from the filter.py in the exercise homework
        q1 = ((dt ** 3) / 3) * q
        q2 = ((dt ** 2) / 2) * q
        q3 = dt * q

        # ## Q_orig without discretization is np.matrix(
        #                  [[0, 0, 0, 0, 0,0],
        #                   [0, 0, 0, 0, 0, 0],
        #                   [0, 0, 0, 0, 0, 0],
        #                   # [0, 0, 0, q, 0, 0],
        #                   [0, 0, 0, 0, q, 0],
        #                   [0, 0, 0, 0, 0 ,q]])


        #### integral of (F * Q_orig * F_T) with respect to time variable generate the matrix below
        Q = np.matrix([[q1, 0, 0, q2, 0,0],
                        [0, q1, 0, 0, q2, 0],
                        [0, 0, q1, 0, 0, q2],
                        [q2, 0, 0, q3, 0, 0],
                        [0, q2, 0, 0, q3, 0],
                        [0, 0, q2, 0, 0 ,q3]])

        return Q
        
        ############
        # END student code
        ############ 

    def predict(self, track):
        ############
        # TODO Step 1: predict state x and estimation error covariance P to next timestep, save x and P in track
        ############

        # Copied the template from the exercise lesson 3-EKF in the file filter.py
        F = self.F()
        x = track.x
        P = track.P
        x = F * x  # state prediction
        P = F * P * F.transpose() + self.Q()  # covariance prediction
        track.set_x(x)
        track.set_P(P)

        ############
        # END student code
        ############ 

    def update(self, track, meas):
        ############
        # TODO Step 1: update state x and covariance P with associated measurement, save x and P in track
        ############

        # Copied the template from the exercise lesson 3-EKF in the file filter.py
        gm = self.gamma(track, meas)
        H_M = meas.sensor.get_H(track.x)
        S = self.S(track, meas, H_M)
        K = track.P * H_M.transpose() * S.I
        x = track.x + K * gm
        P = (np.identity(params.dim_state) - K * H_M) * track.P
        track.set_x(x)
        track.set_P(P)
        ############
        # END student code
        ############ 
        track.update_attributes(meas)
    
    def gamma(self, track, meas):
        ############
        # TODO Step 1: calculate and return residual gamma
        ############

        ## hx = H*x for lidar from the hint that hx = H*x
        Hx = meas.sensor.get_hx(track.x)
        gma = meas.z - Hx
        return gma
        ############
        # END student code
        ############ 

    def S(self, track, meas, H):
        ############
        # TODO Step 1: calculate and return covariance of residual S
        ############

        P = track.P
        S = H * P * H.transpose() + meas.R
        return S
        
        ############
        # END student code
        ############ 