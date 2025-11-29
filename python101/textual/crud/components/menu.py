from textual.containers import ScrollableContainer
from textual.widgets import Button,Static

class Menu(Static):
    def compose(self):
        yield Button("Create New",variant="success",id="addBtn")
        yield Button("Filter Results",variant="primary",id="findBtn")
        yield Button("Delete All",variant="error",id="deleteBtn")
