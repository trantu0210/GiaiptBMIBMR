import flet as ft
from flet import *

class BMIcalculator(ft.Container):
    def __init__(self):
        super().__init__()    
        self.width = 350        
        self.border_radius = border_radius.only(top_left=30, top_right=30, bottom_left=20, bottom_right=20)        
        self.bgcolor = "#089908"        
        self.page = ft.Page
        self.padding = padding.only(top=44, left=14, right=14, bottom=15)    
        self.weight =TextField(label="Cân nặng",hint_text="kg")        
        self.height=TextField(label="Chiều cao",hint_text="cm")       
        self.result=Text("", color="#444444",weight=ft.FontWeight.BOLD)
        self.result2 = Text("", color="#f24b0c", weight=ft.FontWeight.BOLD)        
        self.content = ft.Column(
            controls=[  
                ft.Container(
                    width=350,
                    content=ft.Column(
                        controls=[ 
                            ft.Container(
                                padding=padding.only(left=10, right=10),
                                content=ft.ResponsiveRow(
                                    controls=[
                                        ft.Column(col={"xs":12}, controls=[ ft.Text("KIỂM TRA CHỈ SỐ BMI ONLINE", size=18, color="#FFFFFF", weight=ft.FontWeight.W_600)])                                                                 
                                    ]                                        
                                )       
                            )                                                                                                   
                        ]                                                                                          
                    )                                                           
                ),  
                ft.Container(                  
                    bgcolor="#ffffff",      
                    border_radius=20,
                    padding = 20,                    
                    content=ft.Column(
                        controls=[              
                            ft.Row(controls=[ft.Text("", size=0)]),
                            ft.ResponsiveRow(controls=[
                                ft.Column(col={"xs": 12}, controls=[self.weight]),   
                            ]),
                            ft.Row(controls=[ft.Text("", size=0)]),                            
                            ft.ResponsiveRow(controls=[
                                ft.Column(col={"xs": 12}, controls=[self.height]),   
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
                            ft.Container(
                                padding=padding.only(left=25, right=25),
                                content=ft.ResponsiveRow(
                                    controls=[
                                        ft.Column(col={"xs":3},controls=[ft.Icon(name=ft.icons.HOME_ROUNDED, size=0)]),                                             
                                        ft.Column(col={"xs":9},controls=[self.result])                                                                                    
                                    ]                                        
                                )                                    
                            ),
                            ft.Container(
                                padding=padding.only(left=25, right=25),
                                content=ft.ResponsiveRow(
                                    controls=[
                                        ft.Column(col={"xs":2},controls=[ft.Icon(name=ft.icons.HOME_ROUNDED, size=0)]),                                             
                                        ft.Column(col={"xs":10},controls=[self.result2])                                                                                    
                                    ]                                        
                                )                                    
                            )
                            
                        ],height=350, scroll=ft.ScrollMode.ALWAYS
                    )
                )      
            ]
        )
    
    def de (self,e):
        self.weight.value = ""
        self.height.value = ""      
        self.result2.value = ""
        self.result.value = ""        
        self.update()     
                
    def calc(self,e):        
        self.result.size=34
        self.result.value= str ("%.2f" %(  float(self.weight.value)/(float(self.height.value)*0.01)**2))         
        choice = float(self.result.value)
        if choice < 18.5:
            self.result2.value = str("GẦY, THIẾU CÂN")
            self.result2.size = 19
        elif choice >= 18.5 and choice <= 24.9:
            self.result2.value = str("BÌNH THƯỜNG")
            self.result2.size = 19
        elif choice >= 25.0 and choice <= 29.9:
            self.result2.value = str("  THỪA CÂN")
            self.result2.size = 19
        elif choice >= 30.0 and choice <= 39.9:
            self.result2.value = str("   BÉO PHÌ")
            self.result2.size = 20
        elif choice >= 40.0:
            self.result2.value = str("   BỆNH TẬT")
            self.result2.size = 19      
        self.update()         
