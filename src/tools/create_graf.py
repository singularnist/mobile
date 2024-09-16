from datetime import datetime
import plotly.express as px
import plotly.graph_objects as go

from src.api.request_mreport import Request_Mreport
from src.config.apiconf import Api_Conf

class Create_graf():
    def __init__(self) -> None:
        self.data = Request_Mreport().fetch_data


    

    async def start(self):
        data = await Request_Mreport().fetch_data(Api_Conf.API_GRAF)
        fig1 = go.Figure()
        fig2 = go.Figure()

        dates1 = []
        users1 = []
        all_switch1 = []
        off_switch1 = []
        for item in data['result_vn']:
            dates1.append(datetime.strptime(item['date'], '%Y-%m-%d %H:%M'))
            users1.append(item['sumAbon'])
            all_switch1.append(item['sumAllAbon'])
            off_switch1.append(item['sw_power_off'])

        fig1.add_trace(go.Scatter(
            x=dates1, 
            y=users1, 
            name='Users', 
            mode='lines+markers'
        ))
        fig1.add_trace(go.Scatter(
            x=dates1, 
            y=all_switch1, 
            name='All Switch', 
            mode='lines+markers',
            yaxis='y2'
        ))
        fig1.add_trace(go.Scatter(
            x=dates1, 
            y=off_switch1, 
            name='Off Switch', 
            mode='lines+markers',
            yaxis='y2'
        ))
        fig1.update_layout(
            title='Графік даних',
            xaxis_title='Дата',
            yaxis_title='Користувачі',
            yaxis2=dict(
                title='Switches',
                overlaying='y',
                side='right'
            ),
            autosize=True,
            height=400,
            width=800,
             xaxis=dict(
                tickformat='%d-%m-%Y %H:%M', 
                tickangle=-45, 
                tickmode='auto',
                nticks=20,
            )
        )
        dates2 = []
        users2 = []
        all_switch2 = []
        off_switch2 = []
        for item in data['result_km']:
            dates2.append(datetime.strptime(item['date'], '%Y-%m-%d %H:%M'))
            users2.append(item['sumAbon'])
            all_switch2.append(item['sumAllAbon'])
            off_switch2.append(item['sw_power_off'])

        fig2.add_trace(go.Scatter(
            x=dates2, 
            y=users2, 
            name='Users', 
            mode='lines+markers'
        ))
        fig2.add_trace(go.Scatter(
            x=dates2, 
            y=all_switch2, 
            name='All Switch', 
            mode='lines+markers',
            yaxis='y2'
        ))
        fig2.add_trace(go.Scatter(
            x=dates2, 
            y=off_switch2, 
            name='Off Switch', 
            mode='lines+markers',
            yaxis='y2'
        ))
        fig2.update_layout(
            title='Графік даних KM',
            xaxis_title='Дата',
            yaxis_title='Користувачі',
            yaxis2=dict(
                title='Switches',
                overlaying='y',
                side='right'
            ),
            autosize=True,
            height=400,
            width=800,
             xaxis=dict(
                tickformat='%d-%m-%Y %H:%M', 
                tickangle=-45, 
                tickmode='auto', 
                nticks=20, 
            )
        )
        
        return fig1,fig2

