import cv2, sys, os

if len(sys.argv) != 1:
  print('Usage: python/python3 write_frames.py <directory with images>')
  exit()

directory = sys.argv[1]
if not os.path.exists(directory) or not os.path.isdir(directory):
  print(directory + ' is not a valid directory')
  exit()

video = input('Output video name: ')
fps = input('Output video frames per second: ')
try: 
  fps = int(fps)
except ValueError:
  print(fps + ' must be an integer')
  exit()

# Obtains image files in directory
files = [img for img in os.listdir(directory) if img.endswith('.png') or img.endswith('.jpg')]
# Sorts filenames in ascending order
files.sort(key=lambda f: int(re.sub('\D', '', f)))

frame = cv2.imread(os.path.join(directory, images[0]))
height, width, _ = frame.shape
size = (width, height)

def save_video(vid_name, framerate):
  vid = cv2.VideoWriter(vid_name, int(fourcc), framerate, size)

	for file in files:
		print('Adding frame ' + file)
		img = cv2.imread(os.path.join(directory, file))
		vid.write(img)
	print('All frames added')

	cv2.destroyAllWindows()
	vid.release()
  print('Video ' + vid_name + ' created successfully')

save_video(video + '.avi', fps)
# Feel free to use the save_video method to create different
# types of videos here (maybe with lower/higher fps)
