"""Write a wrapper class TableData for database table, that when
initialized with database name and table acts as collection object
 (implements Collection protocol). Assume all data has unique values
  in 'name' column. So, if presidents =
  TableData(database_name='example.sqlite', table_name='presidents')

then
len(presidents) will give current amount of rows in presidents
table in database presidents['Yeltsin'] should return single
 data row for president with name Yeltsin
'Yeltsin' in presidents should return if president with same
name exists in table object implements iteration protocol.
 i.e. you could use it in for loops:: for president in presidents:
print(president['name'])
all above mentioned calls should reflect most recent data.
If data in table changed after you created collection instance,
your calls should return updated data. Avoid reading entire table
into memory. When iterating through records, start reading the
first record, then go to the next one, until records are exhausted.
When writing tests, it's not always neccessary to mock database calls
completely. Use supplied example.sqlite file as database fixture file.
 """
import sqlite3


class TableData:
    """Connect to database and adapt it to python syntax. Provide to
    use db's tables as iterable obj, check their len, find value
    in primary key column, check value in table.
    Args:
        database_name: path to database
        table_name: primary key column

    """

    def __init__(self, database_name: str, table_name: str):
        self.database_name = database_name
        self.table_name = table_name

    def connect_to_table(self):
        self.conn = sqlite3.connect(self.database_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute("SELECT * from %s" % self.table_name)

    def __iter__(self):
        return TableDataIter(self.database_name, self.table_name)

    def __len__(self):
        self.connect_to_table()
        self.len = len(self.cursor.fetchall())
        self.conn.close()
        return self.len

    def __getitem__(self, item):
        if not isinstance(item, str):
            raise TypeError("Key must be str")
        self.connect_to_table()
        self.cursor.execute('SELECT * from presidents WHERE name = "%s"' % item)
        president = self.cursor.fetchone()
        self.conn.close()
        if president:
            return president
        raise KeyError("There is no such president")

    def __contains__(self, item):
        self.connect_to_table()
        self.cursor.execute('SELECT * from presidents WHERE name = "%s"' % item)
        president = self.cursor.fetchone()
        self.conn.close()
        if president:
            return True
        return False


class TableDataIter(TableData):
    def __init__(self, database_name: str, table_name: str):
        super().__init__(database_name, table_name)
        super().connect_to_table()

    def __iter__(self):
        return self

    def __next__(self):
        row = self.cursor.fetchone()
        if row is not None:
            return row
        self.conn.close()
        raise StopIteration
