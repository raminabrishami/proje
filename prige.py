import os
from dash import Dash,dcc,Output,Input
import dash_bootstrap_components as dbc
import dash_html_components as html
import plotly.graph_objects as go

app=Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])

text=html.H3('',style={'margin-top':'40px'})

inputt=dbc.Input(value='taip',style={'margin-top':'40px'})

btn=dbc.Button('جستو جو',style={'margin-top':'40px'})

div=html.Div(style={'margin-top':'60px'})

nemodar=dcc.Graph(figure={})

@app.callback(
    Output(text,component_property='children'), 
    Output(div,component_property='children'),
    Output(btn,component_property='n_clicks'),
    Output(nemodar, component_property='figure'),
    Input(inputt,component_property='value'),
    Input(btn,component_property='n_clicks')
    )



def update_text(inp_text,n_clicks):
    global ll
    if n_clicks>0:
        row=[html.Tr([html.Th('تصویر'),html.Th('قیمت'), html.Th('محصول')])]
        with open ('title.txt' , encoding='utf-8') as reads:
            title=reads.read().split('\n')
        with open ('price.txt') as reads:
            price=reads.read().split('\n')
        with open ('links.txt') as reads:
            links=reads.read().split('\n')
        image_list=os.listdir('assets/images')
        for t,p,l,image in zip(title,price,links,image_list):
            img=html.Img(src=app.get_asset_url(f'images/{image}'),width='100px' ,height='100px')
            v=html.Tr([html.Td(img),html.Td(p),html.A(t,href=l)] )
            row.append(v)
        children=[html.Table(row,style={'width':'100%'})]
        price=list(map(int,price))
        fig = go.Figure(data=[go.Scatter(x=list(range(0,len(price))), y=price)])
        ll=1
        return inp_text,children,n_clicks,fig

 
app.layout=dbc.Container([dbc.Row([inputt,btn,text,div,nemodar],className='text-center')])


if __name__=='__main__':
    app.run_server(port='8000')
