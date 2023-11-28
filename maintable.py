
import os
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

plt.rcParams['font.size'] = 16
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['CMU Serif'] 

# Data string to be parsed
data_string_7b = """
Corrigibility,0.99,0.81,0.46
Power-Seeking,0.71,0.31,0.18
Survival Instinct,0.78,0.62,0.44
Myopia,0.86,0.50,0.29
Coordination with other AIs,0.62,0.38,0.26
Sycophancy,0.23,0.09,0.01"""

data_string_13b = """
Corrigibility,0.98,0.74,0.35
Power-Seeking,0.60,0.31,0.20
Survival Instinct,0.93,0.62,0.35
Myopia,0.90,0.40,0.25
Coordination with other AIs,0.49,0.36,0.30
Sycophancy,0.13,0.04,0.02"""

def plot(data_string, model):
    # Parsing the data
    lines = data_string.strip().split('\n')
    categories, added, neutral, subtracted = [], [], [], []

    for line in lines:
        parts = line.split(',')
        categories.append(parts[0])
        added.append(float(parts[1]) * 100)  # Convert fraction to percentage
        neutral.append(float(parts[2]) * 100)  # Convert fraction to percentage
        subtracted.append(float(parts[3]) * 100)  # Convert fraction to percentage

    # Redefining the x-axis values
    x_values = [1, 0, -1]  # Corresponding to Added, Neutral, and Subtracted
    labels = ["Added", "Baseline", "Subtracted"]

    # Plotting the parsed data
    plt.figure(figsize=(6, 6))

    colors = sns.color_palette("colorblind", len(categories))

    for i, category in enumerate(categories):
        y_values = [added[i], neutral[i], subtracted[i]]
        plt.plot(x_values, y_values, marker='o', label=category, linestyle='--', linewidth=3, markersize=10, color=colors[i])

    # Adding titles and labels
    plt.xlabel("Contrastive Activation Addition setting")
    plt.ylabel(f"% of responses matching behavior")
    plt.xticks(x_values, labels)
    plt.legend()

    ax = plt.gca()  # Get current axes
    ax.set_xticks(x_values)
    ax.set_xticklabels(labels)
    for i, tick in enumerate(ax.get_xticklabels()):
        if tick.get_text() == 'Added':
            tick.set_color('#D20065')
        elif tick.get_text() == 'Subtracted':
            tick.set_color('#0093B3')
        else:
            tick.set_color('black')

    # Display the plot
    plt.tight_layout()
    plt.savefig(f"behavioral_responses_{model}.png", format="png")
    plt.savefig(f"behavioral_responses_{model}.pdf", format="pdf")

plot(data_string_7b, "7B")
plot(data_string_13b, "13B")