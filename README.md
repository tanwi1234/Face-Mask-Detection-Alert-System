# Face-Mask-Detection-Alert-System
The COVID - 19 pandemic is devastating mankind irrespective of caste, creed, gender, and religion. Until a vaccine is discovered, we should do our bit to constrain the expanse of the coronavirus. Using a facemask can undoubtedly help in managing the spread of the virus. COVID - 19 face mask detector uses or owns Facemask net, deep learning techniques to successfully test whether a person is with wearing a face mask or not and alert them if they are not wearing mask at a time.

Face detection is a branch of image processing that uses machine learning to detect faces in images . Face Mask Detection System uses existing IP cameras and CCTV cameras combined with Computer Vision to detect people without masks and alert the person who are not wearing mask.

APPLICATIONS:

1.Our face mask detector didn't use any morphed masked images dataset.

2.The model is accurate, and since we used the MobileNetV2 architecture, it’s also computationally efficient and thus making it easier to deploy the model to embedded systems (Raspberry Pi, Google Coral, etc.).

3.This system can therefore be used in real-time applications which require face-mask detection for safety purposes due to the outbreak of Covid-19. This project can be integrated with embedded systems for application in airports, railway stations, offices, schools, and public places to ensure that public safety guidelines are followed.

TECH/FRAMEWORK USED:

1.OPENCV  
2.TENSORFLOW  
3.KERAS  
4.FACE DETECTOR  
5.MOBILE NET V2 

DATASET:
This dataset consists of 3835 images belonging to two classes:   
•	With mask : 1916 images          
•	Without mask : 1919 images  

The images used were real images of faces wearing masks. The images were collected from the following sources:

•	Bing Search API 
•	Kaggle datasets 
•	RMFD dataset 
 
Our Goal is to train a custom deep learning model to detect whether a person is or is not wearing a mask.

METHODOLOGY TO BE FOLLOWED:

1.Training: Here,focus on loading our face mask detection dataset from disk, training a model   
(using Keras / TensorFlow) on this dataset, and then serializing the face mask detector to disk.

OUTPUT: Model give 92% accuracy for Face Mask Detection  after Training.

2.Deployment:Once the face mask detector is trained, we can then move on to loading the mask detector, performing face detection, and then classifying each face as with mask or without mask. 

3.Alert system:After denying access to the person, authorities will get an alert email in real- time where the person’s photo will be attached. May be screen panels could be installed at the entrances where a person when denied can see a pop-up Warning Message where he/she would be advised to wear a mask before getting access 

CONCLUSION:   
Addressing the wide spread use of face masks as a preventive measure to the COVID-19 pandemic spread, we presented an exploratory study on the effect of wearing masks on face recognition performance in collaborative scenarios. We presented a specifically collected database captured in two different sessions, with and without wearing a mask, and is part of an ongoing effort to gather a larger scale database with realistic variations.   

REFERENCES:
https://www.mygreatlearning.com/blog/real-time-face-detection/
  



