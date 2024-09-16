import flet as ft
from flet import Column, Text, Container, Row,ScrollMode
from flet.plotly_chart import PlotlyChart


from src.tools.create_graf import Create_graf
from src.api.request_mreport import Request_Mreport
from src.config.colorconf import Color_Conf
from src.config.apiconf import Api_Conf

class Main_page():
    def __init__(self) -> None:
        pass
    def create_create_container(self, on, off, user, power_off, city):
        result = Column(
                controls=[
                    Container(content=Text(city,size=30,)),
                    Row(controls=[Container(
                                content=Text('Комутаторів', size=20),
                                alignment=ft.alignment.center_left,
                            ),Container(
                                content=Text(on, size=20, color=Color_Conf.LIGHT_GREEN),
                                alignment=ft.alignment.center_right,
                                expand=True 
                            ),]),

                    Row(controls=[Container(
                                content=Text('Вимкнений', size=20),
                                alignment=ft.alignment.center_left,
                            ),
                            Container(
                                content=Text(off, size=20, color=Color_Conf.CRITICAL),
                                alignment=ft.alignment.center_right,
                                expand=True 
                            ),
                        ]
                    ),
                    Row(
                        controls=[
                            Container(
                                content=Text('Без живлення', size=20,),
                                alignment=ft.alignment.center_left,
                            ),
                            Container(
                                content=Text(power_off, size=20,color=Color_Conf.WARNING),
                                alignment=ft.alignment.center_right,
                                expand=True
                            ),
                        ]
                    ),
                    Row(
                        controls=[
                            Container(
                                content=Text('Абонентів', size=20, ),
                                alignment=ft.alignment.center_left,
                            ),
                            Container(
                                content=Text(user, size=20,color=Color_Conf.LIGHT_BLUE),
                                alignment=ft.alignment.center_right,
                                expand=True
                            ),
                        ]
                    ),
                ]
            )
        return result

    async def main_page(self):
        api_result = await Request_Mreport().fetch_data(Api_Conf.API_DASHBORD)
        result = Container(
            content=Column(
                scroll=ScrollMode.AUTO,
                auto_scroll=True,
                controls=[
                    Text('Головна', size=30),
                    Container(
                        content=self.create_create_container(api_result['vn_on'],
                                api_result['vn_off'],
                                api_result['user_vn'],
                                api_result['vn_off_power_off'], 'Вінниця'),
                        margin=10,
                        padding=10,
                        alignment=ft.alignment.center,
                        bgcolor=Color_Conf.bg_color,
                        border_radius=10,
                    ),
                    Container(
                        content=self.create_create_container(api_result['km_on'],
                                api_result['km_off'],
                                api_result['user_km'],
                                api_result['km_off_power_off'], 'Хмельницький'),
                        margin=10,
                        padding=10,
                        alignment=ft.alignment.center,
                        bgcolor=Color_Conf.bg_color,
                        border_radius=10,
                    )
                ]
            )
        )

        return result
    


class Graf_Page():
    def __init__(self) -> None:
        pass
    
    async def graf_page(self):
        fig1, fig2 = await Create_graf().start()
        return Container(
            content=Column(
                scroll=ScrollMode.AUTO,
                auto_scroll=True,
                controls=[
                    Text("Графіки", size=30),
                    Container(
                        content=PlotlyChart(fig1),
                    ),
                    Container(
                        content=PlotlyChart(fig2),
                    )
                ],
                spacing=20
            ),
        )

    
    
class Complaint_page():
    def __init__(self) -> None:
        pass
    
    async def complaint_page(self):
        return Column(controls=[Text("Звернення", size=30)])
