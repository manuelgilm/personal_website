import flet as ft
from views.page1 import Page1
from views.page2 import Page2
from views.home import Home
from views.page_layout import AppLayout
from views.login_page import LoginPage
def page_factory(route:str, page:ft.Page):
    
    pages = {
        "/": LoginPage,
        "/page1": Page1,
        "/page2": Page2,
        
    }    
    print(pages)
    return pages.get(route)(page)


def router(e, page:ft.Page):
    page.views.clear()
    print("Initial route:", page.route)
    page.views.append(page_factory(page.route, page))
    page.update()
      