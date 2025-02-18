import numpy as np

def create_interaction_matrix(df):
    """
    Create a user-product interaction matrix.
    """
    interaction_matrix = df.pivot(index='user_id', columns='prod_id', values='rating').fillna(0)
    return interaction_matrix

def calculate_density(matrix):
    """
    Calculate the density of the interaction matrix.
    """
    given_ratings = np.count_nonzero(matrix)
    possible_ratings = matrix.shape[0] * matrix.shape[1]
    density = (given_ratings / possible_ratings) * 100
    print(f'Density of the interaction matrix: {density:.2f}%')