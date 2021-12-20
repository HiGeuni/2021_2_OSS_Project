# Image Crawler & file Selector

데이터셋 구축을 위한 구글 이미지 크롤링 & 파일 정리를 위한 file selector


# Information

데이터셋 구축을 목적으로 많은 이미지들을 크롤링을 했었는데 크롤링 결과에 연구에 도움이 되지 않는 이미지들이 많아서 binary classification을 적용해서 크롤링을 하도록 함.

## Requirements

- tensorflow >= 2.0.0
- numpy
- opencv-python
- selenium
- chrome-driver(크롬 버전에 맞게)
- Pillow

## Model
Binary Classifier with VGG16

trainModel.ipynb

## Arguments 

### crawler.py
```
python crawler.py 
 [--keyword KeyWord-list]
 [--comb keyword_combination_list]
 [--txt txt_file_path] 
 [--noPaint boolean]
 [--limitSize limit_size]
 [--type "jpg"]
 [--dst output_folder]
```
### fileSelector.py
```
python fileSelector.py 
 [--dir file_path]
 [--type "image or file"]
 [--to move_directory]
```

## How to use

### crawler.py 
1. keyword를 입력으로 주는 경우
```
python crawler.py --keyword summer winter --dst ./
```
2. keyword와 comb를 같이 입력으로 주는 경우
```
python crawler.py --keyword summer winter --comb garden building --dst ./
```
Keywords = ["summer garden", "summer buliding", "winter garden", "winter building"]

3. txt파일을 지정한 경우
```
python crawler.py --txt ./examples/keyword.txt --dst ./
```
in keyword.txt  
spring  
autumn  

4. noPaint option
```
python crawler.py --txt ./examples/keyword.txt --dst ./ --noPaint True
```
True : No Paint Image  
False : All Image  

5. limitSize option
```
python crawler.py --txt ./examples/keyword.txt --dst ./ --noPaint True --limitSize=800
```
max(이미지 너비, 이미지 높이) >= 800 인 이미지만 크롤링  

### fileSelector.py
1. 이미지를 정리할 때
```
python fileSelector.py --type="image" --to=./
```
2. 파일들을 정리할 때
```
python fileSelector.py --type="file" --to=./
```
⬇️ : next  
➡️ : delete file  
⬅️ : move file  
end : exit  
