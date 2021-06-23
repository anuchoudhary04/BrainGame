import os 

IMAGE_SIZE = 128
SCREEN_SIZE = 512
NUM_TILES_SIDE = 4
NUM_TILES_TOTAL = 16
MARGIN = 4

IMAGE_DIR = 'images'
IMAGE_FILES = [ x for x in os.listdir(IMAGE_DIR) if x[-3:].lower() == 'png']
assert len(IMAGE_FILES) == 8
