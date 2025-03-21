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

    desk = ft.Container(
        content=ft.Image(
            src="images/desk.png",
            width=500,
            height=500,
            fit=ft.ImageFit.COVER,
        ),
        height=500,
        width=500,
        alignment=ft.alignment.center,
    )

    checkers_list = allFunc.checkers_builder(desk, page)
    

    page.add(
        ft.Stack(
            checkers_list,

        )
    )

ft.app(main)
