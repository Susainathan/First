import sqlite3

con=sqlite3.connect("datatwo.db")
print("database created")

con.execute("create table user(ID integer primary key autoincrement,Name text not null,Last_Name text not null,DOB integer not null,Username varchar(40) not null,Password varchar(20) not null)")
print("table created...")
