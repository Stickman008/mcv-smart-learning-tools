import numpy as np
import pandas as pd
from scipy.stats import pearsonr, spearmanr
from sklearn.metrics import mean_absolute_error, mean_squared_error
from utils.constants import PREDICT_SUFFIX, PATTERN_COL_PREFIX


class Evaluation:
    def format_default_list_to_predict_df(self, predicts_list):
        transposed_list = list(map(list, zip(*predicts_list)))

        df = pd.DataFrame(
            {
                str(i + 1) + PREDICT_SUFFIX: predictions
                for i, predictions in enumerate(transposed_list)
            }
        )
        return df

    def get_report(self, structurer, predict_df):
        report = dict()

        for pattern_number in range(1, len(structurer.pattern_list) + 1):
            print(pattern_number)
            ground_truth_pattern = structurer.score_df[f"pattern1_{pattern_number}"]
            predicted_pattern = predict_df[f"{pattern_number}{PREDICT_SUFFIX}"]
            print(ground_truth_pattern, predicted_pattern)

            pearson_corr, pearson_p_value = pearsonr(
                ground_truth_pattern, predicted_pattern
            )
            spearman_corr, spearman_p_value = spearmanr(
                ground_truth_pattern, predicted_pattern
            )
            mae = mean_absolute_error(ground_truth_pattern, predicted_pattern)
            rmse = np.sqrt(mean_squared_error(ground_truth_pattern, predicted_pattern))

            report[f"{PATTERN_COL_PREFIX}_{pattern_number}"] = {
                "pearson": pearson_corr,
                "pearson_p_value": pearson_p_value,
                "spearman": spearman_corr,
                "spearman_p_value": spearman_p_value,
                "mae": mae,
                "rmse": rmse,
            }

        # Aggregate metrics for all patterns
        total_report = {
            "total_pearson": np.mean(
                [
                    report[f"{PATTERN_COL_PREFIX}_{i}"]["pearson"]
                    for i in range(1, len(structurer.pattern_list) + 1)
                ]
            ),
            "total_spearman": np.mean(
                [
                    report[f"{PATTERN_COL_PREFIX}_{i}"]["spearman"]
                    for i in range(1, len(structurer.pattern_list) + 1)
                ]
            ),
            "total_mae": np.mean(
                [
                    report[f"{PATTERN_COL_PREFIX}_{i}"]["mae"]
                    for i in range(1, len(structurer.pattern_list) + 1)
                ]
            ),
            "total_rmse": np.mean(
                [
                    report[f"{PATTERN_COL_PREFIX}_{i}"]["rmse"]
                    for i in range(1, len(structurer.pattern_list) + 1)
                ]
            ),
        }
        report["total"] = total_report

        return report
