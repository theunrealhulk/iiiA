from textual.app import App


class StopWatchApp(App):
     BINDINGS = [
        ("q", "quit", "Quit"),
    ]



if __name__=="__main__":
    StopWatchApp().run()