import flet as ft
from flet import Column
from src.config.fletconf import ConfFlet
from src.core.page import Main_page, Graf_Page, Complaint_page

class Main:
    def __init__(self):
        self.page = None
        self.content = Column(scroll='vertical')
        self.main_page = Main_page().main_page
        self.graf_page = Graf_Page().graf_page
        self.complaint_page = Complaint_page().complaint_page

    async def switch_page(self, e):
        selected_tab = e.control.selected_index
        self.content.controls.clear()
        if selected_tab == 0:
            self.content.controls.append( await self.main_page())
        elif selected_tab == 1:
            self.content.controls.append( await self.graf_page())
        elif selected_tab == 2:
            self.content.controls.append( await self.complaint_page())
        self.page.update()

    async def main(self, page):
        self.page = ConfFlet.return_page(page)
        self.content.controls.append(await self.main_page())

        self.page.navigation_bar = ft.CupertinoNavigationBar(
            bgcolor=ft.colors.BLACK12,
            inactive_color=ft.colors.GREY,
            active_color=ft.colors.YELLOW_300,
            destinations=[
                ft.NavigationBarDestination(icon=ft.icons.EXPLORE, label="Головно"),
                ft.NavigationBarDestination(icon=ft.icons.COMMUTE, label="Графіки"),
                ft.NavigationBarDestination(
                    icon=ft.icons.BOOKMARK_BORDER,
                    selected_icon=ft.icons.BOOKMARK,
                    label="Звернення",
                ),
            ],
            on_change= self.switch_page,
        )

        self.page.add(
            ft.SafeArea(
                self.content 
            )
        )

ft.app(Main().main)
