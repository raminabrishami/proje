import os
from dash import Dash,dcc,Output,Input
import dash_bootstrap_components as dbc
import dash_html_components as html
import plotly.graph_objects as go

app=Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])

btn=dbc.Button('جستو جو',style={'margin-top':'20px'})

div=html.Div()

@app.callback(
    Output(div,component_property='children'),
    Output(btn,component_property='n_clicks'),
    Input(btn,component_property='n_clicks')
    )


def update_text(n_clicks):
    if n_clicks>0:
        row=[html.Tr([html.Th('تصویر'),html.Th('قیمت'), html.Th('محصول')],style={'padding-top':'2px', 'padding-bottom':'2px'})]
        with open ('title.txt' , encoding='utf-8') as reads:
            title=reads.read().split('\n')
        with open ('price.txt') as reads:
            price=reads.read().split('\n')
        with open ('links.txt') as reads:
            links=reads.read().split('\n')
        image_list=os.listdir('assets/images')
        for t,p,l,image in zip(title,price,links,image_list):
            img=html.Img(src=app.get_asset_url(f'images/{image}'),width='100px' ,height='100px')
            v=html.Tr([html.Td(img),html.Td(p),html.A(t,href=l)],style={'border-width': '2px','border-color': 'white','background-color': '#D6EEEE','padding-top':'2px', 'padding-bottom':'2px'} )
            row.append(v)
        children=[html.Table(row,style={'width':'100%','color': 'black','textAlign': 'center','margin-top':'20px','padding-top':'2px', 'padding-bottom':'2px' })]
        return children,n_clicks
    
app.layout=dbc.Container([dbc.Row([div,btn],className='text-center')])

if __name__=='__main__':
    app.run_server(port='8000')
