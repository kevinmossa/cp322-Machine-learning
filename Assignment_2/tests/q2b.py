OK_FORMAT = True

test = {   'name': 'q2b',
    'points': 4,
    'suites': [   {   'cases': [   {   'code': ">>> assert protocol_encoding_test.columns.all() in set(['protocol_icmp', 'protocol_tcp', 'protocol_udp'])\n"
                                               ">>> assert flag_encoding_test.columns.all() in set(['flag_OTH', 'flag_REJ', 'flag_RSTO', 'flag_RSTOS0', 'flag_RSTR', 'flag_S0', 'flag_S1', 'flag_S2', "
                                               "'flag_S3', 'flag_SF', 'flag_SH'])\n"
                                               '>>> assert test_data.shape == (77291, 58)\n',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> assert flag_encoding_train.columns.all() in set(['flag_OTH', 'flag_REJ', 'flag_RSTO', 'flag_RSTOS0', 'flag_RSTR', 'flag_S0', 'flag_S1', 'flag_S2', "
                                               '\'flag_S3\', \'flag_SF\', \'flag_SH\']), "The encoding labels not created correctly"\n'
                                               ">>> assert protocol_encoding_train.columns.all() in set(['protocol_icmp', 'protocol_tcp', 'protocol_udp'])\n"
                                               '>>> assert train_data.shape == (145586, 58)\n'
                                               '>>> \n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
