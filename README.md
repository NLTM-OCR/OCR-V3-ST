# SceneText Word Recognition for Indic Languages

## Pretrained Models:
- You can find the pretrained models for V3 scenetext for 13 languages under the [Assets](https://github.com/NLTM-OCR/OCR-V3-ST/releases/tag/v3).

## Setup
- Using Python = 3.10+
- Install Parseq Dependencies `pip install -r parseq_requirements.txt`
- Install Dependencies `pip install -r requirements.txt`

## Evaluation and testing:

```bash
python3 read.py --checkpoint bengali/parseq_model.ckpt --input_location test_data --output_location out
```
`--checkpoint` is trained model path containing model checkpoint
`--input_location` is the path to folder containing the inference images

- Please see read.py file, if you want to change these parameters 
- Path "out/output.json" contains the OCR text of each image found in `input_location`

## Contact

You can contact **[Ajoy Mondal](mailto:ajoy.mondal@iiit.ac.in)** for any issues or feedbacks.

## Citation

```
@InProceedings{IndicSTR,
  author="Lunia, Harsh and Mondal, Ajoy and Jawahar, C. V.",
  editor="Coustaty, Mickael and Forn{\'e}s, Alicia",
  title="IndicSTR12: A Dataset for Indic Scene Text Recognition",
  booktitle="Document Analysis and Recognition -- ICDAR 2023 Workshops",
  year="2023",
  pages="233--250"
}
```
