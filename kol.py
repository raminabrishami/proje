import os
from dash import Dash,dcc,Output,Input
import dash_bootstrap_components as dbc
import dash_html_components as html
import plotly.graph_objects as go
import selenium
import requests
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from unidecode import unidecode


class kol():
    
    def __init__(self):
        self.dash()
        

    def title(self):     
        path='chromedriver.exe'
        driver=webdriver.Chrome(executable_path=path)
        driver.get(f'https://www.digikala.com/search/?q={textt}')
        time.sleep(10)
        images=driver.find_elements(By.CSS_SELECTOR,'.w-100.radius-medium.d-inline-block.ls-is-cached.lazyloaded')
        driver.execute_script("window.scrollTo(0,2000)")
        time.sleep(3)
        driver.execute_script("window.scrollTo(2000,4000)")
        time.sleep(4)
        driver.execute_script("window.scrollTo(4000,6000)")
        time.sleep(3)
        driver.execute_script("window.scrollTo(6000,8000)")
        time.sleep(3)
        driver.execute_script("window.scrollTo(8000,10000)")
        time.sleep(3)
        driver.execute_script("window.scrollTo(10000,12000)")
        time.sleep(3)
        driver.execute_script("window.scrollTo(12000,14000)")
        for indx,j in enumerate(images):
            if indx==50:
                break
            src=j.get_attribute('src')
            image_data=requests.get(src).content
            with open(f'assets/imagess/image_name{indx}.jpg','wb') as g:
                g.write(image_data)

        s=''
        pce=driver.find_elements(By.CSS_SELECTOR,'.d-flex.ai-center.jc-end.gap-1.color-700.color-400.text-h5.grow-1')
        for indx,i in enumerate(pce):
            if indx==49:
                s+=str(a)
                break
            price=i.find_element(By.TAG_NAME,'span')
            span=price.get_attribute('innerHTML')
            a = unidecode(span)
            a=a.replace(',','')
            s+=str(a)+'\n'
        with open('price.txt' , 'w' ,encoding='utf-8') as ss:
            ss.write(s)


        xc=''
        links=driver.find_elements(By.CSS_SELECTOR,".d-block.pointer.pos-relative.bg-000.overflow-hidden.grow-1.py-3.px-4.px-2-lg.h-full-md.styles_VerticalProductCard--hover__ud7aD")
        for indx,i in enumerate(links):
            if indx==50:
                break
            link=i.get_attribute('href')
            xc+=str(link)+'\n'
        with open('links.txt' ,'w' ,encoding='utf-8') as lin:
            lin.write(xc)
            
        xcc=''
        title=driver.find_elements(By.CSS_SELECTOR,".ellipsis-2.text-body2-strong.color-700.styles_VerticalProductCard__productTitle__6zjjN")
        for indx,i in enumerate(title):
            if indx==50:
                break
            ss=i.get_attribute('innerHTML')
            xcc+=str(ss)+'\n'
        with open('title.txt' ,'w' ,encoding='utf-8-sig') as writes:
                writes.write(str(xcc))


    def dash(self):

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
            global textt
            if n_clicks>0:
                textt=inp_text
                self.title()
                row=[html.Tr([html.Th('تصویر'),html.Th('قیمت'), html.Th('محصول')])]
                with open ('title.txt' ,'r') as reads:
                    title=reads.read().split('\n')
                with open ('price.txt','r') as reads:
                    price=reads.read().split('\n')
                with open ('links.txt','r') as reads:
                    links=reads.read().split('\n')
                image_list=os.listdir('assets/images')
                for t,p,l,image in zip(title,price,links,image_list):
                    img=html.Img(src=app.get_asset_url(f'images/{image}'),width='100px' ,height='100px')
                    v=html.Tr([html.Td(img),html.Td(p),html.A(t,href=l)] ,style={'border-width': '2px','border-color': 'white','padding-top':'4px', 'padding-bottom':'2px'} )
                    row.append(v)
                children=[html.Table(row,style={'width':'100%'})]
                price=list(map(int,price))
                fig = go.Figure(data=[go.Scatter(x=list(range(0,len(price))), y=price)])
                return inp_text,children,n_clicks,fig

        colors = {
            'background': '#f5f1ff',
            'text': '#7FDBFF'
                }
        app.layout=dbc.Container([dbc.Row([inputt,btn,text,div,nemodar],className='text-center',style={'backgroundColor': colors['background']})])


        if __name__=='__main__':
            app.run_server(debug=True,port=8040)


c=kol()
