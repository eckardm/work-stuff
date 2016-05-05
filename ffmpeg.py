import os

path = os.path.join("Q:", "Homefolders", "eckardm", "Desktop", "Sample_Audio_and_Video")

for name in os.listdir(path):

    if "FFmpeged" not in name and name.replace(name[-4:], "_FFmpeged.mp4") not in os.listdir(path):

        os.system("ffmpeg -i " + os.path.join(path, name) + " " + os.path.join(path, name.replace(name[-4:], "_FFmpeged.mp4")))
