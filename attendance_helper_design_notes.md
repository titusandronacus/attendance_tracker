

# design doc for attendance helper

I need a small program that can help me take attandance for each class and be able to produce attandance information for certain times of the year. 

- not have to cross reference with roster in a different place either when taking attandance or seeing if someone has been showing up when I need to look at it.
- not have to deal with different naming conventions depending on the format of the class (zoom make it a little easier, but then I have the whole name which I sometimes abbrivate, sometimes not vs in seat)
- i hate spreadsheets
- future case: optoins to get up-to-date attending/not attending/ last seen, etc.
- atm fine with cli

### first part: get full roster loaded up without hitting web each and every time
This is the inital setup for a semester. it should contain a way to separate different classes, different students

keyed by:
- semester
- class
- section

simple is better: upload file once keyed, then store as file

#### details for part 1
- dictionary of tuples to handle keyed info

### second part: get attandance on a day

If i fire up the program, select that i'm taking attendance, it should read the current date, add that to the attendance data, then allow me to start typing in names. 

Maybe have an option to type in names or go through roster and say if they're here or not.