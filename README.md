# PY-HP-GPIB-232CT-A
HP Plotter control software for NI GPIB-232CT-A 

Python software to control a National Instruments GPIB-232CT-A controller to transfer HP-GL plots incl. conversion HP-GL/2 to HP-GL to a HP plotter like HP 9872B with HP-IB / GPIB interface. On the PC side RS232 is used to connect the GPIB-232CT-A. The plotter has a HP-IB / GPIB interface. The challenge is that a direct 1 to 1 transmission of HP-GL commands via the GPIB-232CT-A is not possible. For each GPIB command, the controller requires commands in advance to which address the GPIB command should be sent. In addition, there is also the change between TALK and LISTEN, which must also be controlled separately. This is necessary so that the controller does not flood the plotter with commands. 

The following HP plotters were tested:
HP 9872B
HP 9872C
