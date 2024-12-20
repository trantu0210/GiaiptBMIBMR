import flet as ft
from flet import *

class BMRcalculator(ft.Container):
    def __init__(self):
        super().__init__()        
        self.width = 350      
        self.border_radius = border_radius.only(top_left=30, top_right=30, bottom_left=10, bottom_right=10)   
        self.page = ft.Page       
        self.bgcolor = "#089908"  
        self.padding = padding.only(top=44, left=10, right=10, bottom=12)                   
        self.weight =TextField(label="Cân nặng",hint_text="kg",content_padding=padding.Padding(left=10, right=10, top=0, bottom=0))        
        self.height=TextField(label="Chiều cao",hint_text="cm",content_padding=padding.Padding(left=10, right=10, top=0, bottom=0))        
        self.gender=TextField(label="Giới tính",hint_text="Nam/Nữ",content_padding=padding.Padding(left=10, right=10, top=0, bottom=0))
        self.old=TextField(label="Tuổi",hint_text="Tuổi",content_padding=padding.Padding(left=10, right=10, top=0, bottom=0))        
        self.move = ft.Dropdown(
            width=300,
            content_padding=padding.Padding(left=10, right=10, top=0, bottom=0),
            text_size=15,
            label="Vận động",
            hint_text="Vận động",
            options=[
                ft.dropdown.Option("Ít hoặc không tập thể dục"),
                ft.dropdown.Option("Tập thể dục nhẹ 1-3 ngày/tuần"),
                ft.dropdown.Option("Tập thể dục vừa 3-5 ngày/tuần"),
                ft.dropdown.Option("Tập thể dục nặng 6-7 ngày/tuần"),
                ft.dropdown.Option("Tập thể dục rất nặng 2 lần/ngày")          
            ], autofocus=True
        )     
        self.result=Text("", color="#333333", weight=ft.FontWeight.BOLD)
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
                                        ft.Column(col={"xs":12}, controls=[ ft.Text("KIỂM TRA CHỈ SỐ BMR + TDEE", size=18, color="#FFFFFF", weight=ft.FontWeight.W_600)])                                        
                                    ]                                        
                                )       
                            )                                                                                                  
                        ]                                                                                          
                    )                                                           
                ), 
                ft.Column(
                    height=440,
                    scroll=ft.ScrollMode.ALWAYS,                    
                    controls=[
                        ft.Container(                  
                            bgcolor="#ffffff",      
                            border_radius=0,
                            padding = padding.only(left=10, right=10, top=20, bottom=20),                
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
                                    ft.ResponsiveRow(controls=[
                                        ft.Column(col={"xs": 12}, controls=[self.gender]),   
                                    ]),   
                                    ft.Row(controls=[ft.Text("", size=0)]),
                                    ft.ResponsiveRow(controls=[
                                        ft.Column(col={"xs": 12}, controls=[self.old]),   
                                    ]),  
                                    ft.Row(controls=[ft.Text("", size=0)]),
                                    ft.ResponsiveRow(controls=[
                                        ft.Column(col={"xs": 12}, controls=[self.move]),   
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
                                        padding=padding.only(left=20, right=20),
                                        content=ft.ResponsiveRow(
                                            controls=[
                                                ft.Column(col={"xs":2},controls=[ft.Icon(name=ft.icons.HOME_ROUNDED, size=0)]),                                             
                                                ft.Column(col={"xs":10},controls=[self.result])                                                                                    
                                            ]                                        
                                        )                                           
                                    ),
                                    ft.Container(
                                        padding=padding.only(left=20, right=20),
                                        content=ft.ResponsiveRow(
                                            controls=[
                                                ft.Column(col={"xs":2},controls=[ft.Icon(name=ft.icons.HOME_ROUNDED, size=0)]),                                             
                                                ft.Column(col={"xs":10},controls=[self.result2])                                                                                    
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
        self.weight.value = ""
        self.height.value = ""
        self.old.value = ""
        self.gender.value = ""
        self.move.value = ""
        self.result2.value = ""
        self.result.value = ""        
        self.update()    

    def calc(self,e):        
        self.result.size=24  
        self.result2.size = 24
        choice_gender = str(self.gender.value)   
        bmr_nam = (10 * float(self.weight.value)) + (6.25 * float(self.height.value)) - (5 * int(self.old.value)) + 5
        bmr_nu  = (10 * float(self.weight.value)) + (6.25 * float(self.height.value)) - (5 * int(self.old.value)) - 161
        if choice_gender == "Nam" or choice_gender == "nam" or choice_gender == "NAM":
            b_nam = round(float(bmr_nam))
            if self.move.value == "Ít hoặc không tập thể dục":        
                self.result.value = str("BMR = ") + str(b_nam)       
                self.result2.value = str("TDEE = ") + str(round(b_nam * 1.2))
            elif self.move.value == "Tập thể dục nhẹ 1-3 ngày/tuần":        
                self.result.value = str("BMR = ") + str(b_nam)                   
                self.result2.value =  str("TDEE = ") + str(round(b_nam * 1.375))
            elif self.move.value == "Tập thể dục vừa phải 3-5 ngày/tuần": 
                self.result.value = str("BMR = ") + str(b_nam)                
                self.result2.value =  str("TDEE = ") + str(round(b_nam * 1.55))
            elif self.move.value == "Tập thể dục nặng 6-7 ngày/tuần":  
                self.result.value = str("BMR = ") + str(b_nam)              
                self.result2.value =  str("TDEE = ") + str(round(b_nam * 1.725))
            elif self.move.value == "Tập thể dục rất nặng 2 lần/ngày":   
                self.result.value = str("BMR = ") + str(b_nam)            
                self.result2.value =  str("TDEE = ") + str(round(b_nam * 1.9))     
        else:
            b_nu = round(float(bmr_nu))
            if self.move.value == "Ít hoặc không tập thể dục":      
                self.result.value = str("BMR = ") + str(b_nu)           
                self.result2.value =  str("TDEE = ") + str(round(b_nu * 1.2))
            elif self.move.value == "Tập thể dục nhẹ 1-3 ngày/tuần":  
                self.result.value = str("BMR = ") + str(b_nu)                        
                self.result2.value =  str("TDEE = ") + str(round(b_nu * 1.375))
            elif self.move.value == "Tập thể dục vừa phải 3-5 ngày/tuần":  
                self.result.value = str("BMR = ") + str(b_nu)             
                self.result2.value =  str("TDEE = ") + str(round(b_nu * 1.55))
            elif self.move.value == "Tập thể dục nặng 6-7 ngày/tuần":  
                self.result.value = str("BMR = ") + str(b_nu)            
                self.result2.value =  str("TDEE = ") + str(round(b_nu * 1.725))
            elif self.move.value == "Tập thể dục rất nặng 2 lần/ngày":   
                self.result.value = str("BMR = ") + str(b_nu)          
                self.result2.value =  str("TDEE = ") + str(round(b_nu * 1.9))          
        self.update()         
