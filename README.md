## Unit Conversion API

Description:
```
Unit Conversion API convert a value from one unit to another unit, depending on region and user preferences. For example, a user in Thailand may prefer the area unit to be in 'Rai' (ไร่), but a user in the Philippines would prefer it to be in 'Square Meter'
Example: 2 Rai convert to 3200 Square Meter
```
How it work
```
# APIs that handle CRUD of maintaining units.
Database store parameters ​​such as name and type, where name is the name of the unit and type is the region to use.
# APIs that handle CRUD of maintaining conversion formula between 2 units.
Where unit1 is stored as unit2 and ratio, which is the ratio of unit1 to unit2.
# API to convert a value from one unit to another.
Take the values ​​obtained from both units and convert the values ​​from one unit to another by Using the unit name for both unit1 and the value from unit1, and select unit2 as the destination unit to convert.
```

Run API:
```
python convertapi.py
```

Test:
```
pytest test_api.py
```