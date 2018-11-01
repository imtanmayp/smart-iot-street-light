import subprocess
import time

process = subprocess.Popen(" fswebcam image.png ", shell=True, stdout=subprocess.PIPE)
process.wait()
#print process.returncodep

time.sleep(2)
process = subprocess.Popen(" fswebcam image1.png ", shell=True, stdout=subprocess.PIPE)
process.wait()
#print process.returncodep

time.sleep(2)
process = subprocess.Popen(" fswebcam image2.png ", shell=True, stdout=subprocess.PIPE)
process.wait()

time.sleep(2)
process = subprocess.Popen(" fswebcam image3.png ", shell=True, stdout=subprocess.PIPE)
process.wait()

time.sleep(2)
process = subprocess.Popen(" fswebcam image4.png ", shell=True, stdout=subprocess.PIPE)
process.wait()