import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def generate_activity_report():
    # 1. Load the data
    try:
        df = pd.read_csv('detections.csv')
        df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    except FileNotFoundError:
        print("No detections.csv found. Run the AI for a bit first!")
        return

    # 2. Set the style
    sns.set_theme(style="darkgrid")
    plt.figure(figsize=(12, 6))

    # 3. Group by minute to see "Traffic Flow"
    # This shows how many people/dogs were seen per minute
    df['Minute'] = df['Timestamp'].dt.floor('min')
    activity = df.groupby(['Minute', 'Class']).size().unstack(fill_value=0)

    # 4. Plot
    activity.plot(kind='line', marker='o', ax=plt.gca())
    
    plt.title('Mori Point Trail Activity (Live AI Data)', fontsize=15)
    plt.xlabel('Time', fontsize=12)
    plt.ylabel('Count of Detections', fontsize=12)
    plt.legend(title='Object Class')
    
    # 5. Save for the website
    plt.tight_layout()
    plt.savefig('outputs/trail_activity.png')
    print("Report saved to outputs/trail_activity.png")

if __name__ == "__main__":
    generate_activity_report()