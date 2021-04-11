sampledir = '/Users/orion/Dev/klanten/wur/frisbe_import/sample_exchange_files/'
# sampledir = 'sample_exchange_files/'
# sampledir = '/Volumes/frisbep/ont/import'

cookie_path_name = 'exchange_path'
meta_lines = []


def clear_meta_lines():
    global meta_lines
    meta_lines = []


format_data = {
    'general': [
        {
            "field": "type",
            "begin": 0,
            "until": 2,
            "nullable": False,
        },
        {
            "field": "station",
            "begin": 2,
            "until": 9,
            "nullable": False,
        },
        {
            "composite": {
                "label": "date",
                "nullable": False,
                "fields": [
                    {
                        "field": "year",
                        "begin": 9,
                        "until": 13,
                        "nullable": False,
                    },
                    {
                        "field": "month",
                        "begin": 13,
                        "until": 15,
                        "nullable": False,
                    },
                    {
                        "field": "day",
                        "begin": 15,
                        "until": 17,
                        "nullable": False,
                    },
                ]
            }
        },
        {
            "field": "time",
            "begin": 17,
            "until": 21,
            "dtformat": "%H%M",
            "nullable": False,
        },
    ],
    'St': [
        {
            "field": "time_accuracy",
            "begin": 64,
            "until": 73,
        },
        {
            "composite": {
                "label": "program",
                "nullable": False,
                "fields": [
                    {
                        "field": "pgm_code",  # program
                        "begin": 73,
                        "until": 81,
                        "nullable": False
                    },
                    {
                        "field": "pgm_version_number",  # program_version
                        "begin": 81,
                        "until": 85,
                        "min": -9.9,
                        "max": 99.9,
                        "nullable": False
                    },
                ]
            }
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
            "until": 108,
            "min": -99.9,
            "max": 99.9,
        },
        {
            "field": "cloud_cover",
            "begin": 108,
            "min": 0,
            "max": 8,
        },
        {
            "field": "salinity_factor",
            "begin": 109,
            "until": 115,
        },
        {
            "field": "swell_direction",
            "begin": 115,
            "until": 118,
        },
        {
            "field": "swell_height",
            "begin": 118,
            "until": 122,
            "min": 0.0,
            "max": 30.9,
        },
        {
            "composite": {
                "label": "tide",
                "fields": [
                    {
                        "field": "tidal_phase",
                        "begin": 122,
                        "until": 126,
                        "min": 0.0,
                        "max": 12.9,
                        "min_inclusive": True,
                        "max_inclusive": True,
                    },
                    {
                        "field": "tide_direction",
                        "begin": 126,
                        "until": 129,
                    },
                    {
                        "field": "tide_speed",
                        "begin": 129,
                        "until": 132,
                        "min": 0.0,
                        "max": 12.9,
                    },
                ]
            }
        },
        {
            "field": "water_visibility",
            "begin": 132,
            "until": 136,
            "min": 0.0,
            "max": 99.9,
        },
        {
            "field": "wheater_code",
            "begin": 136,
            "until": 137,
            "min": 0,
            "max": 99,
        },
        {
            "composite": {
                "label": "wind",
                "fields": [
                    {
                        "field": "wind_direction",
                        "begin": 138,
                        "until": 141,
                        "min": 0,
                        "max": 359,
                    },
                    {
                        "field": "wind_force",
                        "begin": 141,
                        "until": 146,
                        "min": 0.0,
                        "max": 199.9,
                    },
                ]
            }
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
            "domain": [
                "n", "d", "u", "x"
            ]
        },
        {
            "composite": {
                "label": "landing",
                "nullable": True,
                "fields": [
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
                ]
            }
        }
    ],
    'Pn': [
        {
            "field": "number",  # seq_no
            "begin": 41,
            "until": 64,
            "min": 0,
            "max": 999,
            "nullable": False
        },
        {
            "composite": {
                "label": "latitude",
                "fields": [
                    {
                        "field": "lat_degrees",
                        "begin": 64,
                        "until": 66,
                    },
                    {
                        "field": "lat_minutes",
                        "begin": 66,
                        "until": 68,
                    },
                    {
                        "field": "lat_seconds",
                        "begin": 68,
                        "until": 72,
                    },
                ]
            }
        },
        {
            "field": "north_south",
            "begin": 72,
        },
        {
            "composite": {
                "label": "longitude",
                "fields": [
                    {
                        "field": "lon_degrees",
                        "begin": 73,
                        "until": 76,
                    },
                    {
                        "field": "lon_minutes",
                        "begin": 76,
                        "until": 78,
                    },
                    {
                        "field": "lon_seconds",
                        "begin": 78,
                        "until": 82,
                    },
                ]
            }
        },
        {
            "field": "east_west",
            "begin": 82,
        },
        {
            "composite": {
                "label": "pos",
                "fields": [
                    {
                        "field": "pos_method",
                        "begin": 83,
                    },
                    {
                        "field": "pos_accuracy",
                        "begin": 84,
                        "until": 92,
                    },
                    {
                        "field": "pos_type",
                        "begin": 92,
                    },
                ]
            }
        },
        {
            "field": "depth",
            "begin": 93,
            "until": 99,
        },
    ],
    'Cm': [
        {
            "field": "initials",
            "begin": 64,
            "until": 67,
            "nullable": False
        },
        {
            "field": "function",
            "begin": 67,
            "until": 97,
            "nullable": False
        },
    ]
}
