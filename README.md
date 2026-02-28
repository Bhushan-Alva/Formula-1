# Formula 1 data analysis

This dataset contains data from 1950 all the way through the 2025 season, and consists of tables describing constructors, race drivers, lap times, pit stops and more.

The data to 2024 is downloaded from [http://ergast.com/mrd/](http://ergast.com/mrd/) which was gathered and published to the public domain by Chris Newell. From 2025 the data is refreshed after each Grand Prix weekend using the new Ergast compatible API provided by [api.jolpi.ca](http://api.jolpi.ca/ergast/f1/).

# Dataset details

- Files Used
    - circuits.csv
    - constructor_results.csv
    - constructor_standings.csv
    - constructors.csv
    - driver_standings.csv
    - drivers.csv
    - lap_times.csv
    - pit_stops.csv
    - qualifying.csv
    - races.csv
    - results.csv
    - seasons.csv
    - sprint_results.csv
    - status.csv
- Changes made to the original dataset
    
    Manually added data to results table for raceId 1167
    
    - **circuits**
        - No Change needed
    - **constructor_results**
    - **constructor_standings**
    - **constructors**
        - No Change needed
    - **driver_standings**
    - **drivers**
        - replace “\N” in *number, code* to nan
        - convert *number*  to float
        - convert *dob* to datetime
    - **lap_times**
    - **pit_stops**
    - **qualifying**
    - **races**
        - replace “\N” from columns *time, fp1_date, fp1_time, fp2_date, fp2_time, fp3_date, fp3_time, quali_date, quali_time, sprint_date, sprint_time* to nan
        - convert *date, fp1_date, fp2_date, fp3_date, quali_date, sprint_date* to datetime
        - convert *time, fp1_time, fp2_time, fp3_time, quali_time, sprint_time* to time
        - combine date and time columns to get datetime columns and drop individual columns
    - **results**
        - replace “\N” from columns *grid, position, time, milliseconds, fastestLap, rank, fastestLapTime, fastestLapSpeed* tp nan
    - **seasons**
    - **sprint_results**
    - **status**
- Dimension Tables
    - circuits
        
        Each circuit listed in the file is identified by a unique circuitId which is used to identify the circuit throughout the dataset.
        
        | **sl.no.** | **Columns** | **Details** | **Has null?** | **Is unique?** | **Data Type** |
        | --- | --- | --- | --- | --- | --- |
        | 1 | circuitId | unique numeric id | no | yes | int64 |
        | 2 | circuitRef | unique reference code | no | yes | object |
        | 3 | name | name of the circuit | no | yes | object |
        | 4 | location | city of the circuit | no | no | object |
        | 5 | country | country of the circuit | no | no | object |
        | 6 | lat | latitudinal position of the circuit | no | yes | float64 |
        | 7 | lng | longitudinal position of the circuit | no | yes | float64 |
        | 8 | alt |  | no | no | int64 |
        | 9 | url | wikipedia link to the circuit | no | yes | object |
    - constructors
        
        Each constructor listed in the dataset is identified by a unique constructorId which is used to identify the constructor throughout the dataset.
        
        | **sl.no.** | **Columns** | **Details** | **Has null?** | **Is unique?** | **Data Type** |
        | --- | --- | --- | --- | --- | --- |
        | 1 | constructorId | unique numeric id | no | yes | int64 |
        | 2 | constructorRef | unique reference code | no | yes | object |
        | 3 | name | name of the construtor | no | yes | object |
        | 4 | nationality | nationality of the constructor | no | no | object |
        | 5 | url | wikipedia link to the constructor | no | no | object |
    - drivers
        
        Each driver listed in the dataset is identified by a unique driverId which is used to identify the driver throughout the dataset.
        
        | **sl.no.** | **Columns** | **Details** | **Has null?** | **Is unique?** | **Data Type** |
        | --- | --- | --- | --- | --- | --- |
        | 1 | **driverId** | unique numeric id | no | yes | int64 |
        | 2 | **driverRef** | unique reference code | no | yes | object |
        | 3 | **number** | number representing the driver | yes | no | float64 |
        | 4 | **code** | 3 letter code of the driver | yes | no | object |
        | 5 | **forename** | firstname of the driver | no | no | object |
        | 6 | **surname** | lastname of the driver | no | no | object |
        | 7 | **dob** | date of birth of the driver | no | no | datetime64 |
        | 8 | **nationality** | nationality of the driver | no | no | object |
        | 9 | url | wikipedia link to the driver | no | yes | object |
    - status
        
        Final driver status at the end of the race
        
        | **sl.no.** | **Columns** | **Details** | **Has null?** | **Is unique?** | **Data Type** |
        | --- | --- | --- | --- | --- | --- |
        | 1 | **statusId** | unique numeric id | no | yes | int64 |
        | 2 | **status** | driver position at the end of the race | no | yes | object |
    - seasons
        
        The table consists of all the seasons of formula 1
        
        | **sl.no.** | **Columns** | **Details** | **Has null?** | **Is unique?** | **Data Type** |
        | --- | --- | --- | --- | --- | --- |
        | 1 | year | f1 season | no | yes | int64 |
        | 2 | url | wikipedia link to the f1 season | no | yes | object |
- Fact Tables
    - results
        
        
        | **sl.no.** | **Columns** | **Details** | **Has null?** | **Is unique?** | **Data Type** |
        | --- | --- | --- | --- | --- | --- |
        | 1 | resultId | unique numeric id | no | yes | int64 |
        | 2 | raceId | references raceId from the races table | no | no | int64 |
        | 3 | driverId | references driverId from the drivers table | no | no | int64 |
        | 4 | constructorId | references constructorId from the constructors table | no | no | int64 |
        | 5 | number | driver number | yes | no | int64 |
        | 6 | grid | grid position at the start of the race | no | no | int64 |
        | 7 | position | position of the driver when race is completed | yes | no | int64 |
        | 8 | positionText | position of the driver when race is completed (contains text if retired or any other incident) | no | no | category |
        | 9 | positionOrder | position of the driver when race is completed even if race is not completed | no | no | int64 |
        | 10 | points | points scored by the driver at the end of the race | no | no | float64 |
        | 11 | laps | total laps done by driver at the end of the race | no | no | int64 |
        | 12 | time | time taken to complete the race. The 2nd position and below is represent by 1st position + timedelta | yes | no | object |
        | 13 | milliseconds | total time taken to complete the race in milliseconds | yes | no | int64 |
        | 14 | fastestLap | lap number when it was fastest lap | yes | no | int64 |
        | 15 | rank | rank for the fastest lap | yes | no | int64 |
        | 16 | fastestLapTime | fastest time taken by driver to complete a lap in a race | yes | no | timedelta64 |
        | 17 | fastestLapSpeed | speed of the driver to complete fastest lap in a race | yes | no | float64 |
        | 18 | statusId | references statusId from the status table | no | no | int64 |
    - races
        
        Contains the details like date, time and location of the races
        
        | **sl.no.** | **Columns** | **Details** | **Has null?** | **Is unique?** | **Data Type** | **Comment** |
        | --- | --- | --- | --- | --- | --- | --- |
        | 1 | raceId | unique numeric id | no | yes | int64 |  |
        | 2 | year | year of the race | no | no | int64 |  |
        | 3 | round | race number of the season | no | no | int64 |  |
        | 4 | circuitId | references circuitId from the circuits table | no | no | int64 |  |
        | 5 | name | name of the race | no | no | object |  |
        | 6 | date | date of the race | no | yes | datetime64 | this and below column is combined to form single column race_datetime |
        | 7 | time | starttime of the race | yes | no | object |  |
        | 8 | url | wikipedia link to the race page | no | yes | object |  |
        | 9 | fp1_date | free practice 1 date | yes | no | datetime64 | this and below column is combined to form single column fp1_datetime |
        | 10 | fp1_time | free practice 1 starttime | yes | no | object |  |
        | 11 | fp2_date | free practice 2 date | yes | no | datetime64 | this and below column is combined to form single column fp2_datetime |
        | 12 | fp2_time | free practice 2 starttime | yes | no | object |  |
        | 13 | fp3_date | free practice 3 date | yes | no | datetime64 | this and below column is combined to form single column fp3_datetime |
        | 14 | fp3_time | free practice 3 starttime | yes | no | object |  |
        | 15 | quali_date | qualification date | yes | no | datetime64 | this and below column is combined to form single column quali_datetime |
        | 16 | quali_time | qualification starttime | yes | no | object |  |
        | 17 | sprint_date | sprint date | yes | no | datetime64 | this and below column is combined to form single column sprint_datetime |
        | 18 | sprint_time | sprint starttime | yes | no | object |  |