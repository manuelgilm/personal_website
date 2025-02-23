import flet as ft 

class AppLayout(ft.Row):

    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.appbar = None
        self.page.update()
        self.page: ft.Page = page
       
