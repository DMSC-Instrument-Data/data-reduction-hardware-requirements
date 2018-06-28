# Create a user file to run SANS2DSlicingTest_V2.SANS2DMinimalBatchReductionSlicedTest_V2 with scaled bin count.
import sys

factor = float(sys.argv[1])

template="""PRINT for changer
MASK/CLEAR
MASK/CLEAR/TIME
L/WAV 1.5 12.5 {:f}/LIN

L/Q .001,{:f},.0126,{:f},.2
!L/Q .001 .8 .08/log
L/QXY 0 0.05 .001/lin
BACK/M1 35000 65000
BACK/M2 85000 98000
DET/REAR
GRAVITY/ON
!FIT/TRANS/OFF
FIT/TRANS/LOG 1.5 12.5
mask/rear h0
mask/rear h190>h191
mask/rear h167>h172
mask/rear v0
mask/rear v191
mask/front h0
mask/front h190>h191
mask/front v0
mask/front v191
! dead wire near top
mask/front h156>h159
!masking off beamstop arm - 12mm wide @ 19degrees
!mask/rear/line 12 19 
! spot on rhs beam stop at 11m
! mask h57>h66+v134>v141
!
! mask for Bragg at 12m, 26/03/11, 3 time channels
mask/time 17500 22000
!
L/R 41 -1 3
!L/Q/RCut 200
!L/Q/WCut 8.0
!PRINT REMOVED RCut=200 WCut=8
!
MON/DIRECT=DIRECTM1_15785_12m_31Oct12_v12.dat
MON/TRANS/SPECTRUM=1/INTERPOLATE
MON/SPECTRUM=1/INTERPOLATE
TRANS/TRANSPEC=3
!TRANS/TRANSPEC=4/SHIFT=-70
!
set centre 155.45 -169.6 5.1 5.1
!
! 25/10/13 centre gc 22021, fit gdw20 22023
set scales 0.074 1.0 1.0 1.0 1.0
! correction to actual sample position, notionally 81mm before shutter
SAMPLE/OFFSET +53.0
! Correction to SANS2D encoders in mm 
DET/CORR REAR X -16.0
DET/CORR REAR Z 47.0
DET/CORR FRONT X -44.0
DET/CORR FRONT Y -20.0
DET/CORR FRONT Z 47.0
DET/CORR FRONT ROT 0.0
!
!! 01/10/13 MASKSANS2d_133F M3 by M1 trans Hellsing, Rennie, Jackson, L1=L2=12m A1=20 and A2=8mm
L/EVENTSTIME 7000.0,{:f},60000.0"""

print(template.format(0.125/factor, 0.01/factor, -0.08/factor, 500.0/factor))
