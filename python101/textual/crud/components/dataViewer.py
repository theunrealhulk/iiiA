from textual.containers import Container
from textual.widgets import DataTable
from itertools import cycle
from data.utility import Utility
class DataViewer(Container):
    cursors = cycle(["column", "row", "cell", "none"])

    def compose(self):
        yield DataTable()

    def on_mount(self):
        data=Utility.loadData('data/data.json')
        if not data:
            return
        
        columns = list(data[0].keys())
        table = self.query_one(DataTable)
        table.focus() 
        table.cursor_type = "row"
        table.zebra_stripes = True
        # 1. Get columns from first dict keys
        table.add_columns(*columns)
        # 2. Convert each dict to row values
        rows = [list(item.values()) for item in data]
        table.add_rows(rows)

    def key_c(self):
        table = self.query_one(DataTable)
        table.cursor_type = next(self.cursors)
