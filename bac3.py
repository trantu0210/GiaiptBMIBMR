import flet as ft
import numpy as np
from numpy import roots
from flet import *

class Bac3(ft.Container):
    def __init__(self):
        super().__init__()        
        self.width = 350        
        self.border_radius = border_radius.only(top_left=30, top_right=30, bottom_left=10, bottom_right=10)       
        self.bgcolor = "#089908"  
        self.padding = padding.only(top=44, left=14, right=14, bottom=15)     
        self.a =TextField(label="Nhập a",hint_text="a",content_padding=padding.Padding(left=10, right=10, top=0, bottom=0))        
        self.b=TextField(label="Nhập b",hint_text="b",content_padding=padding.Padding(left=10, right=10, top=0, bottom=0))        
        self.c=TextField(label="Nhập c",hint_text="c",content_padding=padding.Padding(left=10, right=10, top=0, bottom=0))
        self.d=TextField(label="Nhập d",hint_text="d",content_padding=padding.Padding(left=10, right=10, top=0, bottom=0))  
        self.result=Text("", color="#333333", weight=ft.FontWeight.BOLD)
        self.result2=Text("", color="#f24b0c", weight=ft.FontWeight.BOLD)        
        self.content = ft.Column(
            controls=[       
                ft.Container(
                    width=350,
                    content=ft.Column(
                        controls=[ 
                            ft.Container(
                                padding=padding.only(left=15, right=15),
                                content=ft.ResponsiveRow(
                                    controls=[                                      
                                        ft.Column(col={"xs":12}, controls=[ ft.Text("Pt :Ax³ + Bx² + Cx + D = 0", size=21, color="#FFFFFF", weight=ft.FontWeight.W_600)])                                                                                                         
                                    ]                                        
                                )       
                            )                                                                                                                               
                        ]                                                                                          
                    )                                                           
                ),   
                ft.Column(
                    height=400,
                    scroll=ft.ScrollMode.ALWAYS,                    
                    controls=[
                        ft.Container(                  
                            bgcolor="#ffffff",      
                            border_radius=0,
                            padding = 20,                 
                            content=ft.Column(
                                controls=[     
                                    ft.Row(controls=[ft.Text("", size=0)]),         
                                    ft.ResponsiveRow(controls=[
                                        ft.Column(col={"xs": 12}, controls=[self.a]),   
                                    ]),  
                                    ft.Row(controls=[ft.Text("", size=0)]), 
                                    ft.ResponsiveRow(controls=[
                                        ft.Column(col={"xs": 12}, controls=[self.b]),   
                                    ]), 
                                    ft.Row(controls=[ft.Text("", size=0)]),    
                                    ft.ResponsiveRow(controls=[
                                        ft.Column(col={"xs": 12}, controls=[self.c]),   
                                    ]),
                                    ft.Row(controls=[ft.Text("", size=0)]),                                      
                                    ft.ResponsiveRow(controls=[
                                        ft.Column(col={"xs": 12}, controls=[self.d]),   
                                    ]),  
                                    ft.Row(controls=[ft.Text("", size=0)]),                                                                         
                                    ft.Row(controls=[ft.Text("", size=0)]),          
                                    ft.Container(
                                        padding=padding.only(left=20, right=20),
                                        content=ft.ResponsiveRow(                                
                                            controls=[
                                                ft.Column(col={"xs":6}, controls=[ElevatedButton("  Kết quả  ", on_click=self.calc)]),
                                                ft.Column(col={"xs":6}, controls=[ElevatedButton("  Làm lại  ", on_click=self.de)])                                        
                                            ]
                                        )
                                    ),
                                    ft.Row(controls=[ft.Text("", size=0)]), 
                                    ft.Container(
                                        padding=padding.only(left=0, right=0),
                                        content=ft.ResponsiveRow(
                                            controls=[
                                                ft.Column(col={"xs":12},controls=[self.result])                                                                                    
                                            ]                                        
                                        )                                    
                                    ),
                                    ft.Container(
                                        padding=padding.only(left=20, right=20),
                                        content=ft.ResponsiveRow(
                                            controls=[
                                                ft.Column(col={"xs":12},controls=[self.result2])                                                                                    
                                            ]                                        
                                        )                                    
                                    )  
                                ]   
                            )
                        ) 
                    ]
                )    
            ]
        )    
    def de (self,e):       
        self.a.value = ""
        self.b.value = ""
        self.c.value = ""  
        self.d.value = ""       
        self.result.value = ""            
        self.result2.value = ""       
        self.update()        
             
    def calc(self,e):        
        self.result.size=19
        self.result2.size=24
        choice_a= float(self.a.value)
        choice_b= float(self.b.value)
        choice_c= float(self.c.value)  
        choice_d= float(self.d.value)         
        if (choice_a != 0): 
            roots = np.roots([choice_a, choice_b, choice_c, choice_d])
            self.result.value = str("Pt: {0}x³ + {1}x² + {2}x + {3} = 0".format(choice_a,choice_b,choice_c,choice_d) + " có các nghiệm: ")
            self.result2.value = str(roots)             
        else:
            self.result.value = str ("Không phải phương trình Bậc 3")        
        self.update()     
        