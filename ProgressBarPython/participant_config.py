# coding=utf-8


def get_type(participant, session):
    return CONFIG[participant][session]


CONFIG = {
    'p0': {
        '0': 'none',
        '-1': 'linear_continuous',
        '-2': 'circular_continuous',
        '-3': 'text_continuous',
        '-4': 'linear_intermittent',
        '-5': 'circular_intermittent',
        '-6': 'text_intermittent',

        '-7': 'linear_learning',
        '-8': 'circular_learning',

        '1': 'linear_continuous',
        '2': 'circular_continuous',
        '3': 'text_continuous',
        '4': 'linear_intermittent',
        '5': 'circular_intermittent',
        '6': 'text_intermittent',
    },

    'c115': {
        '0': 'none',
        '-4': 'linear_continuous',
        '-5': 'circular_continuous',
        '-6': 'text_continuous',
        '-1': 'linear_intermittent',
        '-2': 'circular_intermittent',
        '-3': 'text_intermittent',

        '-7': 'linear_learning',
        '-8': 'circular_learning',

        '4': 'linear_continuous',
        '5': 'circular_continuous',
        '6': 'text_continuous',
        '1': 'linear_intermittent',
        '2': 'circular_intermittent',
        '3': 'text_intermittent',
    },
    'c116': {
        '0': 'none',
        '-6': 'linear_continuous',
        '-4': 'circular_continuous',
        '-5': 'text_continuous',
        '-3': 'linear_intermittent',
        '-1': 'circular_intermittent',
        '-2': 'text_intermittent',

        '-8': 'linear_learning',
        '-7': 'circular_learning',

        '6': 'linear_continuous',
        '4': 'circular_continuous',
        '5': 'text_continuous',
        '3': 'linear_intermittent',
        '1': 'circular_intermittent',
        '2': 'text_intermittent',
    },
    'c117': {
        '0': 'none',
        '-5': 'linear_continuous',
        '-6': 'circular_continuous',
        '-4': 'text_continuous',
        '-2': 'linear_intermittent',
        '-3': 'circular_intermittent',
        '-1': 'text_intermittent',

        '-7': 'linear_learning',
        '-8': 'circular_learning',

        '5': 'linear_continuous',
        '6': 'circular_continuous',
        '4': 'text_continuous',
        '2': 'linear_intermittent',
        '3': 'circular_intermittent',
        '1': 'text_intermittent',
    },

    'c118': {
        '0': 'none',
        '-6': 'linear_continuous',
        '-5': 'circular_continuous',
        '-4': 'text_continuous',
        '-3': 'linear_intermittent',
        '-2': 'circular_intermittent',
        '-1': 'text_intermittent',

        '-7': 'linear_learning',
        '-8': 'circular_learning',

        '6': 'linear_continuous',
        '5': 'circular_continuous',
        '4': 'text_continuous',
        '3': 'linear_intermittent',
        '2': 'circular_intermittent',
        '1': 'text_intermittent',
    },
    'c119': {
        '0': 'none',
        '-4': 'linear_continuous',
        '-6': 'circular_continuous',
        '-5': 'text_continuous',
        '-1': 'linear_intermittent',
        '-3': 'circular_intermittent',
        '-2': 'text_intermittent',

        '-7': 'linear_learning',
        '-8': 'circular_learning',

        '4': 'linear_continuous',
        '6': 'circular_continuous',
        '5': 'text_continuous',
        '1': 'linear_intermittent',
        '3': 'circular_intermittent',
        '2': 'text_intermittent',
    },
    'c120': {
        '0': 'none',
        '-5': 'linear_continuous',
        '-4': 'circular_continuous',
        '-6': 'text_continuous',
        '-2': 'linear_intermittent',
        '-1': 'circular_intermittent',
        '-3': 'text_intermittent',

        '-8': 'linear_learning',
        '-7': 'circular_learning',

        '5': 'linear_continuous',
        '4': 'circular_continuous',
        '6': 'text_continuous',
        '2': 'linear_intermittent',
        '1': 'circular_intermittent',
        '3': 'text_intermittent',
    },

    'c121': {
        '0': 'none',
        '-4': 'linear_continuous',
        '-5': 'circular_continuous',
        '-6': 'text_continuous',
        '-1': 'linear_intermittent',
        '-2': 'circular_intermittent',
        '-3': 'text_intermittent',

        '-7': 'linear_learning',
        '-8': 'circular_learning',

        '4': 'linear_continuous',
        '5': 'circular_continuous',
        '6': 'text_continuous',
        '1': 'linear_intermittent',
        '2': 'circular_intermittent',
        '3': 'text_intermittent',
    },
    'c122': {
        '0': 'none',
        '-6': 'linear_continuous',
        '-4': 'circular_continuous',
        '-5': 'text_continuous',
        '-3': 'linear_intermittent',
        '-1': 'circular_intermittent',
        '-2': 'text_intermittent',

        '-8': 'linear_learning',
        '-7': 'circular_learning',

        '6': 'linear_continuous',
        '4': 'circular_continuous',
        '5': 'text_continuous',
        '3': 'linear_intermittent',
        '1': 'circular_intermittent',
        '2': 'text_intermittent',
    },
    'c123': {
        '0': 'none',
        '-5': 'linear_continuous',
        '-6': 'circular_continuous',
        '-4': 'text_continuous',
        '-2': 'linear_intermittent',
        '-3': 'circular_intermittent',
        '-1': 'text_intermittent',

        '-7': 'linear_learning',
        '-8': 'circular_learning',

        '5': 'linear_continuous',
        '6': 'circular_continuous',
        '4': 'text_continuous',
        '2': 'linear_intermittent',
        '3': 'circular_intermittent',
        '1': 'text_intermittent',
    },

    'c124': {
        '0': 'none',
        '-6': 'linear_continuous',
        '-5': 'circular_continuous',
        '-4': 'text_continuous',
        '-3': 'linear_intermittent',
        '-2': 'circular_intermittent',
        '-1': 'text_intermittent',

        '-7': 'linear_learning',
        '-8': 'circular_learning',

        '6': 'linear_continuous',
        '5': 'circular_continuous',
        '4': 'text_continuous',
        '3': 'linear_intermittent',
        '2': 'circular_intermittent',
        '1': 'text_intermittent',
    },
    'c125': {
        '0': 'none',
        '-4': 'linear_continuous',
        '-6': 'circular_continuous',
        '-5': 'text_continuous',
        '-1': 'linear_intermittent',
        '-3': 'circular_intermittent',
        '-2': 'text_intermittent',

        '-7': 'linear_learning',
        '-8': 'circular_learning',

        '4': 'linear_continuous',
        '6': 'circular_continuous',
        '5': 'text_continuous',
        '1': 'linear_intermittent',
        '3': 'circular_intermittent',
        '2': 'text_intermittent',
    },
    'c126': {
        '0': 'none',
        '-5': 'linear_continuous',
        '-4': 'circular_continuous',
        '-6': 'text_continuous',
        '-2': 'linear_intermittent',
        '-1': 'circular_intermittent',
        '-3': 'text_intermittent',

        '-8': 'linear_learning',
        '-7': 'circular_learning',

        '5': 'linear_continuous',
        '4': 'circular_continuous',
        '6': 'text_continuous',
        '2': 'linear_intermittent',
        '1': 'circular_intermittent',
        '3': 'text_intermittent',
    },

    'c127': {
        '0': 'none',
        '-4': 'linear_continuous',
        '-5': 'circular_continuous',
        '-6': 'text_continuous',
        '-1': 'linear_intermittent',
        '-2': 'circular_intermittent',
        '-3': 'text_intermittent',

        '-7': 'linear_learning',
        '-8': 'circular_learning',

        '4': 'linear_continuous',
        '5': 'circular_continuous',
        '6': 'text_continuous',
        '1': 'linear_intermittent',
        '2': 'circular_intermittent',
        '3': 'text_intermittent',
    },
    'c128': {
        '0': 'none',
        '-6': 'linear_continuous',
        '-4': 'circular_continuous',
        '-5': 'text_continuous',
        '-3': 'linear_intermittent',
        '-1': 'circular_intermittent',
        '-2': 'text_intermittent',

        '-8': 'linear_learning',
        '-7': 'circular_learning',

        '6': 'linear_continuous',
        '4': 'circular_continuous',
        '5': 'text_continuous',
        '3': 'linear_intermittent',
        '1': 'circular_intermittent',
        '2': 'text_intermittent',
    },
    'c129': {
        '0': 'none',
        '-5': 'linear_continuous',
        '-6': 'circular_continuous',
        '-4': 'text_continuous',
        '-2': 'linear_intermittent',
        '-3': 'circular_intermittent',
        '-1': 'text_intermittent',

        '-7': 'linear_learning',
        '-8': 'circular_learning',

        '5': 'linear_continuous',
        '6': 'circular_continuous',
        '4': 'text_continuous',
        '2': 'linear_intermittent',
        '3': 'circular_intermittent',
        '1': 'text_intermittent',
    },

    'c130': {
        '0': 'none',
        '-6': 'linear_continuous',
        '-5': 'circular_continuous',
        '-4': 'text_continuous',
        '-3': 'linear_intermittent',
        '-2': 'circular_intermittent',
        '-1': 'text_intermittent',

        '-7': 'linear_learning',
        '-8': 'circular_learning',

        '6': 'linear_continuous',
        '5': 'circular_continuous',
        '4': 'text_continuous',
        '3': 'linear_intermittent',
        '2': 'circular_intermittent',
        '1': 'text_intermittent',
    },
    'c131': {
        '0': 'none',
        '-4': 'linear_continuous',
        '-6': 'circular_continuous',
        '-5': 'text_continuous',
        '-1': 'linear_intermittent',
        '-3': 'circular_intermittent',
        '-2': 'text_intermittent',

        '-7': 'linear_learning',
        '-8': 'circular_learning',

        '4': 'linear_continuous',
        '6': 'circular_continuous',
        '5': 'text_continuous',
        '1': 'linear_intermittent',
        '3': 'circular_intermittent',
        '2': 'text_intermittent',
    },
    'c132': {
        '0': 'none',
        '-5': 'linear_continuous',
        '-4': 'circular_continuous',
        '-6': 'text_continuous',
        '-2': 'linear_intermittent',
        '-1': 'circular_intermittent',
        '-3': 'text_intermittent',

        '-8': 'linear_learning',
        '-7': 'circular_learning',

        '5': 'linear_continuous',
        '4': 'circular_continuous',
        '6': 'text_continuous',
        '2': 'linear_intermittent',
        '1': 'circular_intermittent',
        '3': 'text_intermittent',
    },

}
