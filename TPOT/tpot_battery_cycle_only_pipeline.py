import numpy as np
import pandas as pd
from sklearn.ensemble import AdaBoostRegressor
from sklearn.linear_model import SGDRegressor
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline, make_union
from sklearn.preprocessing import RobustScaler
from tpot.builtins import StackingEstimator

# NOTE: Make sure that the outcome column is labeled 'target' in the data file
tpot_data = pd.read_csv('PATH/TO/DATA/FILE', sep='COLUMN_SEPARATOR', dtype=np.float64)
features = tpot_data.drop('target', axis=1)
training_features, testing_features, training_target, testing_target = \
            train_test_split(features, tpot_data['target'], random_state=None)

# Average CV score on the training set was: -0.0007889327968975957
exported_pipeline = make_pipeline(
    RobustScaler(),
    StackingEstimator(estimator=AdaBoostRegressor(learning_rate=0.001, loss="linear", n_estimators=100)),
    RobustScaler(),
    SGDRegressor(alpha=0.001, eta0=0.01, fit_intercept=True, l1_ratio=0.0, learning_rate="constant", loss="huber", penalty="elasticnet", power_t=0.5)
)

exported_pipeline.fit(training_features, training_target)
results = exported_pipeline.predict(testing_features)
