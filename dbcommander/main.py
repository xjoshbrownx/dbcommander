from textual.app import App, ComposeResult
from textual.widgets import Footer, Button, Static
from textual.containers import Horizontal 
# from textual.widgets import Placeholder, TreeControl, Button, Header, Static, Footer, DirectoryTree, Hor
from textual.widget import Widget


# class Window(Widget):

#     BINDINGS = [
#         ("f", "toggle_browser", "Toggle Browser"),
#     ]

#     def compose(self) -> ComposeResult:
#         yield Widget(name='sidebar', id='sidebar', classes='workingwindow')
#         yield Widget(name='querywindow', id='querywindow', classes='workingwindow')

class MenuButtons(Horizontal):
    def compose(self) -> ComposeResult:
        yield Button("File", id="file", classes="menubutton")
        yield Button("Object", id="object", classes="menubutton")
        yield Button("Tools", id="tools", classes="menubutton")
        yield Button("Help", id="help", classes="menubutton")


class Menu(Widget):

    def compose(self) -> ComposeResult:
        yield Static("DB Commander", id='menutext', classes='menuitem')
        # yield MenuButtons(id='menubuttons', classes='menuitem')
        yield Button("File", id="file", classes="menubutton")
        yield Button("Object", id="object", classes="menubutton")
        yield Button("Tools", id="tools", classes="menubutton")
        yield Button("Help", id="help", classes="menubutton")

class SideBar(Widget):

    def compose(self) -> ComposeResult:
        yield Static('###SIDEBAR###')


class QueryWindow(Widget):

    def compose(self) -> ComposeResult:
        yield Static('QUERY WINDOW')

class MainApp(App):

    CSS_PATH = "css/main.css"
    BINDINGS = [
        ("f", "toggle_browser", "Toggle Browser"),
        ("q", "quit", "Quit"),
        ("d","toggle_dark", "Toggle Darkmode"),
    ]

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Menu(name='menu',id='menubar',classes='menu')
        yield SideBar(name='sidebar', id='sidebar', classes='workingwindow')
        yield QueryWindow(name='querywindow', id='querywindow', classes='workingwindow')
        yield Footer()

    def action_toggle_browser(self) -> None:
        """An action to toggle visiblity of the browser window""" 
        self.toggle_class('sidebar','-active')

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.dark = not self.dark

if __name__ == "__main__":
    app = MainApp()
    app.run()