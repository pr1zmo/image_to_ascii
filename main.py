# import PIL as pl
from PIL import Image
import os

_ext = [".png", ".jpg", ".jpeg"]
ascii_arr = ['-', '*', '#', '@']
final_img = open("ascii", 'w+')

def check_file(path) -> bool:
	if (os.path.exists(path)):
		if (path[5:] in _ext):
			return True
	return False

def turn_to_ascii(img):
	any = img.convert('RGB')
	width, height = any.size
	it = (width / 10) * (height / 10)
	brightness = 0
	while (it > 0):
		for x in range(int(width / it)):
			for y in range(int(height / it)):
				r,g,b = any.getpixel((x, y))
				brightness += 0.2126 * r + 0.7152 * g + 0.0722 * b
		brightness /= ((width / it) * (height / it))
		index = int((brightness / 255) * 4)
		if (width / it == 1):
			final_img.write('\n')
		final_img.write(ascii_arr[index])
		it -= 1

if __name__ == "__main__":
	# print(dir(Image))
	path = input("Image path: ")
	if (check_file(path)):
		img = Image.open(path)
		turn_to_ascii(img)
		final_img.close()
	else:
		print("Something went wrong")