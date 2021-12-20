# Binary Classifier With VGG16

imagenet으로 pretrained된 VGG16을 이용해서 그림인지, 실제 사진인지를 판단하는 Binary Classifer를 학습시켰습니다.

## Data
데이터셋 구축을 위해 모은 많은 이미지들 중 그림 파일을 False로, 실제 사진을 True로 라벨링해서 데이터셋을 구축했습니다.  
True Data : 1377  
False Data : 1346  

## Model
### Xception Model
imagenet으로 pretrained된 Xception모델의 출력층을 제외하고 불러와 trainable = False, output layer를 만들어서 학습을 시켰는데 결과가 좋지 않았습니다.  
하이퍼파라미터를 바꿔보며 학습을 진행했지만, 적절한 하이퍼 파라미터를 찾지 못해서 Accuracy : 50%대로 유지가 되었습니다.  그래서 이전에 사용해 보았던 VGG16을 사용했습니다.
### VGG16 Model
위와 동일하게 imagenet으로 pretrained된 VGG16모델의 출력층을 제외하고 불러과 trainable=False로 설정하고, output layer를 만들어서 학습을 시켰습니다.  
학습 결과는 98% 정도로 좋은 성능을 보였습니다.

## Evaluation
1000개의 실제 이미지를 테스트 이미지로 만들어서 돌려본 결과 90%정도로 좋은 성능을 보였습니다.

## 앞으로 할 일
1. Xception 모델이 왜 잘 안되었는지 분석하고, 해결하고 싶습니다.
2. 데이터의 수가 적은 것 같아서 늘려서 더 좋은 성능의 모델을 적용하고 싶습니다.

## Reference
model from https://www.kaggle.com/raulcsimpetru/vgg16-binary-classification
Data Preprocessing from https://mj-lahong.tistory.com/82
