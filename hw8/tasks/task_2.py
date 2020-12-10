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
from typing import Callable


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
        self.conn: sqlite3.Connection
        self.cursor: sqlite3.Cursor

    def connect_to_table(func: Callable) -> Callable:  # type:ignore
        def inner(self, *args):
            self.conn = sqlite3.connect(self.database_name)
            self.cursor = self.conn.cursor()
            self.cursor.execute("SELECT * from %s" % self.table_name)
            return func(self, *args)

        return inner

    @connect_to_table
    def __iter__(self):
        row = self.cursor.fetchone()
        while row is not None:
            yield row
            row = self.cursor.fetchone()
        self.conn.close()

    @connect_to_table
    def __len__(self) -> int:
        count = 0
        for _ in self:
            count += 1
        self.conn.close()
        return count

    @connect_to_table
    def __getitem__(self, item: str) -> str:
        if not isinstance(item, str):
            raise TypeError("Key must be str")
        self.cursor.execute(
            'SELECT * from "%s" WHERE name = "%s"' % (self.table_name, item)
        )
        item = self.cursor.fetchone()
        self.conn.close()
        if item:
            return item
        raise KeyError("There is no such president")

    def __contains__(self, item: str) -> bool:
        if self[item]:
            return True
        return False
