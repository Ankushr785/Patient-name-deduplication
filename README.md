# Patient-name-deduplication
**A machine learning approach towards removing duplicate entries from patient data.**

>Input data - Patient name records

![image1](https://user-images.githubusercontent.com/26039458/36588217-668747a2-18ad-11e8-8748-8a8cd9c0e6c0.png)

The input dataset consists of a lot of duplicate entries. The goal of this assignment is to use a machine learning approach to remove those duplicate entries.

>Preprocessing

* The date of birth column was converted to standard datetime format.
* A list of unique dates of birth was obtained to loop over, followed by looping over a list of uniques genders.
* The input dataset was manually processed to classify entries as either duplicate (0) or occurring for the first time (1), in order to help the model learn through accuracy score.
* The dataset is randomly divided into a training and a test set, keeping the ratio of classes same in both the sets.

>Levenshtein distance/score

* It calculates the number of changes required to make in a string to convert it into another string.
* The only transformations allowed are deletion, substitution and insertion.

>Training

* A learning function was created for the purpose of classifying entries as either duplicate (1) or occurring for the first time (0).
* Parameters of the learning function - training data, levenshtein_scoring_range, no. of equivalent iterations before stopping.
* levenshtein_scoring_range is the number of values to iterate the model over.
* No. of equivalent iterations before stopping is the number of increments in the levenshtein score that the model makes despite no improvement in the accuracy.

>Model

* A loop is run over every unique date of birth in the data, followed by looping over unique genders. To identify duplicate entries, we'll run text matching over entries with same DOB and Gender.
* Once the entries with same DOB and Gender are indexed out, we'll match every entry with every entry coming after it in the same list to obtain a list of levenshtein scores for every entry. This way, for 2 or more same entries, the first entry will be considered as unique while the others will be treated as its duplicates.
* The minimum levenshtein score will determine if the entry is close to at least one of the other entries with the same DOB and Gender.
* Machine learning is done to identify the optimum minimum value of levenshtein score to classify an entry as a duplicate. The algorithm will iterate over a passed range of numbers (levenshtein_scoring_range).
