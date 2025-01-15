import pandas as pd
from scipy.stats import ttest_ind

def compute_mean_editing(df):
    return df["Editing_Level"].mean()

def perform_ttest(mettl3_data, control_data):
    t_stat, p_val = ttest_ind(mettl3_data["Editing_Level"], control_data["Editing_Level"])
    return p_val

def analyze_genes(genes_of_interest, mettl3_data, control_data):
    results = []
    for gene in genes_of_interest["gene_name"]:  # Updated to use 'gene_name'
        mettl3_gene_data = mettl3_data[mettl3_data["Gene"] == gene]
        control_gene_data = control_data[control_data["Gene"] == gene]
        mean_mettl3 = compute_mean_editing(mettl3_gene_data)
        mean_control = compute_mean_editing(control_gene_data)
        p_val = perform_ttest(mettl3_gene_data, control_gene_data)
        results.append({
            "Gene": gene,
            "Mean_Mettl3": mean_mettl3,
            "Mean_Control": mean_control,
            "P_Value": p_val
        })
    return results