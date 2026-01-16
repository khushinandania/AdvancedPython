from concurrent.futures import ThreadPoolExecutor
import requests
import time
import os

images = ["https://img.freepik.com/free-photo/courage-man-jump-through-gap-hill-business-concept-idea_1323-262.jpg",
          "https://www.shutterstock.com/image-photo/sun-sets-behind-mountain-ranges-600nw-2479236003.jpg",
          "https://media.istockphoto.com/id/517188688/photo/mountain-landscape.jpg?s=612x612&w=0&k=20&c=A63koPKaCyIwQWOTFBRWXj_PwCrR4cEoOw2S9Q7yVl8="]

# Create a directory to save downloaded images
save_dir = "/home/khushi/Desktop/khushi_module/AdvancedPython"
os.makedirs(save_dir, exist_ok=True)


def download_image(image_url,idx):

        response = requests.get(image_url, timeout=10)
        response.raise_for_status()

        image_name = f"image{idx+1}.jpg"
        file_path = os.path.join(save_dir, image_name)  # Full path to save the image

        with open(file_path, "wb") as f:
            f.write(response.content)

        print(f"{image_name} downloaded")

    

    
t1 = time.perf_counter()

with ThreadPoolExecutor(max_workers=3) as executor:
    for idx, image in enumerate(images):
         executor.submit(download_image, image,idx)

t2 = time.perf_counter()
print(f"Time taken to download images: {t2-t1} seconds")
