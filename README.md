# Smart iot street light for energy efficiency and safety
the street lights are LED to save energy
consist of camera and panic button for safety
sensors used - LDR, IR, camera
Images from Camera are sent to AWS S3 bucket


First we have to setup a AWS account. 

In AWS we get S3 buckets to store the data.

Create a new bucket and get access to your "ACCESS_KEY_ID", "ACCESS_SECRET_KEY", "BUCKET_NAME"

Enter the same details in "boto_v2.py". boto is the API used to send data from raspberry pi to AWS s3 bucket.

Also take care of proper path names in the codes. do remember that all the codes have to be in the same folder as "cam.py" and "boto_v2.py" are subroutines called from main program.

Once all the connections are made run the "smart_light_main.py" and the application should keep running.
