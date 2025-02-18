import matplotlib.pyplot as plt

def analyze_data(df):
    """
    Perform basic data analysis and visualization.
    """
    print("Dataset Info:")
    df.info()

    print("\nMissing Values:")
    print(df.isna().sum())

    print("\nRating Summary:")
    print(df['rating'].describe())

    # Plot rating distribution
    plt.figure(figsize=(12, 6))
    df['rating'].value_counts(normalize=True).plot(kind='bar')
    plt.title('Rating Distribution')
    plt.show()

    print("\nNumber of Unique Users and Products:")
    print('Unique Users:', df['user_id'].nunique())
    print('Unique Products:', df['prod_id'].nunique())