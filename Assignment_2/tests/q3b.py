OK_FORMAT = True

test = {   'name': 'q3b',
    'points': 6,
    'suites': [   {   'cases': [   {'code': ">>> assert np.isclose(lda_eval['Model_Accuracy'], 0.8186, atol=.9)\n", 'hidden': False, 'locked': False},
                                   {'code': ">>> assert np.isclose(qda_eval['Model_Accuracy'], 0.2831, atol=.9)\n", 'hidden': False, 'locked': False},
                                   {   'code': '>>> assert np.isclose(logit_eval[\'Model_Accuracy\'], 0.8007, atol=.9), "Logistic Regression model\'s accuracy is not as expected."\n',
                                       'hidden': False,
                                       'locked': False},
                                   {'code': '>>> assert np.isclose(gnb_eval[\'Model_Accuracy\'], 0.3307, atol=.9), "NB  model\'s accuracy is not as expected."\n', 'hidden': False, 'locked': False},
                                   {'code': '>>> assert np.isclose(knn_eval[\'Model_Accuracy\'], 0.8065, atol=.9), "Knn model\'s accuracy is not as expected."\n', 'hidden': False, 'locked': False},
                                   {'code': '>>> assert np.isclose(dt_eval[\'Model_Accuracy\'], 0.8100, atol=.9), "DT model\'s accuracy is not as expected."\n', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
