#!/usr/bin/env python3
# Scene Text Recognition Model Hub
# Copyright 2022 Darwin Bautista
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import argparse
import json
import os
from tqdm import tqdm

import torch
from PIL import Image

from strhub.data.module import SceneTextDataModule
from strhub.models.utils import load_from_checkpoint, parse_model_args


@torch.inference_mode()
def infer_and_save():
	parser = argparse.ArgumentParser()
	parser.add_argument('checkpoint', help="Model checkpoint (or 'pretrained=<model_id>')")
	parser.add_argument('--input_location', default='/data', help='Input image directory')
	parser.add_argument('--device', default='cuda')
	parser.add_argument('--output_location', default='/data')
	parser.add_argument('--language_name', default='Indic')

	args, unknown = parser.parse_known_args()
	print(args)
	print(unknown)
	kwargs = parse_model_args(unknown)
	print(f'Additional keyword arguments: {kwargs}')

	model = load_from_checkpoint(args.checkpoint, **kwargs).eval().to(args.device)
	img_transform = SceneTextDataModule.get_transform(model.hparams.img_size)
	prediction_record = {}

	images = os.listdir(args.input_location)
	images = [os.path.join(args.input_location, i) for i in images]
	for i in tqdm(images):
		# Load image and prepare for input
		image = Image.open(i).convert('RGB')
		image = img_transform(image).unsqueeze(0).to(args.device)

		p = model(image).softmax(-1)
		pred, p = model.tokenizer.decode(p)
		fname = os.path.basename(i)
		# print(f'{fname}: {pred[0]}')
		prediction_record[fname] = pred[0].strip()

	with open(os.path.join(args.output_location, "out.json"), 'w', encoding='utf-8') as file_obj:
		file_obj.write(json.dumps(prediction_record, indent=4))

if __name__ == '__main__':
	infer_and_save()
