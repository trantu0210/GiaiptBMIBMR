import flet as ft
from flet import *

class Bac1(ft.Container):
    def __init__(self):
        super().__init__()        
        self.width = 350        
        self.border_radius = border_radius.only(top_left=30, top_right=30, bottom_left=20, bottom_right=20)       
        self.bgcolor = "#089908"  
        self.padding = padding.only(top=44, left=14, right=14, bottom=14)     
        self.a =TextField(label="Nhập a",hint_text="a")        
        self.b=TextField(label="Nhập b",hint_text="b")
        self.c=TextField(label="Nhập c",hint_text="c")   
        self.result=Text("", color="#333333", weight=ft.FontWeight.BOLD)
        self.result2=Text("", color="#f24b0c", weight=ft.FontWeight.BOLD)        
        self.content = ft.Column(
            controls=[       
                ft.Container(
                    width=350,
                    content=ft.Column(
                        controls=[ 
                            ft.Container(
                                padding=padding.only(left=20, right=20),
                                content=ft.ResponsiveRow(
                                    controls=[                                                                         
                                        ft.Column(col={"xs":12}, controls=[ ft.Text("Giải pt Bậc 1: Ax+ B = C", size=20, color="#FFFFFF", weight=ft.FontWeight.W_600)])                                                                   
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
                                        padding=padding.only(left=5, right=5),
                                        content=ft.ResponsiveRow(
                                            controls=[
                                                ft.Column(col={"xs":12},controls=[self.result2])                                                                                    
                                            ]                                        
                                        )                                    
                                    ),
                                    ft.Row(controls=[ft.Text("", size=0)]), 
                                    ft.Row(controls=[ft.Text("", size=0)]) 
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
        self.result.value = ""            
        self.result2.value = ""       
        self.update()      
               
    def calc(self,e):        
        self.result.size=18
        self.result2.size=22
        choice_a= float(self.a.value)
        choice_b= float(self.b.value)
        choice_c= float(self.c.value)      
        if (choice_a != 0):      
            if choice_b > 0:
                x = float((choice_c - choice_b) / choice_a)              
                self.result.value = str("Phương trình {0}x + {1} = {2}".format(choice_a,choice_b,choice_c) + " có nghiệm: ")
                self.result2.value = str(" x= " + str("%.2f" %(x)) )         
            elif choice_b < 0:
                y = float((choice_c + (choice_b * -1)) / choice_a)
                self.result.value = str("Phương trình {0}x + {1} = {2}".format(choice_a,choice_b,choice_c) + " có nghiệm: ")    
                self.result2.value = str(" x= " + str("%.2f" %(y)))
        elif (choice_a == 0):
            if (choice_b - choice_c != 0): 
                self.result.value = str("Phương trình {0}x + {1} = {2}".format(choice_a,choice_b,choice_c))
                self.result2.value = str(" Pt vô nghiệm")
            elif (choice_b - choice_c == 0):
                self.result.value = str("Phương trình {0}x + {1} = {2}".format(choice_a,choice_b,choice_c))
                self.result2.value = str(" Pt vô số nghiệm")                 
        self.update()         
