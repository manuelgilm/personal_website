import flet as ft
from flet.core.control_event import ControlEvent
active_user = {
    "username": "user",
    "password": "password",
}
class LoginPage(ft.View):
    
    def __init__(self, page: ft.Page):
        super().__init__()
        self.title = "Login Page"
        self.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.alert_dialog = ft.AlertDialog(
            title=ft.Text("Invalid Credentials, Please try again"),
            on_dismiss=lambda _: self.update()
        )
        self.username = ft.TextField(label="Username", text_align=ft.TextAlign.CENTER, width=200)
        self.password = ft.TextField(label="Password", text_align=ft.TextAlign.CENTER, width=200,password=True)
        self.login_button = ft.ElevatedButton("Login", on_click=self.login, disabled=True, width=200)
        
        self.login_button.on_change = self._validate
        self.username.on_change = self._validate
        self.password.on_change = self._validate

        self.controls.append(self.username)
        self.controls.append(self.password)
        self.controls.append(self.login_button)
        self.controls.append(self.alert_dialog)
        
    def login(self, e: ControlEvent):
        if self.username.value == active_user["username"] and self.password.value == active_user["password"]:
            self.page.go("/page1")
        else:
            self._open_dlg(e)
            self.username.value = ""
            self.password.value = ""
            self.update()

    def _open_dlg(self, e: ControlEvent):
        self.alert_dialog.open=True
        self.update()
        
    def update(self):
        self.page.controls.clear()
        self.page.add(self)
        self.page.update()


    def _validate(self, e: ControlEvent)->None:
        """
        Validate all the fields are filled
        """

        if all([self.username.value, self.password.value]):
            self.login_button.disabled = False
        else:
            self.login_button.disabled = True

        self.update()
        
    def __str__(self):
        return "Login Page"
        
    def __repr__(self):
        return "Login Page"
        
    def __call__(self):
        return self.page