import pandas as pd
import matplotlib.pyplot as plt

def analyze_data(data_path):
    # Load processed data
    df = pd.read_csv(data_path)
    
    # Analysis of block rewards and mining difficulty trends
    plt.figure(figsize=(10, 5))
    plt.plot(df['date'], df['block_reward'], label='Block Reward')
    plt.plot(df['date'], df['mining_difficulty'], label='Mining Difficulty')
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.title('Block Rewards and Mining Difficulty Over Time')
    plt.legend()
    plt.show()

    # Miner distribution and concentration analysis
    miner_counts = df['miner'].value_counts()
    plt.figure(figsize=(10, 5))
    plt.bar(miner_counts.index, miner_counts.values)
    plt.xlabel('Miner')
    plt.ylabel('Number of Blocks Mined')
    plt.title('Miner Distribution')
    plt.xticks(rotation=90)
    plt.show()

    # Profitability analysis
    df['profitability'] = df['block_reward'] - df['mining_cost']
    plt.figure(figsize=(10, 5))
    plt.plot(df['date'], df['profitability'], label='Profitability')
    plt.xlabel('Date')
    plt.ylabel('Profitability')
    plt.title('Profitability Over Time')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    analyze_data('../data/processed/mining_analysis_data.csv')
