import pandas as pd

def preprocess_data(input_path, output_path):
    # Load raw data
    df = pd.read_csv(input_path)
    
    # Data cleaning and preprocessing steps
    df['date'] = pd.to_datetime(df['date'])
    df.sort_values(by='date', inplace=True)
    
    # Save processed data
    df.to_csv(output_path, index=False)

if __name__ == "__main__":
    preprocess_data('../data/raw/blockchain_data.csv', '../data/processed/mining_analysis_data.csv')
