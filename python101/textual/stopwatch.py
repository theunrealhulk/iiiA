from textual.app import App
from textual.widgets import Header, Footer


class StopWatchApp(App):
    # required for running the app from vscode
    BINDINGS = [
        ("q", "quit", "Quit"), #quit app with 'q' instead of 'CTRL+Q'
    ]

    def compose(self):
        yield Header(show_clock=True)
        yield Footer()



if __name__=="__main__":
    StopWatchApp().run()