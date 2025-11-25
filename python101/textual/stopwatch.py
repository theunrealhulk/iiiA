from textual.app import App
from textual.widgets import Header, Footer


class StopWatchApp(App):

    dark_mode = False  # track custom dark mode

    # required for running the app from vscode
    BINDINGS = [
        ("q", "quit", "Quit"), #quit app with 'q' instead of 'CTRL+Q'
        ("d", "toggle_dark_mode", "toggle Dark Mode"), #quit app with 'q' instead of 'CTRL+Q'
    ]

    def compose(self):
        yield Header(show_clock=True)
        yield Footer()

    def action_toggle_dark_mode(self):
        self.theme = "textual-dark" if self.theme == "textual-light" else "textual-light"


if __name__=="__main__":
    StopWatchApp().run()