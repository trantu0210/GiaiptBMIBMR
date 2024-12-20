import flet as ft 
from flet import * 
import bac1, bac2, bac3, bac4, page1, page2,page3, page4, huongdansudung, bmi, bmi_table, bmr, trangchu, hept2an, hept3an, gioithieu

from page1 import CalculatorApp
from page2  import CalculatorApp2
from page3 import CalculatorApp3
from page4 import CalculatorApp4
from huongdansudung import Huongdansudung
from bmi import BMIcalculator
from bmr import BMRcalculator
from bmi_table import DataTable
from bac1 import Bac1
from bac2 import Bac2
from bac3 import Bac3
from bac4 import Bac4
from trangchu import MainMenu  
from hept2an import Hept_Haian
from hept3an import Hept_Baan
from gioithieu import Gioithieu
 
def main(page: Page):
    page.title = "Giải phương trình-BMI-BMR-TDEE"      
                
    def route_change(e):   
        page.views.clear()
        page.views.append(        
            View(
                "/",     
                [    
                    Gioithieu(),                                    
                    ft.Container(
                        width=350,                                               
                        content=ft.Column(
                            controls=[   
                                ft.Container(
                                    padding=padding.only(left=35, right=35),
                                    content=ft.ResponsiveRow(
                                        controls=[
                                            ft.Column(col={"xs":2}, controls=[ft.Icon(name=ft.icons.HOME_ROUNDED, size=0) ]),
                                            ft.Column(col={"xs":10}, controls=[ElevatedButton("  Đi đến Trang chủ  ", on_click=lambda _: page.go("/trangchu"))])                                        
                                        ]
                                    )
                                )                                  
                            ]                                                              
                        )                             
                    )   
                ]            
            )
        )
        if page.route == "/trangchu":
            page.views.append(
                View(
                    "/trangchu",
                    [
                        MainMenu(),  
                        ft.Container(
                            width=350,                                               
                            content=ft.Column(
                                controls=[
                                    ft.Container(
                                        padding=padding.only(left=35, right=35),
                                        content=ft.ResponsiveRow(
                                            controls=[
                                                ft.Column(col={"xs":2}, controls=[ft.Icon(name=ft.icons.HOME_ROUNDED, size=0)]),                                             
                                                ft.Column(col={"xs":10}, controls=[ElevatedButton("  Trở về trang trước  ",  on_click=lambda _: page.go("/page1"))])                                                                                      
                                            ]                                        
                                        )                                    
                                    )                          
                                ]                                                                                          
                            )                                                     
                        )                                                                                                                 
                    ]
                )
            )    
                       
        if page.route == "/bac1":
            page.views.append(
                View(
                    "/bac1",
                    [
                        Bac1(),    
                        ft.Container(
                            width=350,                                               
                            content=ft.Column(
                                controls=[
                                    ft.Container(
                                        padding=padding.only(left=35, right=35),
                                        content=ft.ResponsiveRow(
                                            controls=[
                                                ft.Column(col={"xs":2},controls=[ft.Icon(name=ft.icons.HOME_ROUNDED, size=0)]),                                             
                                                ft.Column(col={"xs":10},controls=[ElevatedButton("  Trở về trang trước  ", on_click=lambda _: page.go("/trangchu"))])                                                                                    
                                            ]                                        
                                        )                                    
                                    )                          
                                ]                                                                                          
                            )                            
                        )                                    
                    ]
                )
            )      
        if page.route == "/bac2":
            page.views.append(
                View(
                    "/bac2",
                    [
                        Bac2(),    
                        ft.Container(
                            width=350,                                               
                            content=ft.Column(
                                controls=[
                                    ft.Container(
                                        padding=padding.only(left=35, right=35),
                                        content=ft.ResponsiveRow(
                                            controls=[
                                                ft.Column(col={"xs":2},controls=[ft.Icon(name=ft.icons.HOME_ROUNDED, size=0)]),                                             
                                                ft.Column(col={"xs":10},controls=[ElevatedButton("  Trở về trang trước  ", on_click=lambda _: page.go("/trangchu"))])                                                                                    
                                            ]                                        
                                        )                                    
                                    )                          
                                ]                                                                                          
                            )                            
                        )                                    
                    ]
                )
            ) 
        if page.route == "/bac3":
            page.views.append(
                View(
                    "/bac3",
                    [
                        Bac3(),    
                        ft.Container(
                            width=350,                                               
                            content=ft.Column(
                                controls=[
                                    ft.Container(
                                        padding=padding.only(left=35, right=35),
                                        content=ft.ResponsiveRow(
                                            controls=[
                                                ft.Column(col={"xs":2},controls=[ft.Icon(name=ft.icons.HOME_ROUNDED, size=0)]),                                             
                                                ft.Column(col={"xs":10},controls=[ElevatedButton("  Trở về trang trước  ", on_click=lambda _: page.go("/trangchu"))])                                                                                    
                                            ]                                        
                                        )                                    
                                    )                          
                                ]                                                                                          
                            )                            
                        )                                    
                    ]
                )
            ) 
        if page.route == "/bac4":
            page.views.append(
                View(
                    "/bac4",
                    [
                        Bac4(),    
                        ft.Container(
                            width=350,                                               
                            content=ft.Column(
                                controls=[
                                    ft.Container(
                                        padding=padding.only(left=35, right=35),
                                        content=ft.ResponsiveRow(
                                            controls=[
                                                ft.Column(col={"xs":2},controls=[ft.Icon(name=ft.icons.HOME_ROUNDED, size=0)]),                                             
                                                ft.Column(col={"xs":10},controls=[ElevatedButton("  Trở về trang trước  ", on_click=lambda _: page.go("/trangchu"))])                                                                                    
                                            ]                                        
                                        )                                    
                                    )                          
                                ]                                                                                          
                            )                            
                        )                                    
                    ]
                )
            )      
        if page.route == "/hept2an":
            page.views.append(
                View(
                    "/hept2an",
                    [
                        Hept_Haian(),    
                        ft.Container(
                            width=350,                                               
                            content=ft.Column(
                                controls=[                                    
                                    ft.Container(
                                        padding=padding.only(left=35, right=35),
                                        content=ft.ResponsiveRow(
                                            controls=[
                                                ft.Column(col={"xs":2},controls=[ft.Icon(name=ft.icons.HOME_ROUNDED, size=0)]),                                             
                                                ft.Column(col={"xs":10},controls=[ElevatedButton("  Trở về trang trước  ", on_click=lambda _: page.go("/trangchu"))])                                                                                    
                                            ]                                        
                                        )                                    
                                    )                          
                                ]                                                                                          
                            )                            
                        )                                    
                    ]
                )
            )    
        if page.route == "/hept3an":
            page.views.append(
                View(
                    "/hept3an",
                    [
                        Hept_Baan(),    
                        ft.Container(
                            width=350,                                               
                            content=ft.Column(
                                controls=[                                    
                                    ft.Container(
                                        padding=padding.only(left=35, right=35),
                                        content=ft.ResponsiveRow(
                                            controls=[
                                                ft.Column(col={"xs":2},controls=[ft.Icon(name=ft.icons.HOME_ROUNDED, size=0)]),                                             
                                                ft.Column(col={"xs":10},controls=[ElevatedButton("  Trở về trang trước  ", on_click=lambda _: page.go("/trangchu"))])                                                                                    
                                            ]                                        
                                        )                                    
                                    )                          
                                ]                                                                                          
                            )                            
                        )                                    
                    ]
                )
            )  
        if page.route == "/maytinh1":
            page.views.append(
                View(
                    "/maytinh1",
                    [
                        CalculatorApp(),    
                        ft.Container(
                            width=350,                                               
                            content=ft.Column(
                                controls=[
                                    ft.Container(
                                        padding=padding.only(left=35, right=35),
                                        content=ft.ResponsiveRow(
                                            controls=[      
                                                ft.Column(col={"xs":2},controls=[ft.Icon(name=ft.icons.HOME_ROUNDED, size=0)]),                                             
                                                ft.Column(col={"xs":10},controls=[ElevatedButton("  Trở về trang trước  ", on_click=lambda _: page.go("/trangchu"))])                                                                                                                                  
                                            ]                                        
                                        )                                    
                                    )                          
                                ]                                                                                          
                            )                            
                        )                                    
                    ]
                )
            ) 
        if page.route == "/maytinh2":
            page.views.append(
                View(
                    "/maytinh2",
                    [
                        CalculatorApp2(),    
                        ft.Container(
                            width=350,                                               
                            content=ft.Column(
                                controls=[
                                    ft.Container(
                                        padding=padding.only(left=35, right=35),
                                        content=ft.ResponsiveRow(
                                            controls=[
                                                ft.Column(col={"xs":2},controls=[ft.Icon(name=ft.icons.HOME_ROUNDED, size=0)]),                                             
                                                ft.Column(col={"xs":10},controls=[ElevatedButton("  Trở về trang trước  ", on_click=lambda _: page.go("/trangchu"))])                                                                                    
                                            ]                                        
                                        )                                    
                                    )                          
                                ]                                                                                          
                            )                            
                        )                                    
                    ]
                )         
            )  
        if page.route == "/maytinh3":
            page.views.append(
                View(
                    "/maytinh3",
                    [
                        CalculatorApp3(),    
                        ft.Container(
                            width=350,                                               
                            content=ft.Column(
                                controls=[
                                    ft.Container(
                                        padding=padding.only(left=35, right=35),
                                        content=ft.ResponsiveRow(
                                            controls=[
                                                ft.Column(col={"xs":2},controls=[ft.Icon(name=ft.icons.HOME_ROUNDED, size=0)]),                                             
                                                ft.Column(col={"xs":10},controls=[ElevatedButton("  Trở về trang trước  ", on_click=lambda _: page.go("/trangchu"))])                                                                                    
                                            ]                                        
                                        )                                    
                                    )                          
                                ]                                                                                          
                            )                            
                        )                                    
                    ]
                )         
            )          
        if page.route == "/maytinh4":
            page.views.append(
                View(
                    "/maytinh4",
                    [
                        CalculatorApp4(),    
                        ft.Container(
                            width=350,                                               
                            content=ft.Column(
                                controls=[
                                    ft.Container(
                                        padding=padding.only(left=35, right=35),
                                        content=ft.ResponsiveRow(
                                            controls=[
                                                ft.Column(col={"xs":2},controls=[ft.Icon(name=ft.icons.HOME_ROUNDED, size=0)]),                                             
                                                ft.Column(col={"xs":10},controls=[ElevatedButton("  Trở về trang trước  ", on_click=lambda _: page.go("/trangchu"))])                                                                                    
                                            ]                                        
                                        )                                    
                                    )                          
                                ]                                                                                          
                            )                            
                        )                                    
                    ]
                )         
            )          
        if page.route == "/huongdansudung":
            page.views.append(
                View(
                    "/huongdansudung",
                    [
                        Huongdansudung(),    
                        ft.Container(
                            width=350,                                               
                            content=ft.Column(
                                controls=[
                                    ft.Container(
                                        padding=padding.only(left=35, right=35),
                                        content=ft.ResponsiveRow(
                                            controls=[
                                                ft.Column(col={"xs":2},controls=[ft.Icon(name=ft.icons.HOME_ROUNDED, size=0)]),                                             
                                                ft.Column(col={"xs":10},controls=[ElevatedButton("  Trở về trang trước  ", on_click=lambda _: page.go("/trangchu"))])                                                                                    
                                            ]                                        
                                        )                                    
                                    )                          
                                ]                                                                                          
                            )                            
                        )                                    
                    ]
                )
            )    
        if page.route == "/bmi":
            page.views.append(
                View(
                    "/bmi",
                    [
                        BMIcalculator(),    
                        ft.Container(
                            width=350,                                               
                            content=ft.Column(
                                controls=[
                                    ft.Container(
                                        padding=padding.only(left=35, right=35),
                                        content=ft.ResponsiveRow(
                                            controls=[
                                                ft.Column(col={"xs":2},controls=[ft.Icon(name=ft.icons.HOME_ROUNDED, size=0)]),                                             
                                                ft.Column(col={"xs":10},controls=[ElevatedButton("  Trở về trang trước  ", on_click=lambda _: page.go("/trangchu"))])                                                                                    
                                            ]                                        
                                        )                                    
                                    )                      
                                ]                                                                                          
                            )                            
                        )                                    
                    ]
                )
            )  

        if page.route == "/bangdulieu":
            page.views.append(
                View(
                    "/bangdulieu",
                    [
                        DataTable(),    
                        ft.Container(
                            width=350,                                               
                            content=ft.Column(
                                controls=[
                                    ft.Container(
                                        padding=padding.only(left=35, right=35),
                                        content=ft.ResponsiveRow(
                                            controls=[
                                                ft.Column(col={"xs":2},controls=[ft.Icon(name=ft.icons.HOME_ROUNDED, size=0)]),                                             
                                                ft.Column(col={"xs":10},controls=[ElevatedButton("  Trở về trang trước  ", on_click=lambda _: page.go("/trangchu"))])                                                                                    
                                            ]                                        
                                        )                                    
                                    )                          
                                ]                                                                                          
                            )                            
                        )                                    
                    ]
                )
            )       
            
        if page.route == "/bmr":
            page.views.append(
                View(
                    "/bmr",
                    [
                        BMRcalculator(),    
                        ft.Container(
                            width=350,                                               
                            content=ft.Column(
                                controls=[
                                    ft.Container(
                                        padding=padding.only(left=35, right=35),
                                        content=ft.ResponsiveRow(
                                            controls=[
                                                ft.Column(col={"xs":2},controls=[ft.Icon(name=ft.icons.HOME_ROUNDED, size=0)]),                                             
                                                ft.Column(col={"xs":10},controls=[ElevatedButton("  Trở về trang trước  ", on_click=lambda _: page.go("/trangchu"))])                                                                                    
                                            ]                                        
                                        )                                    
                                    )                          
                                ]                                                                                          
                            )                            
                        )                                    
                    ]
                )
            ) 

        page.update()

    def view_pop(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)        
    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)      
    
ft.app(target=main,assets_dir="assets")
