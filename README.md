# Running directions

Below command works for odyssey car(tweak crop_rate if necessary):

(yolov4-gpu) :~/AIGUY_CROP/yolov4-custom-functions$ xvfb-run python detect_video.py --weights ./checkpoints/yolov4-416 --size 416 --model yolov4 --video ./data/video/odyssey.mp4 --crop
