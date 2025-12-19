import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def generate_activity_report():
    # 1. Load the data 
    try:
        # Match your actual file name
        df = pd.read_csv('trail_log.csv')
        
        # Match your lowercase column names: 'timestamp' and 'label'
        df['timestamp'] = pd.to_datetime(df['timestamp'])
    except FileNotFoundError:
        print("No trail_log.csv found. Run the AI for a bit first!")
        return
    except KeyError as e:
        print(f"Column name error: {e}. Current columns: {df.columns.tolist()}")
        return

    # 2. Set the style
    sns.set_theme(style="darkgrid")
    plt.figure(figsize=(12, 6))

    # 3. Group by minute
    # Use 'timestamp' and 'label' to match your CSV
    df['Minute'] = df['timestamp'].dt.floor('min')
    activity = df.groupby(['Minute', 'label']).size().unstack(fill_value=0)

    # 4. Plot
    activity.plot(kind='line', marker='o', ax=plt.gca())
    
    plt.title('Mori Point Trail Activity (Live AI Data)', fontsize=15)
    plt.xlabel('Time', fontsize=12)
    plt.ylabel('Count of Detections', fontsize=12)
    plt.legend(title='Object Category')
    
    # 5. Save and Show
    if not os.path.exists('outputs'):
        os.makedirs('outputs')
        
    plt.tight_layout()
    plt.savefig('outputs/trail_activity.png')
    print("✅ Success! Report saved to outputs/trail_activity.png")
    plt.show()

if __name__ == "__main__":
    generate_activity_report()