OK_FORMAT = True

test = {   'name': 'q3c',
    'points': 12,
    'suites': [   {   'cases': [   {   'code': '>>> \n'
                                               '>>> assert np.isclose(k_accuracy_lda, np.array([0.9034274332028298,\n'
                                               '...  0.9070677931176592,\n'
                                               '...  0.9069304210454014,\n'
                                               '...  0.9041829796002473,\n'
                                               '...  0.9047324678892781,\n'
                                               '...  0.8993062710350985,\n'
                                               '...  0.9017035307047672,\n'
                                               '...  0.9069240280258277,\n'
                                               '...  0.9041763978568484,\n'
                                               '...  0.9034894903146037]), atol= 0.3).all(), "The returned accuracy for LDA does not meet the requirements."\n',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> \n'
                                               '>>> assert np.isclose(k_accuracy_qda, np.array([0.000206058108386565,\n'
                                               '...  0.000206058108386565,\n'
                                               '...  0.35496943471392267,\n'
                                               '...  6.868603612885501e-05,\n'
                                               '...  0.3634865031939007,\n'
                                               '...  0.00013737207225771001,\n'
                                               '...  6.869075422448138e-05,\n'
                                               '...  0.00020607226267344415,\n'
                                               '...  6.869075422448138e-05,\n'
                                               '...  0.35588679763703807]), atol= 0.3).all(), "The returned accuracy for QDA does not meet the requirements."\n',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> \n'
                                               '>>> assert np.isclose(k_accuracy_logit, np.array([0.6378185314925475,\n'
                                               '...  0.6532042035854111,\n'
                                               '...  0.637612473384161,\n'
                                               '...  0.647091146369943,\n'
                                               '...  0.6373377292396456,\n'
                                               '...  0.6379559035648052,\n'
                                               '...  0.6603242203599395,\n'
                                               '...  0.6468608325319412,\n'
                                               '...  0.6388927050419013,\n'
                                               '...  0.6491963181755736]), atol= 0.3).all(), "The returned accuracy for LR does not meet the requirements."\n',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> \n'
                                               '>>> assert np.isclose(k_accuracy_knn, np.array([0.8859124939899718,\n'
                                               '...  0.8985507246376812,\n'
                                               '...  0.8923689813860842,\n'
                                               '...  0.8697712754996909,\n'
                                               '...  0.8906518304828628,\n'
                                               '...  0.8768459372209629,\n'
                                               '...  0.887278472317626,\n'
                                               '...  0.876425333150158,\n'
                                               '...  0.8530017859596098,\n'
                                               '...  0.8850803681824426]), atol= 0.3).all(), "The returned accuracy for NB does not meet the requirements."\n',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> \n'
                                               '>>> assert np.isclose(k_accuracy_dt, np.array([0.9034274332028298,\n'
                                               '...  0.9070677931176592,\n'
                                               '...  0.9069304210454014,\n'
                                               '...  0.9041829796002473,\n'
                                               '...  0.9047324678892781,\n'
                                               '...  0.8993062710350985,\n'
                                               '...  0.9017035307047672,\n'
                                               '...  0.9069240280258277,\n'
                                               '...  0.9041763978568484,\n'
                                               '...  0.9034894903146037]), atol= 0.3).all(), "The returned accuracy for DT does not meet the requirements."\n',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> \n'
                                               '>>> assert np.isclose(k_accuracy_gnb, np.array([0.4827941479497218,\n'
                                               '...  0.4378047942853218,\n'
                                               '...  0.43910982897177003,\n'
                                               '...  0.4437117933924033,\n'
                                               '...  0.4501682807885157,\n'
                                               '...  0.44611580465691325,\n'
                                               '...  0.4321335348262124,\n'
                                               '...  0.4486880065943124,\n'
                                               '...  0.4424371479598846,\n'
                                               '...  0.43968951779090537]), atol= 0.3).all(), "The returned accuracy for NB does not meet the requirements."\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
