import flet as ft 
from flet import AppBar 
from typing import Optional 
from typing import List

def get_app_bar(title:Optional[str]="Manuel Gil",**kwargs):
    """
    Returns an AppBar with the title "Flet"

    :param title: The title of the AppBar
    """
    appbar_items = _get_app_bar_items(["Home", "About", "Contact"])

    return AppBar(
        title=ft.Text(title, text_align="start"),
        leading=ft.Icon(ft.Icons.GRID_GOLDENRATIO_ROUNDED),
        leading_width=100,
        center_title=False,
        toolbar_height=75,
        bgcolor=ft.Colors.LIGHT_BLUE_ACCENT_700,
        actions = [
            ft.Container(
                content = ft.PopupMenuButton(
                    items = appbar_items
                ),
                margin=ft.margin.only(left=50, right=25)
            )
        ]
    )

def _get_app_bar_items(items:Optional[list]=None):
    """
    Returns a list of AppBar items

    :param items: List of AppBar items
    """

    appbar_items = [
        ft.PopupMenuItem(text= text) for text in items
    ]
    return appbar_items


