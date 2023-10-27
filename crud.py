import MySQLdb

host = "localhost"
user = "root"
password = ""
db = "bd_espaco"
port = 3306

con = MySQLdb.connect(host, user, password, db, port)
c = con.cursor(MySQLdb.cursors.DictCursor)

def select(fields):
	global c
	query = "SELECT " + fields + " FROM tb_usuario"
	c.execute(query)
	return c.fetchall()

def insert(values):
	global c, con
	query = "INSERT INTO tb_usuario"
	query = query + " VALUES " + ",".join(["(" + v + ")" for v in values])
	c.execute(query)
	con.commit()

def update(sets, where=None):
	global c, con
	query = "UPDATE tb_usuario"
	query = query + " SET "+",".join([field + " = '"+value+"'" for field, value in sets.items()])
	query = query + " WHERE usu_id = " + where
	c.execute(query)
	con.commit()

def delete(where):
	global c,con
	query = "DELETE FROM tb_usuario"
	query = query + " WHERE usu_id = " + where
	c.execute(query)
	con.commit()