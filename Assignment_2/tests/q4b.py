OK_FORMAT = True

test = {   'name': 'q4b',
    'points': 8,
    'suites': [   {   'cases': [   {   'code': '>>> \n'
                                               '>>> assert college.shape == (777, 19), "Data is not loaded correctly"\n'
                                               '>>> assert \'Private_Yes\' in set(X.columns), "Private_Yes is not found."\n',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> \n'
                                               '>>> assert X_train.shape == (543,17)\n'
                                               '>>> assert X_test.shape == (234,17)\n'
                                               '>>> assert isinstance(fit_lr, LinearRegression)\n'
                                               '>>> assert np.isclose(lr_error, 1931803.194207031, atol=5), "Error is not as expected"\n',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> \n'
                                               '>>> assert isinstance(fit_rcv, RidgeCV)\n'
                                               '>>> assert np.isclose(rcv_error, 1793966.504233349, atol=5),  "Error is not as expected"\n'
                                               '>>> assert np.isclose(fit_rcv.alpha_, 0.01, atol=.05), "alpha is not as expected"\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
