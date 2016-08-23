u.data contains 100,000 records about movie ratings n the format (userID, movieID, rating, timestamp).
The ratings can range from 1 to 5.

This Python MRJob prints the number of occurrences of each type of ratings.


How to RUN the python script:

!python ratingcounter.py u.data > result.txt
