from textual.app import App


class StopWatchApp(App):
    # required for running the app from vscode
    BINDINGS = [
        ("q", "quit", "Quit"), #quit app with 'q' instead of 'CTRL+Q'
    ]



if __name__=="__main__":
    StopWatchApp().run()