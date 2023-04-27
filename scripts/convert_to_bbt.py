import os
import sys

FOLDER = f"{sys.argv[1]}/last_frame"
HP_FOLDER = '../processed/hp/last_frame'
frames = sorted(os.listdir(HP_FOLDER))

for frame in frames:
    idx = frame.split('_')[1]
    frameNum = int(frame.split('_')[-1].split('.')[0])


    #print(f"cp {FOLDER}/shot_{idx}_fn_{frameNum:06d}.jpg ~/mmt/VideoShotThreadSceneDetect/data/bbt_s01e01_excerpt/bbt_s01e01_{frameNum:06d}.jpg")
    #break
    os.system(f"cp {FOLDER}/shot_{idx}_fn_{frameNum:06d}.jpg /home/aneesh/UbuntuStorage/Homework/MMT/SonusTexere/src/VideoSceneDetection/data/bbt_s01e01_excerpt/bbt_s01e01_{frameNum:06d}.jpg")
