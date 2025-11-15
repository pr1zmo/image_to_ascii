from PIL import Image, ImageOps
import cv2, os
import numpy as np

_ext = [".png", ".jpg", ".jpeg"]
ascii_arr = ['-', '*', '^', '#', '@', '=']
final_img = open("ascii", 'w+')
width, height = 1280, 1280
ascii_width, ascii_height = 10, 20

def check_file(path) -> bool:
	if (os.path.exists(path)):
		if (path[5:] in _ext):
			return True
	return False

def scale(pil_img) -> np.ndarray:
	pil_img = pil_img.convert('RGB')
	scaled = ImageOps.fit(pil_img, (width, height))
	return np.array(scaled)

def turn_to_ascii(img):
	res = np.zeros((height, width, 3), np.uint8)
	img = scale(img)
	fin_arr = []

	for by in range(0, height, ascii_height):
		for bx in range(0, width, ascii_width):
			bri_sum = 0
			pixels_in_block = 0

			for y in range(ascii_height):
				for x in range(ascii_width):
					iy = by + y
					ix = bx + x
					if iy >= height or ix >= width:
						continue

					pixel = img[iy, ix]
					brightness = int(
						0.299 * pixel[0]
						+ 0.587 * pixel[1]
						+ 0.114 * pixel[2]
					)
					bri_sum += brightness
					pixels_in_block += 1

			if pixels_in_block == 0:
				avg_brightness = 0
			else:
				avg_brightness = bri_sum // pixels_in_block

			idx = int(avg_brightness / 256 * len(ascii_arr))
			if idx == len(ascii_arr):
				idx -= 1
			ch = ascii_arr[idx]
			fin_arr.append(ch)

			block_value = avg_brightness
			for y in range(ascii_height):
				for x in range(ascii_width):
					iy = by + y
					ix = bx + x
					if iy >= height or ix >= width:
						continue
					res[iy, ix] = (block_value, block_value, block_value)

	with open("ascii_output.txt", "w") as f:
		chars_per_line = width // ascii_width
		for i, ch in enumerate(fin_arr):
			f.write(ch)
			if (i + 1) % chars_per_line == 0:
				f.write("\n")

	cv2.imwrite("res.png", res)

	with open("ascii_output.txt", "w") as f:
		f.write(''.join(fin_arr))
	cv2.imwrite("res.png", res)
	

if __name__ == "__main__":
	path = input("Image path: ")
	if (check_file(path)):
		img = Image.open(path)
		turn_to_ascii(img)
		final_img.close()
	else:
		print("Something went wrong")
