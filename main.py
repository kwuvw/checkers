import flet as ft

import allFunc

is_clicked_on_checker = False
clicked_checker_info: list
white_checkers_list = []
black_checkers_list = []
desk_list = []

def main(page: ft.Page):
    global desk_list
    page.title = "Шишички"
    page.window.width = 600
    page.window.height = 600
    page.window.center()
    page.window.full_screen = False
    page.window.resizable = False
    page.window.maximizable = False
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def click_on_checker(e):
        global is_clicked_on_checker, clicked_checker_info
        is_clicked_on_checker = True
        clicked_checker_info = e.control.data

    def click_on_desk(e):
        global is_clicked_on_checker, clicked_checker_info
        if is_clicked_on_checker:
            is_clicked_on_checker = False
            if e.control.data in white_checkers_list or e.control.data in black_checkers_list:
                return
            else:
                if clicked_checker_info in white_checkers_list:
                    print(e.control.data)
                    print(clicked_checker_info)
                    print("w")
                    page.controls.clear()
                    page.add(
                        ft.Stack(
                            desk_list
                        )
                    )
                    page.update() 
                elif clicked_checker_info in black_checkers_list:
                    print(e.control.data)
                    print(clicked_checker_info)
                    print("b")
                    page.controls.clear()
                    page.add(
                        ft.Stack(
                            desk_list
                        )
                    )
                    page.update() 

    def desk_builder():
        global white_checkers_list, black_checkers_list, desk_list
        for i in range(0, 8):
            for i2 in range(0, 8):
                desk_list.append(
                    ft.Container(
                        bgcolor="white" if i%2 == 0 and i2%2 == 0 else "white" if i%2 == 1 and i2%2 == 1 else "black",
                        content=None if i%2 == 0 and i2%2 == 0 else None if i%2 == 1 and i2%2 == 1 else ft.Image(src='images/whitePl.png') if i in [7, 6, 5] else ft.Image(src='images/BlackPl.png') if i in [0, 1, 2] else None,
                        height=62.5,
                        width=62.5,
                        top=62.5*i,
                        left=62.5*i2,
                        data=[62.5*i, 62.5*i2],
                        alignment=ft.alignment.center,
                        on_click=click_on_desk if i%2 == 0 and i2%2 == 0 else click_on_desk if i%2 == 1 and i2%2 == 1 else click_on_checker if i in [7, 6, 5] else click_on_checker if i in [0, 1, 2] else click_on_desk,
                    )
                )
                if (i%2 == 0 and i2%2 == 1) or (i%2 == 1 and i2%2 == 0):
                    if i in [7, 6, 5]:
                        white_checkers_list.append([62.5*i, 62.5*i2])
                    elif i in [0, 1, 2]:
                        black_checkers_list.append([62.5*i, 62.5*i2])
    desk_builder()

    page.add(
        ft.Container(
            content=ft.Stack(
                desk_list,
                width=500,
                height=500
            ),
            alignment=ft.alignment.center,
            expand=True
        )
    )


ft.app(main)
