import sys, os
from PIL import Image, ImageEnhance
# grab first and second argument
image_folder = sys.argv[1]
dest_folder = sys.argv[2]

# check if new folder exists if not create
if not os.path.exists(dest_folder):
	os.mkdir('new')

# loop trough pokedox and convert images to png
for filename in os.listdir(image_folder):
	if filename=='.DS_Store':
		continue
	img = Image.open(f'{image_folder}{filename}')
	enh = ImageEnhance.Contrast(img)
	x=enh.enhance(1.3)
	clean_name = os.path.splitext(filename)[0]
	img.save(f'{dest_folder}{clean_name}.png', 'png')
	x.save(f'{dest_folder}{clean_name}.enh.png', 'png')
	print('all done!')
	print("haminba hamin vaqt raft bal")
