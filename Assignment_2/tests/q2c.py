OK_FORMAT = True

test = {   'name': 'q2c',
    'points': 2,
    'suites': [   {   'cases': [   {   'code': ">>> expected = ['label', 'label_attack_type', 'index', "
                                               "'protocol_type','flag','service','is_host_login','label_encoding','count','same_srv_rate','diff_srv_rate','src_bytes','flag_SF', "
                                               "'dst_host_same_srv_rate','dst_host_srv_count','dst_bytes','dst_host_srv_serror_rate','dst_host_diff_srv_rate','dst_host_serror_rate','srv_serror_rate','flag_S0','serror_rate','logged_in','dst_host_same_src_port_rate','dst_host_count']\n"
                                               '>>> assert X_train.columns.all() not in set(expected)\n'
                                               '>>> \n',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> expected = ['label', 'label_attack_type', 'index', "
                                               "'protocol_type','flag','service','is_host_login','label_encoding','count','same_srv_rate','diff_srv_rate','src_bytes','flag_SF', "
                                               "'dst_host_same_srv_rate','dst_host_srv_count','dst_bytes','dst_host_srv_serror_rate','dst_host_diff_srv_rate','dst_host_serror_rate','srv_serror_rate','flag_S0','serror_rate','logged_in','dst_host_same_src_port_rate','dst_host_count']\n"
                                               '>>> assert X_test.columns.all() not in set(expected)\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
