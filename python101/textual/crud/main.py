from textual.app import App
from components.menu import Menu
from components.dataViewer import DataViewer
from textual.widgets import Header, Footer



class CrudApp(App):

    # required for running the app from vscode
    BINDINGS = [
        ("q", "quit", "Quit"), #quit app with 'q' instead of 'CTRL+Q'
        ("d", "cycle_themes", "Theme: "), # d to switch between dark/white theme
        ("n", "create", "New"), # d to switch between dark/white theme
        ("u", "update_selected", "Updated Seleced"), # d to switch between dark/white theme
        ("r", "delete_selected", "Delete Selected"), # d to switch between dark/white theme
    ]
    CSS_PATH="style.tcss"
    def on_mount(self):
        # Store available themes and current index
        self.theme_names = list(self.available_themes.keys())
        try:
            self.theme_index = self.theme_names.index(self.theme)
        except ValueError:
            self.theme_index = 1

    def compose(self):
        yield Header(show_clock=True)
        yield Menu()
        yield DataViewer()
        yield Footer()

    def action_cycle_themes(self):
        self.theme = list(self.available_themes.keys())[self.theme_index]
        self.theme_index+=1
        if self.theme_index>= len(list(self.available_themes.keys())):
            self.theme_index=0
    
    def action_create(self):
        pass
    def action_update_selected(self):
        pass
    def action_delete_selected(self):
        pass

if __name__=="__main__":
    CrudApp().run()