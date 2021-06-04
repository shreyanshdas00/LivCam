# LivCam

A basic videocalling app illustrating the principles of image processing, computer networks and socket programming.

A basic interface is up and running, the front-end is still under development.


# Description of code:

1. servercv.py: The server script. Implements the server side of the program.

2. clientcv.py: The client script. Implements the client side of the program.

3. callcv.py: Implements the Call class to store and facilitate the data transfer between the client and server.

4. networkcv.py: Implements the Network class that actually manages the networking and data transfer between the client and server.


# How to use:

Step I: Run the server script on one terminal and keep it running.

Step II: Run the client script, it will show a waiting window.

Step III: Run another instance of the client script (on any machine in the local network), as soon as another user is available for call the server will establish a connection between the two.

