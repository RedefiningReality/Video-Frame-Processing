import cv2, sys, os, shutil

if len(sys.argv) != 2:
	print('Usage: python3 read_frames.py <video file>')

cap = cv2.VideoCapture(sys.argv[1])

fourcc = cap.get(cv2.CAP_PROP_FOURCC)
frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
fps = cap.get(cv2.CAP_PROP_FPS)
print('Encoding: ' + str(fourcc))
print('Number of frames: ' + str(frames))
print('Frames per second: ' + str(fps))

name = sys.argv[1][:-4]

save = input('Save video frames? [Y/N]')
save = save.lower() == 'y'
view = input("View frames as they're being processed? [Y/N]")
view = view.lower() == 'y'

if save:
	if os.path.exists(name):
		if os.path.isdir(name):
			shutil.rmtree(name)
		else:
			print(name + ' is a file. Please remove it and rerun this script')
			exit()
	try:
		os.mkdir(name)
	except OSError:
		print('Failed to make directory ' + name)
		exit()
	else:
		print('Created directory ' + name)

counter = 0
while(cap.isOpened()):
	ret, frame = cap.read()
	if ret == False:
		break
	
	if save:
		out = name + '/' + str(counter) + '.png'
		cv2.imwrite(out, frame)
	if view:
    		cv2.imshow('frame', frame)
    		if cv2.waitKey(1) & 0xFF == ord('q'):
      			break
	
	counter += 1

cap.release()
cv2.destroyAllWindows()
