from metrics import hit_k, mean_hit_k, average_precision_k, mean_average_precision_k
class Evaluation:
    def hit_k(self, predicted, actual, k):
        return hit_k(predicted, actual, k)
    
    def mean_hit_k(self, predicted_list, labeled_list, k=10):
        return mean_hit_k(predicted_list, labeled_list, k)
    
    def average_precision_k(predicted, actual, k):
        return average_precision_k(predicted, actual, k)
    
    def mean_average_precision_k(predicted_list, labeled_list, k=10):
        return mean_average_precision_k(predicted_list, labeled_list, k)
    
    def get_evaluate_report(self, predicted_list, labeled_list, k_list=[10, 5, 3, 1]):
        report_dict = {}
        for k in k_list:
            report_dict[f"mean_hit@{k}"] = self.mean_hit_k(predicted_list, labeled_list, k)
            report_dict[f"map@{k}"] = self.mean_average_precision_k(predicted_list, labeled_list, k)

        return report_dict
    
    def get_st_report(self, labeled_df, selected_query_map_df, model, k_list=[10, 5, 3, 1]):
        '''
            Generate evaluation report for SentenceTransformer model.
        '''
        pass