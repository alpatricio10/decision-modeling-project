## Elaboration of Nutri-score Models
#### Decision Modeling Project - CentraleSupélec BDMA M2

### Project Description
This repository contains the implementation of several Multi-Criteria Decision Analysis (MCDA) and Machine Learning models designed to elaborate a **Nutri-Score** nutrition labeling system. The project explores both compensatory and non-compensatory decision logic to classify food products based on their nutritional and environmental impact.

---

## Project Overview

The objective of this project is to model the Nutri-Score labeling system using different decision-making frameworks. We compare the official logic with:
1.  **ELECTRE-TRI (MR-Sort):** A non-compensatory outranking method.
2.  **Weighted Sum Model (WSM):** A compensatory additive utility model.
3.  **Machine Learning:** Data-driven classifiers trained to mimic existing labels.

A key difference in this project is the integration of the **Green-Score**, allowing for an evaluation of both health and environmental sustainability.

---

## Repository Structure

The project is divided into several notebooks, utility functions and directories:

* **`_0_data_analysis_.ipynb`** and **`_0_data_extraction_.ipynb`**: Data cleaning, handling missing values, and feature engineering for the Open Food Facts dataset.
* **`_1_nutri_score.ipynb`**: Implementation of the standard Nutri-score model.
* **`_2_electre_tri.ipynb`**: Implementation of the MR-Sort model, including profile selection (Centroids, Quantiles) and weight selection.
* **`_3_weighted_sum.ipynb`**: Implementation of the weighted sum model with weight and threshold computations and manual decision-maker schemes.
* **`_4_machine_learning.ipynb`**: Supervised learning pipeline featuring Random Forest, Gradient Boosting, SVM, and KNN with 5-fold cross-validation.
* **`_5_other_group_comparison.ipynb`**: Comparison of our model performance with an external dataset from another group.
* **model_utils.py**: utility functions for reading and verifying the datasets.
* **`data/`**: Directory containing the processed CSV datasets.
* **`images/`**: All generated plots, confusion matrices, and distribution graphs.
* **`submission/`**: All relevant documentation.
