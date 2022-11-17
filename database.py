#%%
import psycopg2
from config import database_config


def create_table():
	""" create tables in the PostgreSQL database"""
	sql = """
		CREATE TABLE ads (
			id SERIAL PRIMARY KEY,
			description  VARCHAR(500),
			email VARCHAR(50),
			state INTEGER,
			category VARCHAR(50)
		)
		"""
	conn = None
	try:
		# connect to the PostgreSQL server
		conn = psycopg2.connect(host = database_config["host"], port = database_config["port"], user = database_config["user"], password = database_config["password"], database = database_config["database"])
		cur = conn.cursor()
		# create table one by one
		cur.execute(sql)
		# close communication with the PostgreSQL database server
		cur.close()
		# commit the changes
		conn.commit()
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	finally:
		if conn is not None:
			conn.close()
# create_table()
#%%

def drop_table():
    try:
        # connect to the PostgreSQL server
        conn = psycopg2.connect(host = database_config["host"], port = database_config["port"], user = database_config["user"], password = database_config["password"], database = database_config["database"])
        cur = conn.cursor()
        # create table one by one
        cur.execute("DROP TABLE student;")
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
# drop_table()
#%%   

def truncate_table():
    try:
        # connect to the PostgreSQL server
        conn = psycopg2.connect(host = database_config["host"], port = database_config["port"], user = database_config["user"], password = database_config["password"], database = database_config["database"])
        cur = conn.cursor()
        # create table one by one
        cur.execute("TRUNCATE TABLE ads;")
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
# truncate_table()
#%%
def select_table():
    conn = psycopg2.connect(host = database_config["host"], port = database_config["port"], user = database_config["user"], password = database_config["password"], database = database_config["database"])
    cursor  =  conn.cursor()
    sql   =  "select * from ads"
    cursor.execute(sql)
    result = cursor.fetchone()
    conn.commit()
    conn.close()
    return result
# ads = select_table()

#%%

def insert_todb(tuple_input):
    try:
        conn = psycopg2.connect(host = database_config["host"], port = database_config["port"], user = database_config["user"], password = database_config["password"], database = database_config["database"])
        cursor  =  conn.cursor()
        postgres_insert_query = """ INSERT INTO ads (id, description, email, state, category) VALUES (%s,%s,%s,%s,%s)"""
        # tuple_input = (1, 'One Plus 6',"HI.com", 0, "")
        cursor.execute(postgres_insert_query, tuple_input)
        conn.commit()
    except (Exception, psycopg2.Error) as error:
        print("Failed to insert record into ads table", error)

    finally:
        # closing database connection.
        if conn:
            cursor.close()
            conn.close()
            print("PostgreSQL connection is closed")
# insert_todb("")

#%%
def update_row(tuple_input):
    
    try:
        conn = psycopg2.connect(host = database_config["host"], port = database_config["port"], user = database_config["user"], password = database_config["password"], database = database_config["database"])
        cursor  =  conn.cursor()
        postgres_insert_query = """ update ads set category = %s, state = %s where id = %s """
        cursor.execute(postgres_insert_query, tuple_input)
        conn.commit()
    except (Exception, psycopg2.Error) as error:
        print("Failed to update ads table", error)

    finally:
        # closing database connection.
        if conn:
            cursor.close()
            conn.close()
            print("PostgreSQL connection is closed")
# update_row((None, 1, 1)) 

#%%
def get_last_id():
    conn = psycopg2.connect(host = database_config["host"], port = database_config["port"], user = database_config["user"], password = database_config["password"], database = database_config["database"])
    cursor  =  conn.cursor()
    sql   =  "select MAX(id) from ads"
    cursor.execute(sql)
    result = cursor.fetchone()
    conn.commit()
    conn.close()
    return result
# last_id = get_last_id()