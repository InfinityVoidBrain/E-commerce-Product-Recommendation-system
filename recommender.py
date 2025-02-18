from sklearn.metrics.pairwise import cosine_similarity

def find_similar_users(user_index, interaction_matrix, top_n=10):
    """
    Find top-N similar users based on cosine similarity.
    """
    similarity_scores = []
    for user in range(interaction_matrix.shape[0]):
        sim = cosine_similarity([interaction_matrix.loc[user_index]], [interaction_matrix.loc[user]])
        similarity_scores.append((user, sim[0][0]))

    similarity_scores.sort(key=lambda x: x[1], reverse=True)
    similar_users = [user[0] for user in similarity_scores[1:top_n+1]]  # Exclude the user itself
    similarity_values = [user[1] for user in similarity_scores[1:top_n+1]]

    return similar_users, similarity_values

def generate_recommendations(user_index, interaction_matrix, num_recommendations=5):
    """
    Generate product recommendations for a user.
    """
    similar_users, _ = find_similar_users(user_index, interaction_matrix)
    user_interactions = set(interaction_matrix.columns[np.where(interaction_matrix.loc[user_index] > 0)])
    recommendations = []

    for similar_user in similar_users:
        if len(recommendations) < num_recommendations:
            similar_user_interactions = set(interaction_matrix.columns[np.where(interaction_matrix.loc[similar_user] > 0)])
            new_recommendations = list(similar_user_interactions.difference(user_interactions))
            recommendations.extend(new_recommendations)
            user_interactions = user_interactions.union(similar_user_interactions)
        else:
            break

    return recommendations[:num_recommendations]