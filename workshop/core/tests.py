from django.test import TestCase

# Create your tests here.

# Um teste
d = {'members': [
    {'id': 1, 'email_address': 'um', 'timestamp_opt': '2019-01-21 12:13:14'},
    {'id': 2, 'email_address': 'dois', 'timestamp_opt': '2019-01-21 12:15:14'},
    {'id': 3, 'email_address': 'um', 'timestamp_opt': '2019-01-21 12:15:22'},
    {'id': 4, 'email_address': 'quatro', 'timestamp_opt': '2019-01-22 12:13:14'},
    {'id': 5, 'email_address': 'dois', 'timestamp_opt': '2019-01-21 12:15:34'},
    {'id': 6, 'email_address': 'um', 'timestamp_opt': '2019-01-24 12:15:22'},
    {'id': 7, 'email_address': 'quatro', 'timestamp_opt': '2019-01-25 12:15:14'},
    {'id': 8, 'email_address': 'dois', 'timestamp_opt': '2019-01-28 13:15:34'},
]
}
d_r = {'result': [
    {'id': 1, 'email_address': 'um', 'timestamp_opt': '2019-01-21 12:13:14'},
    {'id': 2, 'email_address': 'dois', 'timestamp_opt': '2019-01-21 12:15:14'},
    {'id': 3, 'email_address': 'um', 'timestamp_opt': '2019-01-21 12:15:22 PAR'},
    {'id': 4, 'email_address': 'quatro', 'timestamp_opt': '2019-01-22 12:13:14'},
    {'id': 5, 'email_address': 'dois', 'timestamp_opt': '2019-01-21 12:15:34 PAR'},
    {'id': 6, 'email_address': 'um', 'timestamp_opt': '2019-01-24 12:15:22 PAR'},
    {'id': 7, 'email_address': 'quatro', 'timestamp_opt': '2019-01-25 12:15:14 PAR'},
    {'id': 8, 'email_address': 'dois', 'timestamp_opt': '2019-01-28 13:15:34 PAR'}
]
}


class CheckDoubleTest(TestCase):
    def test_double(self):
        # Check double
        user_list = [i['email_address'] for i in d['members']]
        # conjunto de membros repetidos
        d_member = set(i for i in user_list if user_list.count(i) > 1)

        for i in d_member:
            count = 0

            for u in d['members']:
                match_user = u['email_address'] == i

                if count > 0 and match_user:
                    u['timestamp_opt'] += ' PAR'

                if match_user:
                    count += 1

        self.assertEqual(d['members'], d_r['result'])
