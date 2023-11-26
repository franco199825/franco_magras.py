from PIL import Image

import os

downloadsfolder = "/users/franc/Downloads/"
picturesfolder = "/users/franc/Pictures/"

if __name__ == "__main__":
    for filename in os.listdir(downloadsfolder):
        name, extension = os.path.splitext(downloadsfolder + filename)

        if extension in [".lpg", ".jpeg", ".png"]:
            picture = Image.open(downloadsfolder + filename)
            picture.save(picturesfolder + "compressed_"+ filename, optimize=True , quality=60)
            os.remove(downloadsfolder + filename)
            print(name + ": " + extension) 

        if extension in [".mp3"]:
            musicfolder = "/users/franc/Music/"
            os.rename (downloadsfolder + filename, musicfolder + filename)

        if extension in [".mp4"]:
            videofolder = "/users/franc/Music/"
            os.rename (downloadsfolder + filename, videofolder + filename)
