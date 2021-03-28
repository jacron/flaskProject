FRISBE Exchange format
The Exchange format is a text format with fixed positions for all variables. The Exchange format file contains administrative information and information on the observations.

Administrative information in the Exchange file always starts with #. # $Ty: type of file (# $Ty: NEW) # $Id: information on the file, how the file was created, who has created or last updated the file, when was he file updated (# $Id: Billie 8.0 r8, rijn023, 2019-02-22 13:47:35$) # $Vn: version of the Exchange format (# $Vn: Exchange Format 7) # $Cl: lists the number of class records (# $Cl: File contains 71 class records.) # $NR: lists the total number of records in the file (# $NR: 86 records written.)

Observations in the Exchange file always start with:

position 01-02: record type; all observation tables have a unique record type description
position 03-09: station code
position 10-13: sampling year
position 14-15: sampling month
position 16-17: sampling day
position 18-21: sampling time
Positions 22-64 contain, dependent on the table, unique key information in order to relate the different record types. From position 65 onwards the data for the specific record type are added.

The full overview of the positions of the variables, the constraints (field length, field type, range, vocabulary) and units can be found in the Exchange format tables per observation table. You can find the exchange format tables on the the former documentation site.