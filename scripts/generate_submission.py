import pandas as pd
import os

def generate_dummy_submission(clicks_path, output_path, top_k=20):
    """
    Generate a dummy submission using most popular products.
    """
    clicks = pd.read_csv(clicks_path)
    top_products = clicks['product_id'].value_counts().head(top_k).index.tolist()
    sessions = clicks['session_id'].unique()
    submission = []
    for session in sessions:
        submission.append({'session_id': session, 'predicted_products': ' '.join(map(str, top_products))})
    sub_df = pd.DataFrame(submission)
    sub_df.to_csv(output_path, index=False)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--clicks', type=str, required=True, help='Path to clicks CSV')
    parser.add_argument('--output', type=str, required=True, help='Path to output submission CSV')
    parser.add_argument('--top_k', type=int, default=20, help='Number of top products to use')
    args = parser.parse_args()
    generate_dummy_submission(args.clicks, args.output, args.top_k)
