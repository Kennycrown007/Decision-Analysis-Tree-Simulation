# 🌳 Decision Analysis Tree Simulation

This project models a decision-making scenario involving a land purchase that may yield oil. The simulation incorporates an expert’s predictive accuracy and calculates the expected monetary value (EMV) across varying accuracy rates.

---


## 🧠 Problem Summary

- Buy land for $180,000 with a chance of discovering oil.
- If oil is found: earn $1.8 million.
- An expert can be hired to predict oil presence with varying accuracy.

---

## 🔍 Objective

1. Construct a decision tree representing possible outcomes.
2. Perform sensitivity analysis on expert prediction accuracy.
3. Visualize EMV as a function of expert reliability.

---

## 📈 Sensitivity Analysis

- Vary `P(Predict Oil | Oil)` and `P(Predict No Oil | No Oil)` from 0.5 to 0.8.
- Calculate updated posterior probabilities using Bayes’ Theorem.
- Compute and compare EMVs with and without hiring the expert.

---

## 🖼️ Output

- Decision tree diagram (Graphviz)
  ![decision_tree](https://github.com/user-attachments/assets/b18e560e-1bb2-4822-8441-e18c833caf59)

---

- EMV dot plot showing impact of expert accuracy
  
  ![EMV Plot](https://github.com/user-attachments/assets/01a798a9-d3e0-4ff9-967a-960343688bb7)
  
---

- Observations on when hiring the expert is financially beneficial

---

## 🧰 Requirements

- Python 3.8+
- Jupyter Notebook
- Required Libraries:
  - NumPy
  - Pandas
  - Matplotlib
  - Graphviz

## 🚀 Usage

1. Clone the repository
2. Install the required packages (e.g., via `pip install -r requirements.txt`)
3. Open the `.ipynb` notebook in Jupyter and run the cells in order

## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://www.datascienceportfol.io/KehindeAromona)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/kehinde-gabriel-aromona-808578119/)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/kennycrown7)


## Badges
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange.svg)](https://jupyter.org/)

