import numpy as np

def recall_at_k(y_true, y_pred, k=20, weights=None):
    """
    Compute weighted Recall@K for click and purchase events.
    y_true: list of sets (ground truth items per session)
    y_pred: list of lists (predicted items per session, ordered)
    k: int, cutoff
    weights: list or array, same length as y_true, weight per session (optional)
    Returns: float, weighted recall@k
    """
    recalls = []
    for true_items, pred_items in zip(y_true, y_pred):
        pred_topk = set(pred_items[:k])
        if not true_items:
            recalls.append(0.0)
        else:
            recalls.append(len(true_items & pred_topk) / len(true_items))
    recalls = np.array(recalls)
    if weights is not None:
        recalls = recalls * np.array(weights)
        return recalls.sum() / np.sum(weights)
    return recalls.mean()
