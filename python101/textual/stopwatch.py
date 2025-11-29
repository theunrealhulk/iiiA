from textual.app import App
from textual.containers import ScrollableContainer
from textual.widgets import Header, Footer,Button,Static

class TimeDisplay(Static):
    def compose(self):
        return super().compose()

class StopWatchCmp(Static):
    def compose(self):
        yield Button("Start",variant="primary",id="Start")
        yield Button("Stop",variant="error",id="Stop",classes="hidden")
        yield Button("Reset",id="Reset")
        yield TimeDisplay("00:00:00.00",)


class StopWatchApp(App):

    # required for running the app from vscode
    BINDINGS = [
        ("q", "quit", "Quit"), #quit app with 'q' instead of 'CTRL+Q'
        ("d", "cycle_themes", "Theme: "), # d to switch between dark/white theme
    ]
    CSS_PATH="stopwatch.tcss"
    def on_mount(self):
        # Store available themes and current index
        self.theme_names = list(self.available_themes.keys())
        try:
            self.theme_index = self.theme_names.index(self.theme)
        except ValueError:
            self.theme_index = 0

    def compose(self):
        yield Header(show_clock=True)
        with ScrollableContainer(id="stopwatches"):
            yield StopWatchCmp()
            yield StopWatchCmp()
            yield StopWatchCmp()
        yield Footer()

    def action_cycle_themes(self):
        self.theme = list(self.available_themes.keys())[self.theme_index]
        self.theme_index+=1
        if self.theme_index>= len(list(self.available_themes.keys())):
            self.theme_index=0
    


if __name__=="__main__":
    StopWatchApp().run()