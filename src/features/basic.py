import pandas as pd

def compute_popularity_features(clicks_df, orders_df):
    """Compute product popularity features from clicks and orders."""
    click_counts = clicks_df['product_id'].value_counts().rename('click_popularity')
    order_counts = orders_df['product_id'].value_counts().rename('order_popularity')
    popularity = pd.concat([click_counts, order_counts], axis=1).fillna(0)
    popularity['total_popularity'] = popularity['click_popularity'] + popularity['order_popularity']
    return popularity.reset_index().rename(columns={'index': 'product_id'})

def compute_session_stats(sessions_df):
    """Compute basic session statistics."""
    session_lengths = sessions_df.groupby('session_id').size().rename('session_length')
    return session_lengths.reset_index()
