# testing this app? use own sample_exchange dir
# as not to spoil improtant test files
sampledir = '/Users/orion/Dev/klanten/wur/frisbe_import/sample_exchange_files/'
# sampledir = 'sample_exchange_files/'

format_data = {
    'meta_lines': [],
    'general': [
        # fieldname, begin, [until], [alignment]
        ["type", 0, 2],
        ["station", 2, 9],
        ["year", 9, 13],
        ["month", 13, 15],
        ["day", 15, 17],
        ['time', 17, 21],
    ],
    'St': [
        ['time_accuracy', 64, 73],
        ['pgm_code', 73, 81],
        ['pgm_version_number', 81, 85],
        ['platform_code', 85, 95],
        ['city_code', 95, 98],
        ['area_code', 98, 102],
        ['quarter', 102],
        ['air_temperature', 103, 108],
        ['cloud_cover', 108],
        ['salinity_factor', 109, 115],
        ['swell_direction', 115, 118],
        ['swell_height', 118, 122],
        ['tidal_phase', 122, 126],
        ['tide_direction', 126, 129],
        ['tide_speed', 129, 132],
        ['water_visibility', 132, 136],
        ['wheater_code', 136, 137],
        ['wind_direction', 138, 141],
        ['wind_force', 141, 146],
        ['distance_to_shore', 146, 154],
        ['stm_code', 154, 158, 'l'],
        ['day_night', 158],
        ['landing_year', 159, 163],
        ['landing_month', 163, 165],
        ['landing_day', 165, 167],
    ],
    'Pn': [
        ['number', 41, 64],
        ['lat_degrees', 64, 66],
        ['lat_minutes', 66, 68],
        ['lat_seconds', 68, 72],
        ['north_south', 72],
        ['lon_degrees', 73, 76],
        ['lon_minutes', 76, 78],
        ['lon_seconds', 78, 82],
        ['east_west', 82],
        ['pos_method', 83],
        ['pos_accuracy', 84, 92],
        ['pos_type', 92],
        ['depth', 93, 99]
    ],
    'Cm': [
        ['initials', 64, 67],
        ['function', 67, 97],
    ]
}
