# Introduction

------
For this dataset is used for Emotion recognition. 15 Chinese film clips (positive, neutral and negative emotions) were chosen from the pool of materials as stimuli used in the experiments. The selection criteria for film clips are as follows: (a) the length of the whole experiment should not be too long in case it will make subjects fatigue; (b) the videos should be understood without explanation; and (c) the videos should elicit a single desired target emotion. The duration of each film clip is about 4 minutes. Each film clip is well edited to create coherent emotion eliciting and maximize emotional meanings. The details of the film clips used in the experiments are listed below:

![cmd-markdown-logo](http://bcmi.sjtu.edu.cn/~seed/img/seed/stimuli_table.png)

There are totally 15 trials for each experiment. There is a 15s hint before each clips and 10s feedback after each clip. The order of presentation is arranged so that two film clips targeting the same emotion are not shown consecutively. For the feedback, participants are told to report their emotional reactions to each film clip by completing the questionnaire immediately after watching each clip. The detailed protocol is shown below:

![cmd-markdown-logo](http://bcmi.sjtu.edu.cn/~seed/img/seed/protocol.png)

The EEG cap according to the international 10-20 system for 62 channels is shown below:

![cmd-markdown-logo](http://bcmi.sjtu.edu.cn/~seed/img/seed-iv/montage.png)

EEG-based emotion recognition has been studied for a long time. A new effective EEG feature named differential entropy is proposed to represent the characteristics associated with emotional states. 

In the "data" folder, there are train and test dataset containing downsampled, preprocessed and segmented versions of the EEG differential entropy data. 

------

# Data Structure

The training set contains a total of 19960 data and testing set contains 13720 data. Each piece of data contains 310 values representing the data of 62 electrodes on 5 frequencies. 
