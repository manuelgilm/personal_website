import flet as ft 

class Home(ft.View):

    def __init__(self, page: ft.Page):
        super().__init__()
        self.title = "Home Page"
        button1 = ft.ElevatedButton("Go to Page 1", on_click=lambda _ : page.go("/page1"))
        button2 = ft.ElevatedButton("Go to Page 2", on_click=lambda _ : page.go("/page2"))
        self.controls.append(button1)
        self.controls.append(button2)
        
        
        
    def update(self):
        self.page.controls.clear()
        self.page.add(self)
        self.page.update()
        
    def __str__(self):
        return "Home Page"
        
    def __repr__(self):
        return "Home Page"
        
    def __call__(self):
        return self.page