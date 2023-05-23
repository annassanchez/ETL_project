import calendar

dict_month = dict(zip(list(calendar.month_name)[1:], list(range(1,13))))

dict_keys = {
    0: 'C',
    1: 'C♯, D♭',
    2: 'D',
    3: 'D♯, E♭',
    4: 'E',
    5: 'F',
    6: 'F♯, G♭',
    7: 'G',
    8: 'G♯, A♭',
    9: 'A',
    10: 'A♯, B♭',
    11: 'B'
}

dict_scale = {
    1: 'Major',
    0: 'Minor',
}

dict_gender = {
    'male': [' his '],
    #'group': ['duo', 'septet', 'trio', 'collective', 'quintet', 'quartet', 'septet', 'its', ' group ', ' band ', '-group', ' members ', ' brothers ', ' duo ', ' trio ', ' collective ', ' group,', ' quartet ', ' superduo ', ' band,', ' quintet '],
    'female': [' she ', ' her ', 'actress', ' she is '],
    'male': [' him ', ' he ', ' his '],
    'group': ['duo', 'septet', 'trio', 'collective', 'quintet', 'quartet', 'septet', 'its', ' group ', ' band ', '-group', ' members ', ' brothers ', ' duo ', ' trio ', ' collective ', ' group,', ' quartet ', ' superduo ', ' band,', ' quintet '],
    'non-binary': [' they ', ' them ', ' their '],
}