def f1_micro(y_true, y_pred) -> float:
    """
    Compute micro-averaged F1 for multi-class integer labels.
    """
    # Write code here
    tp, wrong = 0, 0
    
    for true, pred in zip(y_true, y_pred):
        if true == pred:
            tp += 1
        else:
            wrong += 1

    return tp/len(y_true)