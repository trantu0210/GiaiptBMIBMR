import flet as ft
from flet import *

class Hept_Haian(ft.Container):
    def __init__(self):
        super().__init__()        
        self.width = 350        
        self.border_radius = border_radius.only(top_left=30, top_right=30, bottom_left=10, bottom_right=10)       
        self.bgcolor = "#089908"  
        self.padding = padding.only(top=44, left=14, right=14, bottom=14)    
        self.a1 =TextField(label="Nhập a1",hint_text="a1",content_padding=padding.Padding(left=10, right=10, top=0, bottom=0))        
        self.b1=TextField(label="Nhập b1",hint_text="b1",content_padding=padding.Padding(left=10, right=10, top=0, bottom=0))        
        self.c1=TextField(label="Nhập c1",hint_text="c1",content_padding=padding.Padding(left=10, right=10, top=0, bottom=0))
        self.a2 =TextField(label="Nhập a2",hint_text="a2",content_padding=padding.Padding(left=10, right=10, top=0, bottom=0))        
        self.b2=TextField(label="Nhập b2",hint_text="b2",content_padding=padding.Padding(left=10, right=10, top=0, bottom=0))        
        self.c2=TextField(label="Nhập c2",hint_text="c2",content_padding=padding.Padding(left=10, right=10, top=0, bottom=0))             
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
                                        ft.Column(col={"xs":12}, controls=[ ft.Text("GIẢI HỆ PT BẬC NHẤT 2 ẨN", size=18, color="#FFFFFF", weight=ft.FontWeight.W_600)]) 
                                    ]                                        
                                )       
                            )                                                                                                  
                        ]                                                                                          
                    )                                                           
                ),   
                ft.Column(
                    height=430,
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
                                        ft.Column(col={"xs": 12}, controls=[self.a1]),   
                                    ]),  
                                    ft.Row(controls=[ft.Text("", size=0)]), 
                                    ft.ResponsiveRow(controls=[
                                        ft.Column(col={"xs": 12}, controls=[self.b1]),   
                                    ]),    
                                    ft.Row(controls=[ft.Text("", size=0)]), 
                                    ft.ResponsiveRow(controls=[
                                        ft.Column(col={"xs": 12}, controls=[self.c1]),   
                                    ]),  
                                    ft.Row(controls=[ft.Text("", size=0)]),                                    
                                    ft.ResponsiveRow(controls=[
                                        ft.Column(col={"xs": 12}, controls=[self.a2]),   
                                    ]),  
                                    ft.Row(controls=[ft.Text("", size=0)]), 
                                    ft.ResponsiveRow(controls=[
                                        ft.Column(col={"xs": 12}, controls=[self.b2]),   
                                    ]), 
                                    ft.Row(controls=[ft.Text("", size=0)]),    
                                    ft.ResponsiveRow(controls=[
                                        ft.Column(col={"xs": 12}, controls=[self.c2]),   
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
                                        padding=padding.only(left=10, right=10),
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
        self.a1.value = ""
        self.b1.value = ""
        self.c1.value = ""  
        self.a2.value = ""
        self.b2.value = ""
        self.c2.value = ""       
        self.result.value = ""            
        self.result2.value = ""       
        self.update()             
    def calc(self,e):        
        self.result.size=20
        self.result2.size=23
        choice_a1= float(self.a1.value)
        choice_b1= float(self.b1.value)
        choice_c1= float(self.c1.value)    
        choice_a2= float(self.a2.value)
        choice_b2= float(self.b2.value)
        choice_c2= float(self.c2.value)  
        DT = (choice_a1 * choice_b2) - (choice_b1 * choice_a2)
        DTx = (choice_c1 * choice_b2) - (choice_b1 * choice_c2) 
        DTy = (choice_a1 * choice_c2) - (choice_a2 * choice_c1)
        if (DT != 0):   
            self.result.value = str("Hệ pt: {0}x + {1}y = {2} ; {3}x + {4}y = {5} ".format(choice_a1,choice_b1,choice_c1,choice_a2,choice_b2,choice_c2) + " có 1 nghiệm: ")  
            self.result2.value = str("x= " + str("%.2f" %(DTx/DT)) + " ; " + "y= " + str("%.2f" %(DTy/DT)))
        else:
            if DTx != 0 or DTy != 0:
                self.result.value = str("Hệ pt: {0}x + {1}y = {2} ; {3}x + {4}y = {5} ".format(choice_a1,choice_b1,choice_c1,choice_a2,choice_b2,choice_c2))             
                self.result2.value = str("Hệ pt vô nghiệm")
            else:
                self.result.value = str("Hệ pt: {0}x + {1}y = {2} ; {3}x + {4}y = {5} ".format(choice_a1,choice_b1,choice_c1,choice_a2,choice_b2,choice_c2))            
                self.result2.value = str("Hệ pt vô số nghiệm")           
        self.update()         
