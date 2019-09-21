'''
Description:
Python program that uses multi-processing to apply a Gaussian Blur to multiple
high definition images. Using Multi-Processing significantly speeds up this process
'''
import time
import concurrent.futures
from PIL import Image, ImageFilter

# Input image file names
img_names = [
    'Input_Images/photo-1516117172878-fd2c41f4a759.jpg',
    'Input_Images/photo-1532009324734-20a7a5813719.jpg',
    'Input_Images/photo-1524429656589-6633a470097c.jpg',
    'Input_Images/photo-1530224264768-7ff8c1789d79.jpg',
    'Input_Images/photo-1564135624576-c5c88640f235.jpg',
    'Input_Images/photo-1541698444083-023c97d3f4b6.jpg',
    'Input_Images/photo-1522364723953-452d3431c267.jpg',
    'Input_Images/photo-1513938709626-033611b8cc03.jpg',
    'Input_Images/photo-1507143550189-fed454f93097.jpg',
    'Input_Images/photo-1493976040374-85c8e12f0c0e.jpg',
    'Input_Images/photo-1504198453319-5ce911bafcde.jpg',
    'Input_Images/photo-1530122037265-a5f1f91d3b99.jpg',
    'Input_Images/photo-1516972810927-80185027ca84.jpg',
    'Input_Images/photo-1550439062-609e1531270e.jpg',
    'Input_Images/photo-1549692520-acc6669e2f0c.jpg'
]

t1 = time.perf_counter()

size = (1200, 1200)


# Function that applies a Gaussian Blur ti each of the images above
def process_image(img_name):
    img = Image.open(img_name)

    img = img.filter(ImageFilter.GaussianBlur(15))

    img.thumbnail(size)
    saved_name = img_name.replace('Input_Images/', '')
    img.save(f'Processed_Images/{saved_name}')
    print(f'{img_name} was processed...')


# Applying multi-processing
with concurrent.futures.ProcessPoolExecutor() as executor:
    executor.map(process_image, img_names)


t2 = time.perf_counter()

print(f'Finished in {t2-t1} seconds')
