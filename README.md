# Python Multi-Processing Code to apply Gaussian Blur to High Def Images

<p>
<b>process-images.py</b> uses Python's ProcessPoolExecutor to use multi-processing to apply a Gaussian blur from the <b>Pillow</b> library to multiple high definition images.
<br />
The original images are stored in the <b>Input_Images</b> folder. The code takes each image, applies the Gaussian blur  and splits the work between multi-processors and finally stores the processed images in the <b>Processed_Images</b> folder
<br />
<br />
To run the code:
<br />
<b>python process_images.py
<br />
