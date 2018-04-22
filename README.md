# GroupNo4-Determine-depression-quotient-and-suicidal-behavior-using-machine-learning-techniques

The training dataset is expected to be a csv file of type tweet_id,sentiment,tweet where the tweet_id is a unique integer identifying the tweet, sentiment is either 1 (positive) or 0 (negative), and tweet is the tweet enclosed in "". Similarly, the test dataset is a csv file of type tweet_id,tweet. Please note that csv headers are not expected and should be removed from the training and test datasets.

Usage
Preprocessing
Run preprocess.py <raw-csv-path> on both train and test data. This will generate a preprocessed version of the dataset.
Run stats.py <preprocessed-csv-path> where <preprocessed-csv-path> is the path of csv generated from preprocess.py. This gives general statistical information about the dataset and will two pickle files which are the frequency distribution of unigrams and bigrams in the training dataset.
After the above steps, you should have four files in total: <preprocessed-train-csv>, <preprocessed-test-csv>, <freqdist>, and <freqdist-bi> which are preprocessed train dataset, preprocessed test dataset, frequency distribution of unigrams and frequency distribution of bigrams respectively.

For all the methods that follow, change the values of TRAIN_PROCESSED_FILE, TEST_PROCESSED_FILE, FREQ_DIST_FILE, and BI_FREQ_DIST_FILE to your own paths in the respective files. Wherever applicable, values of USE_BIGRAMS and FEAT_TYPE can be changed to obtain results using different types of features as described in report.

3.	Open anaconda command prompt, cd to the directory where the code is stored and type ‘jupyter notebook’ and enter
4.	Open cnn2\3\6 and lstm2\3\6 one by one and run
 This will run the 4-Conv-NN (4 conv layers neural network) model as described in the report. To run other versions of CNN, just comment or remove the lines where Conv layers are added. Will validate using 10% data and save models for each epoch in ./models/. (Please make sure this directory exists before running cnn.py).
5.	Make sure to change the files names and models folder according to the training type
6.	For cnn\lstm2 use models2, for cnn\lstm3 models3, fopr cnn\lstm6 models6
7.	For cnn\lstm2 training3, for cnn\lstm3 training1 and for cnn\lstm6 training2
8.	For test data set, format is id, tweet
9.	One pred file used thrice on same user changing the hdf5 file for the respective type everytime
10.	In pred use hdf5 files starting from cnn only, the latest and from the corresponding folder for the type for which prediction is being made
11.  Run scoring.py to calculate a score for individual tweets using their classes
12. Use the scores generated to form a auto regression model using auto_reg.py and get the final depression quotient using depression_quotient.py

