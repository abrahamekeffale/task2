import pandas as pd

def load_data(file_path):
    df = pd.read_csv(file_path, sep='\t')
    print(f"Columns in {file_path}: {df.columns}")  # Debugging line
    return df

def merge_samples(sample_files):
    dfs = [calculate_editing_level(load_data(file)) for file in sample_files]
    merged_df = pd.concat(dfs)
    return merged_df

def calculate_editing_level(df):
    required_columns = ['Count_A', 'Count_C', 'Count_G', 'Count_T']
    for col in required_columns:
        if col not in df.columns:
            raise ValueError(f"Column {col} is missing from the data")
    df["Editing_Level"] = df["Count_G"] / (df["Count_A"] + df["Count_C"] + df["Count_G"] + df["Count_T"])
    df["Gene"] = df["#CHR"]  # Assuming '#CHR' column can be used as 'Gene' for demonstration
    return df