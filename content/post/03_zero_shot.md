+++
title = "When there are no labels v2"
cover = "https://source.unsplash.com/nLXOatvTaLo"
description = "Use LLMs to generate labels for a classifier"
weight = 3
+++

Image by [Juan Rumimpunu](https://unsplash.com/photos/gray-monkey-in-bokeh-photography-nLXOatvTaLo)


## Train a classifier with SetFit and Argilla using zero-shot learning - and an LLM.
This tutorial focuses on zero-shot learning using a large language model (LLM) for text classification. The LLM is utilized through the Together API to prelabel the dataset, which is then validated using Argilla. The traditional machine learning approach, using TF-IDF vectorization and logistic regression, is presented for comparison. The tutorial demonstrates the effectiveness of the LLM zero-shot approach in classifying news articles into predefined categories with limited labeled data. The performance of the LLM approach is evaluated and compared to the traditional machine learning approach.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/rjuro/unistra-nlp2024/blob/main/notebooks/UNISTRA-03-ZeroShot-classifier-argilla-setfit-LLM.ipynb)

