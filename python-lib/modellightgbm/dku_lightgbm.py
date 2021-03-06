from lightgbm import LGBMClassifier, LGBMRegressor
        
class DkuLGBMClassifier(LGBMClassifier):
    
    def __init__(self, boosting_type='gbdt', num_leaves=31, max_depth=-1, learning_rate=0.1, n_estimators=100, 
                 subsample_for_bin=200000, objective=None, class_weight=None, min_split_gain=0.0, min_child_weight=0.001, 
                 min_child_samples=20, subsample=1.0, subsample_freq=0, colsample_bytree=1.0, reg_alpha=0.0, 
                 reg_lambda=0.0, random_state=None, n_jobs=-1, silent=True, importance_type='split', 
                 early_stopping_rounds=None, early_stopping=None):

        self.early_stopping_rounds = early_stopping_rounds
        super(DkuLGBMClassifier, self).__init__(boosting_type=boosting_type, num_leaves=num_leaves, max_depth=max_depth, learning_rate=learning_rate, n_estimators=n_estimators, 
                                             subsample_for_bin=subsample_for_bin, objective=objective, class_weight=class_weight, min_split_gain=min_split_gain, min_child_weight=min_child_weight, 
                                             min_child_samples=20, subsample=1.0, subsample_freq=0, colsample_bytree=1.0, reg_alpha=0.0, 
                                             reg_lambda=reg_lambda, random_state=random_state, n_jobs=n_jobs, silent=silent, importance_type=importance_type)
        
    def fit(self, X, y, sample_weight=None, init_score=None, eval_set=None, eval_names=None, eval_sample_weight=None, 
            eval_class_weight=None, eval_init_score=None, eval_metric=None, early_stopping_rounds=None, verbose=True, 
            feature_name='auto', categorical_feature='auto', callbacks=None):
        
        return super(DkuLGBMClassifier, self).fit(X, y, init_score=init_score, eval_set=eval_set or [(X, y)], eval_names=eval_names, eval_sample_weight=eval_sample_weight, 
                                               eval_class_weight=eval_class_weight, eval_init_score=eval_init_score, eval_metric=eval_metric, verbose=verbose, 
                                               feature_name=feature_name, categorical_feature=categorical_feature, callbacks=callbacks, early_stopping_rounds=self.early_stopping_rounds)          

class DkuLGBMRegressor(LGBMRegressor):
    
    def __init__(self, boosting_type='gbdt', num_leaves=31, max_depth=-1, learning_rate=0.1, n_estimators=100, 
                 subsample_for_bin=200000, objective=None, class_weight=None, min_split_gain=0.0, min_child_weight=0.001, 
                 min_child_samples=20, subsample=1.0, subsample_freq=0, colsample_bytree=1.0, reg_alpha=0.0, 
                 reg_lambda=0.0, random_state=None, n_jobs=-1, silent=True, importance_type='split', 
                 early_stopping_rounds=None, early_stopping=None):
        self.early_stopping_rounds = early_stopping_rounds
        super(DkuLGBMRegressor, self).__init__(boosting_type=boosting_type, num_leaves=num_leaves, max_depth=max_depth, learning_rate=learning_rate, n_estimators=n_estimators, 
                                             subsample_for_bin=subsample_for_bin, objective=objective, class_weight=class_weight, min_split_gain=min_split_gain, min_child_weight=min_child_weight, 
                                             min_child_samples=20, subsample=1.0, subsample_freq=0, colsample_bytree=1.0, reg_alpha=0.0, 
                                             reg_lambda=reg_lambda, random_state=random_state, n_jobs=n_jobs, silent=silent, importance_type=importance_type)
        
    def fit(self, X, y, sample_weight=None, init_score=None, eval_set=None, eval_names=None, eval_sample_weight=None, 
            eval_init_score=None, eval_metric=None, early_stopping_rounds=None, verbose=True, 
            feature_name='auto', categorical_feature='auto', callbacks=None):
        
        return super(DkuLGBMRegressor, self).fit(X, y, init_score=init_score, eval_set=eval_set or [(X, y)], eval_names=eval_names, eval_sample_weight=eval_sample_weight, 
                                               eval_init_score=eval_init_score, eval_metric=eval_metric, verbose=verbose, 
                                               feature_name=feature_name, categorical_feature=categorical_feature, callbacks=callbacks, early_stopping_rounds=self.early_stopping_rounds)  