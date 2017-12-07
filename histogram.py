#import the necessary libraries

import sys
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# define the numbers you enter

num1 = sys.argv[1]
num2 = sys.argv[2]

# connect to postgres

conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
cur = conn.cursor()

# connect to postgres

cur.execute("SELECT word, count from tweetwordcount WHERE count >= %s and count <= %s ORDER BY count desc", (num1, num2))
listofwords = cur.fetchall()
for word in listofwords:
	print word[0], word[1] 

conn.commit()
conn.close()
