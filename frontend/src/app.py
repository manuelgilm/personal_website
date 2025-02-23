import flet as ft 
from components.app_bar import get_app_bar
from views.page_layout import AppLayout
from components.router import router


# class PersonalWebsite(AppLayout):

#     def __init__(self, page: ft.Page):
#         super().__init__()
#         self.title = "Manuel Gil"
#         self.page = page
#         self.appbar = get_app_bar()
#         self.page.appbar = self.appbar
#         self.page.update()

#     def router(self):
#         self.page.views.clear()
#         self.page.views.append(self)
#         self.page.update()
        