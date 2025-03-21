import flet as ft

import allFunc

def main(page: ft.Page):
    page.title = "Шишички"
    page.window.width = 600
    page.window.height = 600
    page.window.center()
    page.window.full_screen = False
    page.window.resizable = False
    page.window.maximizable = False
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER


    desk_info = allFunc.desk_builder()
    desk = desk_info[0]
    white_checkers = desk_info[1]
    black_checkers = desk_info[2]
    

    page.add(
        ft.Container(
            content=ft.Stack(
                desk,
                width=500,
                height=500
            ),
            alignment=ft.alignment.center,
            expand=True
        )
    )

ft.app(main)
