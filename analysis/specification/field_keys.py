def field_keys(field):
    return [
        'count',
        field + '_delta_avg',
        field + '_delta_avg_abs',
        field + '_delta_std_dev',
    ]


def map_keys(field):
    return [
        field + '_delta_avg_ad',
        field + '_delta_abs_avg_ad',
        field + '_delta_std_dev_ad'
    ]
