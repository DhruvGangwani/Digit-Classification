# Digit-Classification
Dataset:

txt file containing binary representation of digits (32 rows * 32 columns)

sample of original data is provided in raw_data directory

classes : Nine (0 to 9 digits)

training size : 1934

test size : 946


Collect_data.py : Converts txt file data into a single csv file for training and testing respectively.

classifier.ipynb : Implements KNN classifier with cross-validation. Multiple values of k were tried ranging from 1 to 11. Best model on gtraining dataset was used to predict test dataset
