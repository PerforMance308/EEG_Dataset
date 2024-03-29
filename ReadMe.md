### 1. Introduction

------
This dataset is used for Emotion recognition. 15 Chinese film clips (positive, neutral and negative emotions) were chosen from the pool of materials as stimuli used in the experiments. The selection criteria for film clips are as follows: (a) the length of the whole experiment should not be too long in case it will make subjects fatigue; (b) the videos should be understood without explanation; and (c) the videos should elicit a single desired target emotion. The duration of each film clip is about 4 minutes. Each film clip is well edited to create coherent emotion eliciting and maximize emotional meanings. 

There are totally 15 trials for each experiment. There is a 15s hint before each clips and 10s feedback after each clip. The order of presentation is arranged so that two film clips targeting the same emotion are not shown consecutively. For the feedback, participants are told to report their emotional reactions to each film clip by completing the questionnaire immediately after watching each clip. 

A new effective EEG feature named differential entropy is proposed to represent the characteristics associated with emotional states. 

In the "data" folder, there are train and test dataset containing downsampled, preprocessed and segmented versions of the EEG differential entropy data. 

------

### 2. Data Structure

The dataset containing extracted differential entropy (DE) features of the EEG signals. These data is well-suited to those who want to quickly test a classification method without propcessing the raw EEG data. The training set contains a total of 84420 data and testing set contains 58128 data. Each piece of data contains 310 values representing the data of 62 electrodes on 5 frequencies.

------

### 3. How to use

1. Download dataset from [here](https://drive.google.com/file/d/1Ql5jRm-JDHNm46sfX68ahEXCUrVw7VFR/view?usp=sharing).

2. Unzip the downloaded file and put the train test files in the folder under the project /data/

3. Download load_data.py and put it in the same directory with /data folder. The directory structure is as follows:
![image](https://github.com/PerforMance308/EEG_Dataset/blob/master/folder.png)

4. Add the following statement to your code to use.

```python
import load_data

# return DataSet class
data = load_data.read_data_sets(one_hot=True)

# get train data and labels by batch size
train_x, train_label = data.train.next_batch(BATCH_SIZE)

# get test data
test_x = data.test.data

# get test labels
test_labels = data.test.labels

# get sample number
n_samples = data.train.num_examples
```

------

### 4. More

For more information please go to:
- https://ieeexplore.ieee.org/document/6695876
- https://ieeexplore.ieee.org/abstract/document/7883875

------

### 5. Contact

Author: Shiqi Wang

Email: swang50@lakeheadu.ca
