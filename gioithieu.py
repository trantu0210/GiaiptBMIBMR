import flet as ft 
from flet import *

class Gioithieu(ft.Container):
    def __init__(self):
        super().__init__()        
        self.width = 350        
        self.border_radius = border_radius.only(top_left=30, top_right=30, bottom_left=10, bottom_right=10)        
        self.bgcolor = "#089908"        
        self.page = ft.Page
        self.padding = padding.only(top=44, left=14, right=14, bottom=15)   
        self.text1 = ft.Text("BMI hay còn gọi là chỉ số khối cơ thể, được sử dụng để đo lượng mỡ trong cơ thể, được tính dựa trên trọng lượng và chiều cao, áp dụng cho nam và nữ trưởng thành.", color=ft.colors.BLACK, italic=True      
        )
        self.text2 = ft.Text("BMR là tỷ lệ trao đổi chất cơ bản trong cơ thể, cho biết số lượng calo tối thiểu mà cơ thể cần để duy trì các chức năng cơ bản (thở, tuần hoàn máu..) ở trạng thái nghỉ ngơi hoàn toàn.", color=ft.colors.BLACK, italic=True       
        )
        self.text3 = ft.Text("TDEE là tổng năng lượng (calo) mà cơ thể tiêu thụ trong một ngày bao gồm những hoạt động thể chất như: đi bộ, luyện tập thể dục, làm việc và các chức năng cơ bản như: tuần hoàn máu, tiêu hoá, hít thở..", color=ft.colors.BLACK, italic=True      
        )
        self.text4 = ft.Text("Chỉ số TDEE cho biết nhu cầu năng lượng mỗi ngày của cơ thể, giúp kiểm soát cân nặng, điều chỉnh chế độ dinh dưỡng và tập luyện phù hợp.", color=ft.colors.BLACK, italic=True        
        )      
        self.content = ft.Column(            
            controls=[    
                ft.Container(                    
                    content=ft.Column(
                        controls=[ 
                            ft.Container(
                                padding=padding.only(left=15, right=15),
                                content=ft.ResponsiveRow(
                                    controls=[
                                        ft.Column(col={"xs":12}, controls=[ft.Text("CHỈ SỐ KIỂM TRA SỨC KHOẺ", size=18, color="#FFFFFF", weight=ft.FontWeight.W_600)])                                                                                                               
                                    ]                                        
                                )       
                            )                                                                                                  
                        ]                                                                                          
                    )                                                           
                ),                                                      
                ft.Container(                  
                    bgcolor="#ffffff",      
                    border_radius=20,
                    padding = padding.only(top=20, left=20, right=7, bottom=20),                                       
                    content=ft.Column(
                        controls=[   
                            ft.ResponsiveRow(controls=[
                                ft.Column(col={"xs": 12}, controls=[ft.Text("1. BMI (Body Mass Index)", size=18, weight=ft.FontWeight.W_600)]),   
                            ]),
                            ft.ResponsiveRow(controls=[
                                ft.Column(col={"xs": 12}, controls=[self.text1]),   
                            ]),
                            ft.ResponsiveRow(controls=[
                                ft.Column(col={"xs": 12}, controls=[ft.Text("2. BMR (Basal Metabolic Rate)", size=18, weight=ft.FontWeight.W_600)]),   
                            ]),
                            ft.ResponsiveRow(controls=[
                                ft.Column(col={"xs": 12}, controls=[self.text2]),   
                            ]),
                            ft.ResponsiveRow(controls=[
                                ft.Column(col={"xs": 12}, controls=[ft.Text("3. TDEE (Total Daily Energy Expenditure)", size=18, weight=ft.FontWeight.W_600)]),   
                            ]),
                            ft.ResponsiveRow(controls=[
                                ft.Column(col={"xs": 12}, controls=[self.text3]),   
                            ]),
                            ft.ResponsiveRow(controls=[
                                ft.Column(col={"xs": 12}, controls=[self.text4]),   
                            ]),
                            ft.Row(controls=[ft.Text("", size=0)]),
                            ft.Row(controls=[ft.Text("", size=0)])                                                                                                      
                        ],height=400, scroll=ft.ScrollMode.ALWAYS
                    )
                )            
            ]            
        )      
     