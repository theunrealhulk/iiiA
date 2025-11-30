from textual.containers import ScrollableContainer
from textual.widgets import Button,Static

class Menu(Static):
    def compose(self):
        yield Button("✨",variant="primary",id="addBtn")
        yield Button("🔎",variant="warning",id="findBtn")
        yield Button("🗑️",variant="error",id="deleteBtn")
