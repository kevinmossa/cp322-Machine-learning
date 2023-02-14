OK_FORMAT = True

test = {   'name': 'q2d',
    'points': 4,
    'suites': [   {   'cases': [   {   'code': '>>> dt_model = DecisionTreeClassifier(random_state=RANDOM_STATE)\n'
                                               '>>> dt_predictions = dt_model.fit(X_train, y_train).predict(X_test)\n'
                                               '>>> dt_predictions_proba = dt_model.fit(X_train, y_train).predict_proba(X_test)\n'
                                               '>>> evaluation = get_performance_metrics(y_test, dt_predictions,dt_predictions_proba)\n'
                                               ">>> assert np.isclose(evaluation['Model_Accuracy'], 0.8086, atol = 2)\n",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
