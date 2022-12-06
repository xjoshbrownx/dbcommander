from textual.app import App, ComposeResult
from textual.widgets import Placeholder, TreeControl, Button, Header, Static

# class MenuBar():
#     def compose(self) -> ComposeResult:
#         yield Static('DBcommander', id='menutitle')
#         yield Button('|||', id='hamburger')
    # static title 
    # depending on size
    # either 
    #     hamburger menu
    #     4 menu items
            # file
            # object
            # tools
            # help

# class DataBaseBrowser
    #browser top row
        #static title "browser"
        # 4 buttons on right
            # query tool
                # opens query tool in main window
            # view data 
                #conditional on view, table, materialized view
                #opens query tool on table with filter selected
            # filtered rows
                # opens popup
            # search objects
                # opens popup
    #tree view for each server
        # tree view for each database   

# class mainwindow()
    #6 tabs + open queries
        #dashboard
        #properties
        # SQL
        # statistics
        # dependancies
        # dependants

class MainApp(App):
    CSS_PATH = "css/main.css"
    BINDINGS = [
        ("f", "toggle_tables", "Toggle Tables"),
        ("q", "quit", "Quit"),
    ]


    def compose(self) -> ComposeResult:
        # yield MenuBar()
        yield Static('DBcommander', id='menutitle')
        yield Button('|||', id='hamburger', classes='menubar')

        # yield Welcome()

    def on_button_pressed(self) -> None:
        self.exit()


if __name__ == "__main__":
    app = MainApp ()
    app.run()