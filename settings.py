# testing this app? use own sample_exchange dir
# as not to spoil improtant test files
sampledir = '/Users/orion/Dev/klanten/wur/frisbe_import/sample_exchange_files/'
# sampledir = 'sample_exchange_files/'

format_data = {
    'meta_lines': [],
    'general': [
        # fieldname, begin, [until], [alignment]
        {
            "field": "type",
            "begin": 0,
            "until": 2
        },
        {
            "field": "station",
            "begin": 2,
            "until": 9
        },
        {
            "field": "year",
            "begin": 9,
            "until": 13
        },
        {
            "field": "month",
            "begin": 13,
            "until": 15
        },
        {
            "field": "day",
            "begin": 15,
            "until": 17
        },
        {
            "field": "time",
            "begin": 17,
            "until": 21
        },
    ],
    'St': [
        {
            "field": "time_accuracy",
            "begin": 64,
            "until": 73
        },
        {
            "field": "pgm_code",
            "begin": 73,
            "until": 81
        },
        {
            "field": "pgm_version_number",
            "begin": 81,
            "until": 85
        },
        {
            "field": "platform_code",
            "begin": 85,
            "until": 95
        },
        {
            "field": "city_code",
            "begin": 95,
            "until": 98
        },
        {
            "field": "area_code",
            "begin": 98,
            "until": 102
        },
        {
            "field": "quarter",
            "begin": 102
        },
        {
            "field": "air_temperature",
            "begin": 103,
            "until": 108
        },
        {
            "field": "cloud_cover",
            "begin": 108,
        },
        {
            "field": "salinity_factor",
            "begin": 109,
            "until": 115
        },

        {
            "field": "swell_direction",
            "begin": 115,
            "until": 118
        },
        {
            "field": "swell_height",
            "begin": 118,
            "until": 122
        },
        {
            "field": "tidal_phase",
            "begin": 122,
            "until": 126
        },
        {
            "field": "tide_direction",
            "begin": 126,
            "until": 129
        },
        {
            "field": "tide_speed",
            "begin": 129,
            "until": 132
        },

        {
            "field": "water_visibility",
            "begin": 132,
            "until": 136
        },
        {
            "field": "wheater_code",
            "begin": 136,
            "until": 137
        },
        {
            "field": "wind_direction",
            "begin": 138,
            "until": 141
        },
        {
            "field": "wind_force",
            "begin": 141,
            "until": 146
        },
        {
            "field": "distance_to_shore",
            "begin": 146,
            "until": 154
        },

        {
            "field": "stm_code",
            "begin": 154,
            "until": 158,
            "alignment": "l"
        },
        {
            "field": "day_night",
            "begin": 158,
        },
        {
            "field": "landing_year",
            "begin": 159,
            "until": 163
        },
        {
            "field": "landing_month",
            "begin": 163,
            "until": 165
        },
        {
            "field": "landing_day",
            "begin": 165,
            "until": 167
        },
    ],
    'Pn': [
        {
            "field": "number",
            "begin": 41,
            "until": 64
        },
        {
            "field": "lat_degrees",
            "begin": 64,
            "until": 66
        },
        {
            "field": "lat_minutes",
            "begin": 66,
            "until": 68
        },
        {
            "field": "lat_seconds",
            "begin": 68,
            "until": 72
        },

        {
            "field": "north_south",
            "begin": 72,
        },

        {
            "field": "lon_degrees",
            "begin": 73,
            "until": 76
        },
        {
            "field": "lon_minutes",
            "begin": 76,
            "until": 78
        },
        {
            "field": "lon_seconds",
            "begin": 78,
            "until": 82
        },
        {
            "field": "east_west",
            "begin": 82,
        },
        {
            "field": "pos_method",
            "begin": 83,
        },

        {
            "field": "pos_accuracy",
            "begin": 84,
            "until": 92
        },
        {
            "field": "pos_type",
            "begin": 92,
        },
        {
            "field": "depth",
            "begin": 93,
            "until": 99
        },
    ],
    'Cm': [
        {
            "field": "initials",
            "begin": 64,
            "until": 67
        },
        {
            "field": "function",
            "begin": 67,
            "until": 97
        },
    ]
}
