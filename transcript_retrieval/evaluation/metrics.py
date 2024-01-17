def hit_k(predicted, actual, k):
    if len(predicted) > k:
        top_k_predictions = predicted[:k]
    
    return 1.0 if any(ac in top_k_predictions for ac in actual) else 0.0
    

# def average_hit_k(predicted, actual, k):
#     top_k_predictions = predicted[:k]
#     total_hits = 0
    
#     for p in top_k_predictions:
#         if p in actual:
#             total_hits += 1.0
    
#     if not actual:
#         return 0.0

#     # return total_hits / len(actual)
#     # return total_hits / min(len(predicted), k)
#     return total_hits / min(len(actual), k)


def mean_hit_k(predicted_list, labeled_list, k=10):
    hit_k_scores = [
        hit_k(predictions, labels, k)
        for predictions, labels in zip(predicted_list, labeled_list)
    ]
    
    mean_hit_k_score = sum(hit_k_scores) / len(predicted_list)
    return mean_hit_k_score


def average_precision_k(predicted, actual, k):
    if len(predicted) > k:
        predicted = predicted[:k]

    score = 0.0
    true_positives = 0

    for i, p in enumerate(predicted):
        if p in actual and p not in predicted[:i]:
            true_positives += 1
            score += true_positives / (i + 1.0)

    if not actual:
        return 0.0

    # return score / max(true_positives, 1)
    # return score / min(len(actual), k)
    return score / min(len(predicted), k)


def mean_average_precision_k(predicted_list, labeled_list, k=10):
    total_average_precision = 0.0

    for i in range(len(labeled_list)):
        true_labels = labeled_list[i]
        predicted = predicted_list[i]

        average_precision = average_precision_k(predicted, true_labels, k)
        total_average_precision += average_precision

    map_k = total_average_precision / len(labeled_list)
    return map_k
