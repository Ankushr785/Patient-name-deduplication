# Patient-name-deduplication
**A machine learning approach towards removing duplicate entries from patient data.**

>Input data - Patient name records

![image1](https://user-images.githubusercontent.com/26039458/36588217-668747a2-18ad-11e8-8748-8a8cd9c0e6c0.png)

The input dataset consists of a lot of duplicate entries. The goal of this assignment is to use a machine learning approach to remove those duplicate entries.

>Preprocessing

* The date of birth column is converted to standard datetime format.
* Lists of unique dates of birth as well as unique genders are obtained.
* The input dataset is manually processed to classify entries as either duplicate (0) or occurring for the first time (1), in order to help the model learn through evaluation. Hence, a labelled (binary) column is created.
* The dataset is randomly divided into a training and a test set, keeping the ratio of classes/labels same in both the sets.

>Levenshtein distance/score

* It calculates the number of changes required to convert a string into another.
* The only transformations allowed are deletion, substitution and insertion.

>Training

* A learning function is created for the purpose of classifying entries as either duplicate (1) or occurring for the first time (0).
* Parameters of the learning function - training data, levenshtein_scoring_range, no. of equivalent iterations before stopping.
* levenshtein_scoring_range is the number of values to iterate the model over.
* No. of equivalent iterations before stopping is the maximum number of increments in the minimum levenshtein score that the model makes despite no improvement in the accuracy.

>Model

* A loop is run over every unique date of birth in the data, followed by looping over every unique gender. To identify duplicate entries, we'll run text matching over entries with same DOB and Gender.
* Once the entries with the same DOB and Gender are indexed out as a dataframe, we'll match every entry in that dataframe with every other entry in the same dataframe to obtain a list of levenshtein scores for each entry. For 2 or more same entries, the first entry will be considered as unique (using a conditional statement over index) while the others will be treated as its duplicates.
* The minimum levenshtein score will determine if the entry is close to at least one of the other entries with the same DOB and Gender. This minimum value will be selected as the final levenshtein score for that entry.
* Machine learning is done to identify the optimum maximum value of levenshtein score to classify an entry as a duplicate. The algorithm will iterate over a passed range of numbers (levenshtein_scoring_range).
* Since we not only want the duplicate entries to be removed, we also want the first time entries to remain, hence the appropriate evaluation metric for this problem would be Macro F1-score.
* Macro F1-score calculates F1-score for each label/class, and finds their unweighted mean.

>Result

* Macro F1-score on training set -> 0.69
* Macro F1-score on test set -> 0.5

**The model successfully removed majority of the duplicates, since it puts a heavy penalty on mis-identification of both duplicates and originals.**
