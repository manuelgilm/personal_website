import flet as ft
from views.page1 import Page1
from views.page2 import Page2
from components.router import router
from functools import partial

def main(page:ft.Page):
    page.title= "Anki-like APP"
    page.theme = ft.Theme(
        page_transitions=ft.PageTransitionsTheme(
            windows=ft.PageTransitionTheme.NONE
        )
    )    
    def view_pop(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = partial(router, page=page)
    page.on_view_pop = view_pop # This seems to be necessary to go back to the previous view in web view

    page.go(page.route)

ft.app(main, view=ft.AppView.WEB_BROWSER)
