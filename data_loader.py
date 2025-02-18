import pandas as pd

def load_data(filepath):
    """
    Load the dataset and preprocess it.
    """
    df = pd.read_csv(filepath, header=None)  # No headers in the data file
    df.columns = ['user_id', 'prod_id', 'rating', 'timestamp']  # Add column names
    df = df.drop('timestamp', axis=1)  # Drop timestamp column
    return df

def preprocess_data(df, min_ratings=50):
    """
    Filter users with at least `min_ratings` ratings.
    """
    user_rating_counts = df['user_id'].value_counts()
    df_filtered = df[df['user_id'].isin(user_rating_counts[user_rating_counts >= min_ratings].index)]
    return df_filtered