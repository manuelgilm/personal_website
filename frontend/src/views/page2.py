import flet as ft

class Page2(ft.View):
    def __init__(self, page:ft.Page):
        super().__init__()
        self.title = "Page 2"
        self.padding = 0
        button = ft.ElevatedButton("Go to Page 1", on_click=lambda _ : page.go("/page1"))
        home_button = ft.ElevatedButton("Go to Home", on_click=lambda _ : page.go("/"))
        self.controls.append(ft.Text("Page 2")) 
        self.controls.append(button)
        self.controls.append(home_button)