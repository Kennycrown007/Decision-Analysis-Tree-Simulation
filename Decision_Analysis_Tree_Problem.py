#!/usr/bin/env python
# coding: utf-8

# # Decision Analysis Tree Problem
# 
# --------
# 
# ## Problem Overview
# - Purchase land for \$180,000 which may contain oil.
# - If drill and oil is present, the return is \$1.8M.
# - An expert can be hired to predict whether oil is present.
# 
# ## Options
# - Do nothing (40% of the time) → EMV = 0
# - Buy land (60% of the time)
#   - Hire expert (50%)
#   - Don’t hire expert (50%)
# 
# ## Expert Behavior
# - P(Predict Oil | Oil): varies from 0.5 to 0.8
# - P(Predict No Oil | No Oil): varies from 0.5 to 0.8
# 
# ## Objective
# 1. Create a decision tree showing the choices and payoffs.
# 2. Perform a sensitivity analysis on expert accuracy.
# 3. Plot expected monetary value (EMV) as a dot plot.
# 

# ## Import Libraries

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import graphviz


# ## Decision Tree

# In[2]:


# Decision Tree using Graphviz
dot = graphviz.Digraph(format='png')
dot.attr(rankdir='LR')

# Initial choice
dot.node('Start', 'Start')
dot.node('DoNothing', 'Do Nothing\nEMV = $0')
dot.node('Buy', 'Buy Land\nCost = $180k')

dot.edge('Start', 'DoNothing', label='40%')
dot.edge('Start', 'Buy', label='60%')

# After buying
dot.node('NoExpert', 'Don\'t Hire Expert\nP(oil)=0.7')
dot.node('Expert', 'Hire Expert')

dot.edge('Buy', 'NoExpert', label='50%')
dot.edge('Buy', 'Expert', label='50%')

# Predictions if expert is hired
dot.node('Predict_Oil', 'Predict: Oil')
dot.node('Predict_NoOil', 'Predict: No Oil')

dot.edge('Expert', 'Predict_Oil', label='P1')
dot.edge('Expert', 'Predict_NoOil', label='P2')

# Outcomes from predictions
dot.node('Drill_Oil', 'Drill (P_oil > threshold)\nPayoff = $1.8M or -$180k')
dot.node('NoDrill', 'Don’t Drill\nLoss = $180k')

dot.edge('Predict_Oil', 'Drill_Oil')
dot.edge('Predict_NoOil', 'Drill_Oil')  # Based on posterior

# No expert drilling decision
dot.edge('NoExpert', 'Drill_Oil')

# Render tree
# dot.render('decision_tree', view=True)

dot


# ## Extract Parameters

# In[3]:


P_O = 0.7                     # Prior: Probability of oil
P_NO = 1 - P_O                # Prior: No oil
profit_if_oil = 1_800_000     # Revenue if oil is found
cost_of_land = 180_000        # Land purchase cost
net_profit_if_oil = profit_if_oil - cost_of_land


# ## Sensitivity ranges

# In[4]:


p_values = np.linspace(0.5, 0.8, 20)  # P(Predict Oil | Oil)
q_values = np.linspace(0.5, 0.8, 20)  # P(Predict No Oil | No Oil)


# ## Sensitivity Analysis and Compute EMV

# In[5]:


results = []

for p in p_values:
    for q in q_values:
        # Total prediction probabilities
        P_Predict_O = p * P_O + (1 - q) * P_NO
        P_Predict_NO = (1 - p) * P_O + q * P_NO

        # Bayes updates
        P_O_given_Predict_O = (p * P_O) / P_Predict_O
        P_O_given_Predict_NO = ((1 - p) * P_O) / P_Predict_NO

        # EMV for each prediction
        EMV_Predict_O = max(
            P_O_given_Predict_O * net_profit_if_oil + (1 - P_O_given_Predict_O) * (-cost_of_land),
            -cost_of_land
        )
        EMV_Predict_NO = max(
            P_O_given_Predict_NO * net_profit_if_oil + (1 - P_O_given_Predict_NO) * (-cost_of_land),
            -cost_of_land
        )

        # EMV if expert is hired
        EMV_Hire = P_Predict_O * EMV_Predict_O + P_Predict_NO * EMV_Predict_NO

        # EMV if no expert
        EMV_NotHire = P_O * net_profit_if_oil + P_NO * (-cost_of_land)

        # Optimal buy strategy
        EMV_Buy = max(EMV_Hire, EMV_NotHire)

        # Final expected value: 60% Buy
        EMV_Total = 0.6 * EMV_Buy  # + 0.4 * 0 (Do nothing)

        results.append((p, q, EMV_Total))


# ## EMV Dot Plot

# In[6]:


results = np.array(results)

# Plot
plt.figure(figsize=(10, 6))
scatter = plt.scatter(results[:, 0], results[:, 1], c=results[:, 2], cmap='viridis', s=100, edgecolors='k')
plt.colorbar(scatter, label='Expected Monetary Value ($)')
plt.xlabel('P(Predict Oil | Oil)')
plt.ylabel('P(Predict No Oil | No Oil)')
plt.title('Sensitivity Analysis: EMV vs Expert Accuracy')
plt.grid(True)
plt.show()


# ### Plot Legend
# 
# - **X-axis**: Expert's true positive rate.
# - **Y-axis**: Expert's true negative rate.
# - **Color**: Expected monetary value (EMV) in dollars.
# 
# 
# ### Observations
# - Higher expert accuracy → higher EMV.
# - If expert predictions are poor (≤ 0.6), buying land is usually suboptimal.
# - Investing in the expert is only beneficial if both `P(Predict Oil | Oil)` and `P(Predict No Oil | No Oil)` are strong.

