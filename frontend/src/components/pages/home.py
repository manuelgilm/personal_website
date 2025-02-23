import flet as ft 

def show_home(page:ft.Page):
    page.controls.clear()
    text = ft.Text("Home Page")
    page.add(text)