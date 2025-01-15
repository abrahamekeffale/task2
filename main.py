import os
from src.data_preprocessing import load_data, merge_samples
from src.editing_analysis import compute_mean_editing, perform_ttest, analyze_genes
import pandas as pd

# File paths
genes_file = "data/genes_of_interest.tsv"
mettl3_files = [
    "data/Mettl3_1.tsv",
    "data/Mettl3_2.tsv",
    "data/Mettl3_3.tsv"
]
control_files = [
    "data/Mettl3_ctrl_1.tsv",
    "data/Mettl3_ctrl_2.tsv",
    "data/Mettl3_ctrl_3.tsv"
]

# Load data
genes_of_interest = load_data(genes_file)
mettl3_data = merge_samples(mettl3_files)
control_data = merge_samples(control_files)

# Overall analysis
mettl3_mean = compute_mean_editing(mettl3_data)
control_mean = compute_mean_editing(control_data)
overall_pval = perform_ttest(mettl3_data, control_data)

# Gene-specific analysis
results = analyze_genes(genes_of_interest, mettl3_data, control_data)
results_df = pd.DataFrame(results)

# Save results
os.makedirs("results", exist_ok=True)
results_df.to_csv("results/gene_editing_results.csv", index=False)
with open("results/overall_results.txt", "w") as f:
    f.write(f"Overall mean editing change: {mettl3_mean - control_mean}\n")
    f.write(f"Overall p-value: {overall_pval}\n")