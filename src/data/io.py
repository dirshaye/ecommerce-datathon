import pandas as pd
import os

def load_sessions(path):
    """Load session data (clicks/orders) from CSV."""
    return pd.read_csv(path)

def load_clicks(path):
    """Load click events from CSV."""
    return pd.read_csv(path)

def load_orders(path):
    """Load order events from CSV."""
    return pd.read_csv(path)

def load_products(path):
    """Load product metadata from CSV."""
    return pd.read_csv(path)
