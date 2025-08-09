import lightgbm as lgb
import pandas as pd
from sklearn.model_selection import train_test_split

def train_lgbm_ranker(X, y, group):
    """Train a LightGBM ranker (LambdaMART)."""
    params = {
        'objective': 'lambdarank',
        'metric': 'ndcg',
        'verbosity': -1,
        'boosting_type': 'gbdt',
        'random_state': 42
    }
    train_data = lgb.Dataset(X, label=y, group=group)
    model = lgb.train(params, train_data, num_boost_round=100)
    return model

def predict_lgbm_ranker(model, X):
    """Predict scores with trained LightGBM ranker."""
    return model.predict(X)
