import matplotlib.pyplot as plt

def plot_editing_levels(group1, group2, title="Editing Level Comparison"):
    """Create a boxplot to compare editing levels."""
    data = [group1["Editing_Level"], group2["Editing_Level"]]
    plt.boxplot(data, labels=["Mettl3", "Control"])
    plt.title(title)
    plt.ylabel("Editing Level")
    plt.show()
