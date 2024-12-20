import flet as ft
from flet import *

class DataTable(ft.Container):
    def __init__(self):
        super().__init__()    
        self.width = 350        
        self.border_radius = border_radius.only(top_left=30, top_right=30, bottom_left=15, bottom_right=15)        
        self.bgcolor = "#089908"        
        self.page = ft.Page
        self.padding = padding.only(top=44, left=14, right=14, bottom=17)         
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
                                        ft.Column(col={"xs":12}, controls=[ ft.Text("BẢNG SỐ LIỆU THAM KHẢO", size=18, color="#FFFFFF", weight=ft.FontWeight.W_600)])                                
                                    ]                                        
                                )       
                            )                                                                                                                               
                        ]                                                                                          
                    )                                                           
                ),  
                ft.Container(                  
                    bgcolor="#ffffff",      
                    border_radius=10,
                    padding = 5,                    
                    content=ft.Column(
                        controls=[
                            ft.Container(
                                padding=padding.only(left=10, right=10),
                                content=ft.ResponsiveRow(                                
                                    controls=[
                                        ft.Row(controls=[ft.Text("", size=0)]),                                        
                                        ft.Row(controls=[ft.Text("", size=0)]),      
                                        ft.ResponsiveRow(
                                            controls=[                                               
                                                ft.Column(col={"xs": 12}, controls=[ft.Text("1. CHỈ SỐ KHỐI CƠ THỂ", size=17, weight=ft.FontWeight.W_700)])  
                                            ]
                                        ),                                   
                                        ft.Column(col={"xs":12}, controls=[ft.Image(src=f"/image/bmi.png")]),      
                                        ft.Row(controls=[ft.Text("", size=0)]),                                        
                                        ft.Row(controls=[ft.Text("", size=0)]), 
                                        ft.Row(controls=[ft.Text("", size=0)]),   
                                        ft.ResponsiveRow(
                                            controls=[
                                                ft.Column(col={"xs":12},controls=[ft.Divider( color="#0080ff")])  
                                            ]
                                        ),
                                        ft.Row(controls=[ft.Text("", size=0)]),                                        
                                        ft.Row(controls=[ft.Text("", size=0)]), 
                                        ft.Row(controls=[ft.Text("", size=0)]),    
                                        ft.ResponsiveRow(
                                            controls=[                                               
                                                ft.Column(col={"xs": 12}, controls=[ft.Text("2. KHẨU PHẦN ĂN DINH DƯỠNG", size=17, weight=ft.FontWeight.W_700)])  
                                            ]
                                        ),                                                                              
                                        ft.Row(controls=[ft.Text("", size=0)]), 
                                        ft.Row(controls=[ft.Text("", size=0)]),                                              
                                        ft.ResponsiveRow(
                                            controls=[
                                                ft.Column(col={"xs":12},controls=[ft.Image(src=f"/image/rau-cu-nhieu-mau-sac.png")]) 
                                            ]
                                        ),
                                        ft.Row(controls=[ft.Text("", size=0)]),     
                                        ft.ResponsiveRow(                                            
                                            controls=[                                                 
                                                ft.Column(col={"xs": 12}, controls=[ft.Text("Kết hợp nhiều loại thực phẩm trong chế độ dinh dưỡng của bạn.", size=16, weight=ft.FontWeight.W_500)])  
                                            ]
                                        ),
                                        ft.Row(controls=[ft.Text("", size=0)]),                                        
                                        ft.Row(controls=[ft.Text("", size=0)]), 
                                        ft.Row(controls=[ft.Text("", size=0)])                                       
                                    ]
                                )
                            )                                      
                        ], height=380, scroll=ft.ScrollMode.ALWAYS
                    )
                )          
            ]
        )                
