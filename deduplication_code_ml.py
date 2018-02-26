
# coding: utf-8

# In[1]:

import pandas as pd
import numpy as np
import os
os.chdir('/home/ankushraut/Downloads/assignment')
from sklearn.metrics import f1_score, accuracy_score


# In[2]:

data = pd.read_csv('sample_input.csv')


# In[3]:

data.head()


# #### The dob is converted to standard datetime format.

# In[4]:

data.dob = pd.to_datetime(data.dob)


# In[5]:

data.head()


# In[6]:

data.dob.head(10)


# In[7]:

data['name'] = data.fn + ' ' + data.ln


# In[8]:

data.head()


# #### A list of unique dates of birth and unique genders is obtained.

# In[9]:

unique_dob = data.dob.unique()
unique_sex = data.gn.unique()


# In[10]:

import distance


# #### Deduplication model function. This function learns by evaluating the Macro F1-score of classification on a passed range of values for maximum levenshtein score to classify an entry as duplicate.

# In[11]:

def deduplication_model(data, scoring_range = 10, step = 2):
    data['indices'] = list(range(len(data)))
    accuracy = []
    index = []
    final_step = 0
    for value in range(scoring_range):
        for i in unique_dob:
            for j in unique_sex:
                sample = data[(data.dob == i)][(data.gn == j)].reset_index(drop = True)
                for a in range(len(sample)):
                    comparison = sample[(sample.indices != sample.indices[a])].reset_index(drop = True)
                    scores = [distance.levenshtein(sample.name[a], comparison.name[x]) for x in range(len(comparison))]
                    compare = [comparison.indices[x] for x in range(len(comparison))]
                    try:
                        if sample.indices[a]>compare[scores.index(min(scores))]:
                            score = np.min(scores)
                            if score<=value:
                                index.append(sample.indices[a])
                    except ValueError:
                        pass
        prediction = []
        for k in range(len(data)):
            if data.indices[k] in index:
                prediction.append(1)
            else:
                prediction.append(0)

        data['prediction'] = prediction
        print('F1-score after ',value, 'iterations : ', f1_score(data.is_duplicate, data.prediction, average = 'macro'))
        accuracy.append(f1_score(data.is_duplicate, data.prediction, average = 'macro'))
        if len(accuracy)>1 and accuracy[-1] <= accuracy[-2]:
            final_step+=1
        if final_step>=step:    
            value = value-final_step
            break
    
    index = []
    for i in unique_dob:
        for j in unique_sex:
            sample = data[(data.dob == i)][(data.gn == j)].reset_index(drop = True)
            for a in range(len(sample)):
                comparison = sample[(sample.indices != sample.indices[a])].reset_index(drop = True)
                scores = [distance.levenshtein(sample.name[a], comparison.name[x]) for x in range(len(comparison))]
                compare = [comparison.indices[x] for x in range(len(comparison))]
                try:
                    if sample.indices[a]>compare[scores.index(min(scores))]:
                        score = np.min(scores)
                        if score<=value:
                            index.append(sample.indices[a])
                except ValueError:
                    pass
    prediction = []
    for k in range(len(data)):
        if data.indices[k] in index:
            prediction.append(1)
        else:
            prediction.append(0)
    return prediction, value


# In[12]:

from sklearn.model_selection import train_test_split
train, test = train_test_split(data, test_size = 0.05, stratify = data.is_duplicate, random_state = 0)
train = train.reset_index(drop = True)
test = test.reset_index(drop = True)
performance, levenshtein_value_optimum = deduplication_model(train, scoring_range = 10, step = 3)


# In[13]:

def deduplication_prediction(data, optimum_value):
    data['indices'] = list(range(len(data)))
    index = []
    for i in unique_dob:
        for j in unique_sex:
            sample = data[(data.dob == i)][(data.gn == j)].reset_index(drop = True)
            for a in range(len(sample)):
                comparison = sample[(sample.indices != sample.indices[a])].reset_index(drop = True)
                scores = [distance.levenshtein(sample.name[a], comparison.name[x]) for x in range(len(comparison))]
                compare = [comparison.indices[x] for x in range(len(comparison))]
                try:
                    if sample.indices[a]>compare[scores.index(min(scores))]:
                        score = np.min(scores)
                        if score<=optimum_value:
                            index.append(sample.indices[a])
                except ValueError:
                    pass
    prediction = []
    for k in range(len(data)):
        if data.indices[k] in index:
            prediction.append(1)
        else:
            prediction.append(0)
    return prediction


# In[14]:

predictions = deduplication_prediction(test, levenshtein_value_optimum)


# In[15]:

print('F1-score on test set:',accuracy_score(test.is_duplicate, predictions))


# In[16]:

train['prediction'] = performance
test['prediction'] = predictions
dataset = pd.concat([train, test], axis = 0)
dataset = dataset[(dataset.prediction != 1)].reset_index(drop = True).drop(labels = ['name', 'is_duplicate', 'prediction', 'indices'], axis = 1)


# In[17]:

dataset.to_csv('Deduplicated_dataset.csv', index = False)

