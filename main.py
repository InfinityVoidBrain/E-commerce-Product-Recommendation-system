from data_loader import load_data, preprocess_data
from data_analyzer import analyze_data
from interaction_matrix import create_interaction_matrix, calculate_density
from recommender import find_similar_users, generate_recommendations

def main():
    # Load and preprocess data
    filepath = '/content/drive/MyDrive/ratings_Electronics.csv'
    df = load_data(filepath)
    df_filtered = preprocess_data(df, min_ratings=50)

    # Analyze data
    analyze_data(df_filtered)

    # Create interaction matrix
    interaction_matrix = create_interaction_matrix(df_filtered)
    calculate_density(interaction_matrix)

    # Example: Find similar users and generate recommendations
    user_index = 3
    similar_users, similarity_scores = find_similar_users(user_index, interaction_matrix)
    print(f"\nTop 10 similar users to user {user_index}: {similar_users}")
    print(f"Similarity scores: {similarity_scores}")

    recommendations = generate_recommendations(user_index, interaction_matrix)
    print(f"\nTop 5 recommendations for user {user_index}: {recommendations}")

if __name__ == "__main__":
    main()