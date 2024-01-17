def hitk(predicted, actual, k):
    top_k_predictions = predicted[:k]
    total_hits = 0

    for ac in actual:
        if ac in top_k_predictions:
            total_hits += 1.0
    
    if not actual:
        return 0.0

    return total_hits / len(actual)


def mean_hitk(predicted_list, labeled_list, k=10):
    hitk_scores = [
        hitk(predictions, labels, k)
        for predictions, labels in zip(predicted_list, labeled_list)
    ]
    mean_hitk_score = sum(hitk_scores) / k

    return mean_hitk_score


def apk(predicted, actual, k):
    if len(predicted) > k:
        predicted = predicted[:k]

    score = 0.0
    num_hits = 0

    for i, p in enumerate(predicted):
        if p in actual and p not in predicted[:i]:
            num_hits += 1
            score += num_hits / (i + 1.0)

    if not actual:
        return 0.0

    # return score / max(num_hits, 1)
    return score / min(len(actual), k)
    # return score / min(len(predicted), k)


def mapk(predicted_list, labeled_list, k=10):
    total_average_precision = 0.0

    for i in range(len(labeled_list)):
        true_labels = labeled_list[i]
        predicted = predicted_list[i]

        average_precision = apk(predicted, true_labels, k)
        total_average_precision += average_precision

    map_at_k = total_average_precision / len(labeled_list)
    return map_at_k
