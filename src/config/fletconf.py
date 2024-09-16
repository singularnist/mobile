from flet import Page, ScrollMode, ThemeMode,MainAxisAlignment,CrossAxisAlignment

class ConfFlet():
    @staticmethod 
    def return_page(page:Page) -> Page:
        page.theme_mode = ThemeMode.DARK
        page.bgcolor = '#181a21'
        page.adaptive = True
        page.scroll  = ScrollMode.ALWAYS
        # page.vertical_alignment = MainAxisAlignment.CENTER
        # page.horizontal_alignment = CrossAxisAlignment.CENTER
        return page