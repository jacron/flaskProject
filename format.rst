FRISBE Exchange format
The Exchange format is a text format with fixed positions for all variables. The Exchange format file contains administrative information and information on the observations.

Administrative information in the Exchange file always starts with #.

- # $Ty: type of file (# $Ty: NEW)
- # $Id: information on the file, how the file was created, who has created or last updated the file, when was he file updated (# $Id: Billie 8.0 r8, rijn023, 2019-02-22 13:47:35$)
- # $Vn: version of the Exchange format (# $Vn: Exchange Format 7)
- # $Cl: lists the number of class records (# $Cl: File contains 71 class records.)
- # $NR: lists the total number of records in the file (# $NR: 86 records written.)

Observations in the Exchange file always start with:

- position 01-02: record type; all observation tables have a unique record type description
- position 03-09: station code
- position 10-13: sampling year
- position 14-15: sampling month
- position 16-17: sampling day
- position 18-21: sampling time

Positions 22-64 contain, dependent on the table, unique key information in order to relate the different record types. From position 65 onwards the data for the specific record type are added.

The full overview of the positions of the variables, the constraints (field length, field type, range, vocabulary) and units can be found in the Exchange format tables per observation table. You can find the exchange format tables on the the former documentation site.

Or shall I just add it here?

Position (Pn)

- position 42-64: number
- position 65-66: lat degrees
- position 67-68: lat minutes
- position 69-72: lat seconds
- position 73: North/South (N|S)
- position 74-76: Lon degrees
- position 77-78: Lon minutes
- position 79-82: Lon Seconds
- position 83: East/West
- position 84: Postioning method (c,d,e,g,h,l,r,t,u,D)
- position 85-92: Positioning accuracy (0,99 999 999)
- position 93: Position type
- position 94: Depth (0.8000.0)

Station (St)

- position 65-73: Time accuracy
- position 74-81: pgm_code
- position 82-85: pgm_version_number
- position 86-95: platform_code
- position 96-98: city_code
- position 99-102: area_code
- position 103: [quarter]
- position 104-108: air_temperature
- position 109: cloud_cover
- position 110-115: salinity_factor
- position 116-118: swell_direction
- position 119-122: swell_height
- position 123-126: tidal_phase
- position 127-129: tide_direction
- position 130-132: tide_speed
- position 133-136: water_visibility
- position 137-138: wheater_code
- position 139-141: wind_direction
- position 142-146: wind_force
- position 147-154: distance_to_shore
- position 155-158: stm_code
- position 159: day/night
- position 160-163: landing year
- position 164-165: landing month
- position 166-167: landing day

Crew member (Cm)

- position 65-67: initials
- position 68-97: function
