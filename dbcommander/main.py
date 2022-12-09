from textual.app import App, ComposeResult
from textual.widgets import Footer, Button, Static
from textual.widget import Widget


class Menu(Widget):

    def compose(self) -> ComposeResult:
        yield Static("DB Commander", id='menutext', classes='menubutton')
        # yield MenuButtons(id='menubuttons', classes='menuitem')
        yield Button("File", id="file", classes="menubutton")
        yield Button("Object", id="object", classes="menubutton")
        yield Button("Tools", id="tools", classes="menubutton")
        yield Button("Help", id="help", classes="menubutton")


class BrowserControl(Widget):

    def compose(self) -> ComposeResult:
        yield Static('Browser', id='browsertext', classes='browseritem')
        yield Button('Query Tool', id='querytool', classes='browseritem')
        yield Button('View Data', id='viewdata', classes='browseritem')
        yield Button('Filter Rows', id='filterrows', classes='browseritem')
        yield Button('Search Objects', id='searchobjects', classes='browseritem')


class QueryControl(Widget):

    def compose(self) -> ComposeResult:
        yield Static('Query Window', id='querywindowtext', classes='queryitem')
        yield Button('Dependants', id='dependantsmenu', classes='querybutton')
        yield Button('Dashboard', id='dashboardmenu', classes='querybutton')
        yield Button('Properties', id='propertiesmenu', classes='querybutton')
        yield Button('SQL', id='sqlmenu', classes='querybutton')
        yield Button('Statistics', id='statistics', classes='querybutton')
        yield Button('Dependancies', id='dependancies', classes='querybutton')


class SchemaBrowser(Widget):

    def compose(self) -> ComposeResult:
        yield Static('SCHEMA BROWSER')


class SideBar(Widget):

    def compose(self) -> ComposeResult:
        yield BrowserControl(name='browsercontrol', id='browsercontrol', classes='menubar')
        yield SchemaBrowser(name='schemabrowser', id='schemabrowser', classes='windower')


class QueryWindow(Widget):

    def compose(self) -> ComposeResult:
        yield QueryControl(name='querycontrol', id='querycontrol', classes='windower')
        yield Static('QUERY WINDOW', id='querypane')


class MainApp(App):

    CSS_PATH = "css/main.css"
    BINDINGS = [
        ("f", "toggle_browser", "Toggle Browser"),
        ("q", "quit", "Quit"),
        ("d","toggle_dark", "Change Theme"),
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