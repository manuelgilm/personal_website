import flet as ft 

class Page1(ft.View):
    def __init__(self, page:ft.Page):
        super().__init__()
        self.title = "Page 1"
        self.padding = 0
        button = ft.ElevatedButton("Go to Page 2", on_click=lambda _ : page.go("/page2"))
        home_button = ft.ElevatedButton("Go to Home", on_click=lambda _ : page.go("/"))
        self.controls.append(ft.Text("Page 1"))
        self.controls.append(button)
        self.controls.append(home_button)
        