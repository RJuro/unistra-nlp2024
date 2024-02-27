+++
title = "When there are no labels"
cover = "https://source.unsplash.com/KKtEXWJaSv8"
description = "Classify text with few-shot learning and manual labeling"
weight = 2
+++

Image by [joel herzog](https://unsplash.com/photos/grayscale-photo-of-man-holding-shot-glass-filled-with-liquid-KKtEXWJaSv8)

## Few-shot learning with SetFit and Argilla

In this tutorial, we explore the case of having no labels and the need to "bootstrap" a training dataset using a few-shot approach called SetFit. Additionally, we cover the use of Argilla for data labeling and quality assurance.

## Key Steps in Each Approach

### SetFit Framework:

1. **Data Preparation**: The training data is read from a Parquet file and sampled for demonstration purposes. It is then converted into a Hugging Face `datasets` Dataset.

2. **Text Encoding**: A pre-trained sentence transformer model is used to encode the text data, resulting in embeddings for each text instance. These embeddings are employed for semantic search within Argilla to expedite labeling.

3. **Training with SetFit**: The encoded text data is loaded into a SetFit dataset for text classification. The model, loss function, and trainer are instantiated, and the training process is initiated. The model's performance is subsequently evaluated using the evaluation dataset.

### Traditional Machine Learning Approach:

To compare performance, a simple traditional classifier using TFIDF and logistic regression is implemented.

1. **Data Loading**: The AG News dataset is loaded using the `load_dataset` function from Hugging Face datasets.

2. **Data Preprocessing**: The text data is split into training and test sets, and TF-IDF vectorization is applied to convert the text into numerical features.

3. **Model Training and Evaluation**: A logistic regression model is trained on the TF-IDF transformed text data, and predictions are made on the test set. The performance of the model is evaluated using classification reports to assess its accuracy, precision, recall, and F1-score.


[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/rjuro/unistra-nlp2024/blob/main/notebooks/UNISTRA-02-FewShot-classifier-argilla-setfit.ipynb)

