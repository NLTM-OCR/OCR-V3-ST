import os
import sys


def main(modality, lang):
	"""
	There is a bug in the V2 OCR where if we only give one word image as input,
	then the output of the ocr will only contain the first character of the word,
	instead of the complete word, while the OCR is working perfectly fine when
	the number of input word images > 1.
	The issue appears to be on ajoy side's in the testing code somewhere.
	for now, I added a dummy word image (hindi) called "-1.jpg" so that the OCR will
	always get >1 word images as input, and I remove the dummy image inference
	when creating the out.json file finally.
	"""
	# if os.path.isdir(output_location) == False:
	# 	os.makedirs(output_location)
	# # adding a dummy image, creating the lmdb, then removing the dummy image.
	command = [
		'./read.py',
		f'/model/parseq_model.ckpt',
		# f"--input_location /data",
		# "--device cpu",
		# f"--output_location /data",
		# f"--language_name {lang}"
	]
	os.system(' '.join(command))

if __name__ == '__main__':
	#1: language

	main(sys.argv[1], sys.argv[2])

