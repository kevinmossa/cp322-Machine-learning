OK_FORMAT = True

test = {   'name': 'q1d',
    'points': 4,
    'suites': [   {   'cases': [   {   'code': ">>> assert train_data['label_attack_type'].value_counts()['normal'] == 87814\n"
                                               ">>> assert train_data['label_attack_type'].value_counts()['dos'] == 54572\n"
                                               ">>> assert train_data['label_attack_type'].value_counts()['probes'] == 2131\n"
                                               ">>> assert train_data['label_attack_type'].value_counts()['rtl'] == 991\n"
                                               ">>> assert train_data['label_attack_type'].value_counts()['utr'] == 52\n"
                                               ">>> assert train_data['label_attack_type'].value_counts()['others'] == 26\n",
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> assert test_data['label_attack_type'].value_counts()['normal'] == 47913\n"
                                               ">>> assert test_data['label_attack_type'].value_counts()['dos'] == 21720\n"
                                               ">>> assert test_data['label_attack_type'].value_counts()['probes'] == 1269\n"
                                               ">>> assert test_data['label_attack_type'].value_counts()['rtl'] == 2325\n"
                                               ">>> assert test_data['label_attack_type'].value_counts()['utr'] == 39\n"
                                               ">>> assert test_data['label_attack_type'].value_counts()['others'] == 4025\n",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
