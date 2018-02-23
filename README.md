# Patient-name-deduplication
**A machine learning approach towards removing duplicate entries from patient data.**

>Input data - Patient name records

![image1](https://user-images.githubusercontent.com/26039458/36588217-668747a2-18ad-11e8-8748-8a8cd9c0e6c0.png)

The input dataset consists of a lot of duplicate entries. The goal of this assignment is to use a machine learning approach to remove those duplicate entries.

>Preprocessing

* The date of birth column was converted to standard datetime format.
* A list of unique dates of birth was obtained to loop over, followed by looping over a list of uniques genders.
* The input dataset was manually processed to classify entries as either duplicate (0) or occurring for the first time (1), in order to help the model learn through accuracy score.

>Levenshtein distance/score

* 
>Training model

* A learning function was created for the purpose of classifying entries as either duplicate (1) or occurring for the first time (0).
* Parameters of the learning function - training data, levenshtein_scoring_range, no. of equivalent iterations before stopping.
* No. of equivalent iterations before stopping is the number of increments in the levenshtein score that the model makes despite no improvement in the accuracy.

