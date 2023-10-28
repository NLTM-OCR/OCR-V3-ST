# Testing and Evaluation

## Dataset preparation
- This README assumes that you have all the word level test images in the path `bengali/images`
- Create `bengali/test_images.txt` file containing path of test word images. Each row of the file contains path of each word image in test set. for e.g.
  ```
  images/0001.jpg
  images/0002.jpg
  images/0003.jpg
  ...
  ```
- Create `bengali/test_labels.txt` file containing ground truth trascription of test word images. Each row of the file contains transcription of each word image in test set. for e.g.
  ```
  শুভেচ্ছা
  আচ্ছা
  বাংলা
  ...
  ```

## Create LMDB Test files 

`python3 create_lmdb_dataset --type test`

- It creates "test_lmdb" file under "bengali" folder 
