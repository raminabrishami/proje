import os
from dash import Dash,dcc,Output,Input
import dash_bootstrap_components as dbc
import dash_html_components as html

app=Dash(__name__,external_stylesheets={dbc.themes.BOOTSTRAP})
div=html.Div()

btn=dbc.Button('جستو جو')

@app.callback(

    Output(div,component_property='figure'),
    Output(btn,component_property='n_clicks'),
    Input(btn,component_property='n_clicks')
    )

def create_table(n_clicks):
    if n_clicks>0:
        row=[html.Th('تصویر'),html.Th('قیمت'), html.Th('محصول')]
        with open ('title' , encoding='utf-8') as reads:
            title=reads.read().split('/n')
        with open ('price') as reads:
            price=reads.read().split('/n')
        with open ('links') as reads:
            links=reads.read().split('/n')
        image_list=os.listdir('asset/images')
        for t,p,l,image in zip(title,price,links,image_list):
            img=html.Img(src=app.get_asset_url(f'images/{image}'),width='100px' ,height='100px')
            v=html.Tr(html.Td(img),html.Td(p),html.A(t,href=l))
            row.append(v)
        child=[html.Table(row,style={'wedth':'100px'})]
        return child , n_clicks
 
app.layout=dbc.Container([

dbc.Row([div,btn],class_name='text-center')
])

if __name__=='__main__':
    app.run_server(port='8000')
