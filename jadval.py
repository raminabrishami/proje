import os
from dash import Dash,dcc,Output,Input
import dash_bootstrap_components as dbc
import dash_html_components as html
import plotly.graph_objects as go

app=Dash(__name__,external_stylesheets={dbc.themes.BOOTSTRAP})

text=html.H3('' ,style={'text-align':'center'})

search=dbc.Input(value='تایپ کنید', style={'text-align':'center'})

btn=dbc.Button('جستو جو' ,style={'margin-top':'20px'})

div=html.Div()

nemodar=dcc.Graph(figure={})

@app.callback(
    Output(text,component_property='cilderen'),
    Output(div,component_property='cilderen'),
    Output(nemodar, component_property='figure'),
    Output(btn,component_property='n_clicks'),
    Input(btn,component_property='n_clicks'),
    Input(search,component_property='value')
    )


def create_table(n_clicks,np_text):
    if n_clicks>0:
        row=[html.Th('تصویر'),html.Th('قیمت'), html.Th('محصول')]
        with open ('title' , encoding='utf-8') as reads:
            title=reads.read().split('\n')
        with open ('price') as reads:
            price=reads.read().split('\n')
        with open ('links') as reads:
            links=reads.read().split('\n')
        image_list=os.listdir('asset/images')
        for t,p,l,image in zip(title,price,links,image_list):
            img=html.Img(src=app.get_asset_url(f'images/{image}'),width='100px' ,height='100px')
            v=html.Tr(html.Td(img),html.Td(p),html.A(t,href=l))
            row.append(v)
        children=[html.Table(row,style={'wedth':'100px'})]
        number_list=list(map(int,price))
        print(number_list)
        figure=go.Figure(data=go.scatter(x=list(range(0,len(number_list)),y=number_list )))
        return np_text,figure ,children , n_clicks

 

 
app.layout=dbc.Container([dbc.Row([text,btn,div,nemodar],class_name='text-center')])

if __name__=='__main__':
    app.run_server(port='8000')
