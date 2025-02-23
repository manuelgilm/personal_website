import flet as ft 
from typing import Callable

def get_nav_bar(nav_change:Callable):
    """
    Returns a NavigationBar with the following destinations:

    :param nav_change: The function to call when the NavigationBar changes
    """
    navigation_bar = ft.NavigationBar(
        selected_index=0,
        on_change= nav_change,
        destinations = [
            ft.NavigationBarDestination(icon = ft.Icons.HOME, label="Home"),
            ft.NavigationBarDestination(icon = ft.Icons.INFO, label="About"),
            ft.NavigationBarDestination(icon = ft.Icons.MAIL, label="Contact"),
        ]
    )
    return navigation_bar