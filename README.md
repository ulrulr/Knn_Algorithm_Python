# Knn_Algorithm_Python

The main goal of this project is to make a knn algorithm as efficient as possible.For the first version, we have a dataset on irises, described by 4 numerical variables that correspond to coordinates and their iris type in the last column.  I separated the dataset into 2 files, a training file and a test file. In order to know if the predictions are good, I made a confusion matrix, this allows to know the efficiency of the algorithm and especially if the predictions are good.

Why have I made 2 versions of this algorithm ?

Because in a second step, we changed dataset. I didn't specify it above but in the first dataset there were only 3 types of Iris (so 3 forecast cases), the Setosa, Versicolor and Virginica iris. In the new dataset, we don't have any iris, it's simply a dataset with a lot of forecast cases named from A to F (see more), this forced me to generalize the knn algorithm by automating the management of the forecast types because I had manually put the iris types in the first version because there were only 4, so it's logical that I wasn't going to type 20 types manually...
Then the second version is better because the algorithm learns the forecast types by itself and we don't need to enter them manually anymore.
