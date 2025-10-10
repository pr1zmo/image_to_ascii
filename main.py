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

def write_in_ascii(r, g, b):
	brightness = 0.2126 * r + 0.7152 * g + 0.0722 * b
	index = int((brightness / 255) * 4)
	final_img.write(ascii_arr[index])




def turn_to_ascii(img):
	any = img.convert('RGB')
	width, height = any.size
	for x in range(width):
		for y in range(height):
			r,g,b = any.getpixel((x, y))
			write_in_ascii(r, g, b)

if __name__ == "__main__":
	# print(dir(Image))
	path = input("Image path: ")
	if (check_file(path)):
		img = Image.open(path)
		turn_to_ascii(img)
		final_img.close()
	else:
		print("Something went wrong")