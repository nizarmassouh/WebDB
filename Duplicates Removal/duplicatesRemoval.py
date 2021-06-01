import imagehash
import os
import glob
import time
import sys

from PIL import Image

timestr = time.strftime("%Y%m%d-%H%M%S")
text_file = open("duplicateslog-%s.txt" % timestr, "w")


def find_similar_images(userpath):
    g = str(userpath)
    for dirr in sorted(glob.iglob(g)):
        stats = {}
        if os.path.isdir(dirr):
            count = 0
            s = 0
            images = {}
            text_file.write("%s :" % dirr)
            print("%s :" % dirr)
            dirs = str(dirr + "/*")  # iterate between concepts
            for img in glob.iglob(dirs):  # for each image get its perceptual hash
                try:
                    image_hash = imagehash.phash(Image.open(img))
                except Exception:
                    continue
                if image_hash in images:
                    oldsize = os.path.getsize(images[image_hash])
                    newsize = os.path.getsize(img)
                    oldrank = images[image_hash].split(dirr + '/')[1].split('.')[0]
                    newrank = img.split(dirr + '/')[1].split('.')[0]
                    key = str("(%s,%s)" % (oldrank, newrank))

                    if key in stats:
                        stats[key] += 1
                    else:
                        stats[key] = 1
                        if oldsize < newsize:
                            os.remove(images[image_hash])
                            images[image_hash] = img
                        else:
                            os.remove(img)
                        count += 1
                else:
                    images[image_hash] = img
            print(stats)
            text_file.write(str(stats) + str("\n"))
            text_file.close()


print("searching for duplicates")
find_similar_images(sys.argv[1])
