+++
title = "LLMs for topic modeling"
cover = "img/tm.png"
description = "Use LLMs to label topics with BerTopic and Mistral"
weight = 4
+++

**Enhancing Topic Modeling with Open Source Large Language Models (LLMs)**

This guide explores the use of open-source Large Language Models (LLMs) like Mistral, Zephyr, and others, including Llama 2 and Qwen for enhanced Chinese language support, to improve topic modeling efficiency. We will focus on avoiding the exhaustive approach of processing each document with an LLM and utilize BERTopic, a flexible topic modeling framework, to refine topic delineations.

BERTopic simplifies topic modeling into five clear steps: embedding documents, dimensionality reduction of embeddings, clustering of embeddings, document tokenization by cluster, and extraction of the most representative words for each topic. With advanced LLMs like Mistral or Gemma, our topic modeling capabilities have expanded beyond simple word lists.

We propose a novel approach: utilizing BERTopic to generate clusters and topics, then employing Mixtral to refine and enhance these into more precise topic representations. This method combines the strengths of both BERTopic's efficient topic generation and Mixtral's refined topic representation.

In this practical tutorial, we will be using together.ai and the remote LLM. We will start by installing a number of packages used throughout this example.

Summary:

* This guide explores the use of open-source LLMs to improve topic modeling efficiency.
* BERTopic, a flexible topic modeling framework, is utilized to refine topic delineations.
* A novel approach is proposed: utilizing BERTopic for topic generation and Mixtral for refined topic representation.
* The tutorial will employ together.ai and the remote LLM.
* The installation of required packages will be covered.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/rjuro/unistra-nlp2024/blob/main/notebooks/UNISTRA-04-TMOpenAITogether.ipynb)

