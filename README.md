## PY-HP-GPIB-232CT-A
# HP Plotter control software for NI GPIB-232CT-A 

![NI-GPIB-232CT-A](https://github.com/user-attachments/assets/75a0002e-42bc-412a-82a2-8ed0126918e5)

Python software to control a National Instruments GPIB-232CT-A controller to transfer HP-GL plots incl. conversion HP-GL/2 to HP-GL to a HP plotter like HP 9872B with HP-IB / GPIB interface. On the PC side RS232 is used to connect the GPIB-232CT-A. The plotter has a HP-IB / GPIB interface. The challenge is that a direct 1 to 1 transmission of HP-GL commands via the GPIB-232CT-A is not possible. For each GPIB command, the controller requires commands in advance to which address the GPIB command should be sent. In addition, there is also the change between TALK and LISTEN, which must also be controlled separately. This is necessary so that the controller does not flood the plotter with commands. 

# The following HP plotters were tested:

- HP 9872B
- HP 9872C

# The following HP plotters were tested

<iframe width="560" height="315" src="https://www.youtube.com/embed/bWLo2th_44o?si=3zSs1uyg1cIk9ePh" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
