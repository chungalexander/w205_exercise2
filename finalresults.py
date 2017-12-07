#import necessary libraries

import sys
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


#connect to postgres

conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
cur = conn.cursor()

#first scenario - with word in command line

if len(sys.argv) == 2:
    word = sys.argv[1]
    cur.execute("SELECT count from tweetwordcount WHERE word = %s", (word, ))
    result = cur.fetchone()
    print word, str(result[0])

#second scenario - no words just list the words and their counts

if len(sys.argv) == 1:
    cur.execute("SELECT word, count from tweetwordcount ORDER BY count DESC")
    records = cur.fetchall()
    print records

else:
    print "Something went wrong. Try again please."

conn.commit()
conn.close()
