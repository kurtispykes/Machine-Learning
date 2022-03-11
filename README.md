# Machine Learning 

A collection of blog articles and code related to machine learning that I've curated. 

I regularly write about Python, Machine Learning, Freelancing, Productivity, and Self-Branding in my 
[Medium Blog](https://kurtispykes.medium.com). With a $5 a month commitment, you can unlock an 
unlimited access to stories on Medium. If you use my 
[sign-up](https://kurtispykes.medium.com/membership) link, I'll recieve a small commision. 
If you're already a member, [subscribe](https://kurtispykes.medium.com/subscribe) to recieve 
my posts directly to your inbox whenever I publish. 


## Downloading the code

The simplest way to download the code is to clone the repository with `git clone`: 
```
git clone https://github.com/kurtispykes/Machine-Learning.git
```
### The steps
1. `git clone <repo>`
2. `cd <repo>`
3. `pip install virtualenv` (if you don't already have virtualenv installed)
4. `virtualenv venv` to create your new environment (called 'venv' here)
5. `venv/bin/activate.bat` to enter the virtual environment
6. `pip install -r requirements.txt` to install the requirements in the current environment

## Table of Contents 
### General ML Concepts
* [The Difference Between Classification and Regression](https://towardsdatascience.com/the-difference-between-classification-and-regression-in-machine-learning-4ccdb5b18fd3)
* [Semi-Supervised Machine Learning Explained](https://towardsdatascience.com/semi-supervised-machine-learning-explained-c1a6e1e934c7)
* [Unsupervised Machine Learning Explained](https://towardsdatascience.com/unsupervised-machine-learning-explained-1ccc5f20ca29)
* [Model Drift in Machine Learning](https://towardsdatascience.com/a-simple-explanation-of-mlops-e47009e245f7)
* [Building Reproducible Machine Learning Pipelines](https://medium.datadriveninvestor.com/machine-learning-model-deployment-b1eaf7ca96cd)
* [The Machine Learning Workflow](https://towardsdatascience.com/the-machine-learning-workflow-1d168cf93dea)

### Machine Learning Algorithms From Scratch
* [Linear Regression](https://towardsdatascience.com/algorithms-from-scratch-linear-regression-c654353d1e7c): [See Full Code](machine_learning_algorithms/linear_regression.ipynb)
* [Logistic Regression](https://towardsdatascience.com/algorithms-from-scratch-logistic-regression-7bacdfd9738e): [See Full Code](machine_learning_algorithms/logistic_regression.ipynb)
* [Naive Bayes](https://towardsdatascience.com/algorithms-from-scratch-naive-bayes-classifier-8006cc691493): [See Full Code](machine_learning_algorithms/naive_bayes.ipynb)
* [K-Nearest Neighbors](https://towardsdatascience.com/algorithms-from-scratch-k-nearest-neighbors-fe19b431a57): [See Full Code](machine_learning_algorithms/k-nearest_neighbors.ipynb)
* [Decision Tree](https://towardsdatascience.com/algorithms-from-scratch-decision-tree-1898d37b02e0): [See Full Code](machine_learning_algorithms/decision_tree.ipynb)
* [Support Vector Machine](https://towardsdatascience.com/algorithms-from-scratch-support-vector-machine-6f5eb72fce10): [See Full Code](machine_learning_algorithms/support_vector_machine.ipynb)
* [PCA](https://towardsdatascience.com/algorithms-from-scratch-pca-cde10b835ebc)

### Feature Engineering
* [Feature Engineering for Numerical Data](https://towardsdatascience.com/feature-engineering-for-numerical-data-e20167ec18): [See Full Code](feature_engineering/feature_engineering_numerical_data.ipynb)
* [Oversampling and Undersampling](https://towardsdatascience.com/oversampling-and-undersampling-5e2bbaf56dcf): [See Full Code](feature_engineering/oversampling_and_undersampling.ipynb)
* [Pandas: Combining data](https://towardsdatascience.com/pandas-combining-data-b190d793b626): [See Full Code](feature_engineering/combing_data_in_pandas.ipynb)
* [A Peek into Missing Data With Pandas](https://towardsdatascience.com/a-peek-into-missing-data-with-pandas-2fb9e5df8bd0): [See Full Code](feature_engineering/peek_into_missing_data.ipynb)
* [Handling Missing Data](https://towardsdatascience.com/handling-missing-data-f998715fb73f): [See Full Code](feature_engineering/handling_missing_data.ipynb)
* [Hyperparameter Optimization with Comet](https://heartbeat.comet.ml/hyperparameter-optimization-with-comet-80c6d4b83502): [See Full Code](feature_engineering/hyperparameter_opt_with_comet.ipynb)

### Feature Selection
* [Getting Started with Feature Selection](https://towardsdatascience.com/getting-started-with-feature-selection-3ecfb4957fd4): [See Full Code](feature_selection/feature_selection_beginner.ipynb)

### Data Visualization
* [Effective Data Visualization](https://towardsdatascience.com/effective-data-visualization-ef30ae560961): [See Full Code](data_visualization/data_visualization.ipynb)

### MLOps
* [A Simple Explaination of MLOps](https://towardsdatascience.com/a-simple-explanation-of-mlops-e47009e245f7)
* [Machine Learning in The Cloud](https://medium.datadriveninvestor.com/machine-learning-in-the-cloud-66bd25bc1a2b)
* [Machine Learning Model Deployment](https://medium.datadriveninvestor.com/machine-learning-model-deployment-b1eaf7ca96cd)
* [Introducing CI/CD Pipelines To Your Machine Learning Project](https://medium.com/pykes-technical-notes/introducing-ci-cd-pipelines-to-your-machine-learning-project-aa610dbeea2f?source=rss------programming-5)
* [7 Benefits of CI/CD Pipelines](https://medium.com/pykes-technical-notes/7-benefits-of-ci-cd-pipelines-22f807e81266)

### Evaluation Metrics
* [Cohen's Kappa](https://towardsdatascience.com/cohens-kappa-9786ceceab58)
* [Comprehension of the AUC-ROC Curve](https://towardsdatascience.com/comprehension-of-the-auc-roc-curve-e876191280f9)
* [Confusion Matrix "Un-confused"](https://towardsdatascience.com/confusion-matrix-un-confused-1ba98dee0d7f)

### Testing
* [Testing Machine Learning Systems: Unit Tests](https://medium.com/pykes-technical-notes/testing-machine-learning-systems-unit-tests-38696264ee04): [See Full Code](testing/)