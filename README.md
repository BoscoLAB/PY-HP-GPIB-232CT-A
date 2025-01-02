## PY-HP-GPIB-232CT-A
# HP Plotter control software for NI GPIB-232CT-A 

The software is still under development and is a beta version! The translation from HP-GL/2 to HP-GL is still incomplete!

![NI-GPIB-232CT-A](https://github.com/user-attachments/assets/75a0002e-42bc-412a-82a2-8ed0126918e5)

Python software to control a National Instruments GPIB-232CT-A controller to transfer HP-GL plots incl. conversion HP-GL/2 to HP-GL to a HP plotter like HP 9872B with HP-IB / GPIB interface. On the PC side RS232 is used to connect the GPIB-232CT-A. The plotter has a HP-IB / GPIB interface. The challenge is that a direct 1 to 1 transmission of HP-GL commands via the GPIB-232CT-A is not possible. For each GPIB command, the controller requires commands in advance to which address the GPIB command should be sent. In addition, there is also the change between TALK and LISTEN, which must also be controlled separately. This is necessary so that the controller does not flood the plotter with commands. 

The software is still under development and is a beta version! The translation from HP-GL/2 to HP-GL is still incomplete!

![HP-GL Plotter Control](https://github.com/user-attachments/assets/0848364b-87ea-4647-bc60-b15ae2334101)

# The following HP plotters were tested:

- HP 9872B
- HP 9872C

# Here is an example of how the software works:

HP Plotter Control software for NI GPIB-232CT-A Demo: https://youtu.be/bWLo2th_44o?si=Pba61OVcQiW6J4Hu

# Plots HP9872C

![cassini_plot](https://github.com/user-attachments/assets/ac681042-6432-4ee7-8738-dcf48fa3b8af)
![perseverance_plot](https://github.com/user-attachments/assets/e32b1b0b-51c4-492f-a998-b91bbef874a4)
![deepspace_plot](https://github.com/user-attachments/assets/2645849c-a006-4be4-aba1-4bd0d0e28021)
![voyager_plot](https://github.com/user-attachments/assets/cdc59640-01db-4606-82f9-7aa40cf14b3d)
![skylab_plot](https://github.com/user-attachments/assets/884368df-3aba-4352-97c3-04de5910c3d5)
