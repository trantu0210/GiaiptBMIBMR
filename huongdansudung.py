import flet as ft 
from flet import *

class Huongdansudung(ft.Container):
    def __init__(self):
        super().__init__()        
        self.width = 350   
        self.border_radius = border_radius.only(top_left=30, top_right=30, bottom_left=15, bottom_right=15)        
        self.bgcolor = "#089908"        
        self.padding = padding.only(top=44, left=14, right=14, bottom=17)            
        userguide = '''          
        5² = 25               BẤM  5 -> A²
        4³ = 64               BẤM  4 -> A³           
        √4 = 2                BẤM  4 -> √A
        ∛8 = 2                BẤM  8 -> ∛A

        2^4 = 16      
        BẤM  2 -> Aᴮ -> 4

        6% = 0.06       
        BẤM  6 -> %

        sin(30) = 0.5
        BẤM: 30 -> sinx -> =

        cos(60) = 0.5
        BẤM: 60 -> cosx -> =        

        UCLN(10,20,30) = 10
        BẤM: 10 UCLN 20 UCLN 30 = 10 
          
        BCNN(12,24,30) = 120
        BẤM: 12 BCNN 24 BCNN 30 = 120       
          
        4/5 = 0.8    
        BẤM 4 -> A/B -> 5  

        0.6 = 3/5     
        BẤM 0.6 -> >A/B 

        0.25 = 1/4
        BẤM 4 -> 1/x -> =

        5! = 120        
        BẤM 5 -> n! 

        e^3 = 20.0855           
        BẤM: 3 -> e^ -> =

        ln(6) = 1.79175947
        BẤM: 6 -> lnx -> =

        log2(7) = 2.80735
        BẤM: 7 -> log2(x) -> =        

        log3(27) = 3
        BẤM: 3 -> logb(x) -> 27 -> =          

        10C5 = 252
        BẤM: 10 -> nCr -> 5 -> =   
      
        7P4 = 840  
        BẤM: 7 -> nPr -> 4 -> =

        ** VÍ DỤ GIẢI PT BẬC NHẤT 1 ẨN:
        2x + 3 = 0                  
        -> Kết quả: x=-1.5

        ** VÍ DỤ GIẢI PT BẬC HAI 1 ẨN:
        x² - 8x + 12 = 0                          
        -> Kết quả: x=2 ; x=6

        ** VÍ DỤ GIẢI PT BẬC BA 1 ẨN:
        x³ -6x² + 11x - 6 = 0                          
        -> Kết quả: [1. 2. 3.]

        ** VÍ DỤ GIẢI PT BẬC BỐN 1 ẨN:
        x⁴ -5x² + 4 = 0                          
        -> Kết quả: [-2. 2. -1. 1.]

        ** VÍ DỤ HỆ PT BẬC NHẤT 2 ẨN:
        2x + y = 3
        x - y = 6       
           -> Kết quả: x=3; y =-3

        ** VÍ DỤ HỆ PT BẬC NHẤT 3 ẨN:
        2x + y - z  = 8
        -3x - y + 2z = -11
        -2x + y + 2z = -3
           -> Kết quả: [2. 3. -1.]
        '''  
        self.content = ft.Column(
            controls=[   
                ft.Container(                    
                    content=ft.Column(
                        controls=[ 
                            ft.Container(
                                padding=padding.only(left=20, right=20),
                                content=ft.ResponsiveRow(
                                    controls=[
                                        ft.Column(col={"xs":12}, controls=[ ft.Text("HƯỚNG DẪN SỬ DỤNG APP", size=18, color="#FFFFFF", weight=ft.FontWeight.W_600)])                                                                                                            
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
                            ft.ResponsiveRow(controls=[
                                ft.Column(col={"xs": 12}, controls=[ft.Text(userguide)])]),
                                ft.Row(controls=[ft.Text("", size=0)])                            
                        ],height=400,scroll=ft.ScrollMode.ALWAYS
                    )
                )   
            ]
        )   
        