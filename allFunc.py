import flet as ft


class GreenMoves():
    height = 62.5,
    width = 62.5,
    bgcolor = 'Green',


white_checkers_list = []
black_checkers_list = []
checkers_list = []

def checkers_builder(desk, page):
    global checkers_list
    checkers_list.append(desk)
    for i in range(0, 3):
        match i:
            case 1:
                for i2 in range(0, 4):
                    checkers_list.append(
                        ft.Container(
                            content=ft.Image(
                                src="images/whitePl.png",
                                fit=ft.ImageFit.COVER,
                            ),
                            height=62.5,
                            width=62.5,
                            top=62.5 * i,
                            left=62.5 * (i2*2),
                            data = [62.5, 62.5 * (i2*2)],
                            on_click=lambda e: moves_white(e)
                        )
                    )
                    make_white_checkers_list([62.5, 62.5 * (i2*2)])
                    checkers_list.append(
                        ft.Container(
                            content=ft.Image(
                                src="images/blackPL.png",
                                fit=ft.ImageFit.COVER
                            ),
                            height=62.5,
                            width=62.5,
                            bottom=62.5 * i,
                            right=62.5 * (i2*2),
                            data = [500 - 62.5 * i, 500 - 62.5 * (i2*2)],
                            on_click=lambda e: moves_white(e)
                        )
                    )
                    make_black_checkers_list([500 - 62.5 * i, 500 - 62.5 * (i2*2)])
            case _:
                for i2 in range(0, 4):
                    checkers_list.append(
                        ft.Container(
                            content=ft.Image(
                                src="images/whitePl.png",
                                fit=ft.ImageFit.COVER
                            ),
                            height=62.5,
                            width=62.5,
                            top=62.5 * i,
                            left=62.5 * (i2*2 + 1),
                            data = [62.5 * i, 62.5 * (i2*2+1)],
                            on_click=lambda e: moves_white(e)
                        )
                    )
                    make_white_checkers_list([62.5 * i, 62.5 * (i2*2+1)])
                    checkers_list.append(
                        ft.Container(
                            content=ft.Image(
                                src="images/blackPL.png",
                                fit=ft.ImageFit.COVER
                            ),
                            height=62.5,
                            width=62.5,
                            bottom=62.5 * i,
                            right=62.5 * (i2*2 + 1),
                            data = [500 - 62.5 * i, 500 - 62.5 * (i2*2+1)],
                            on_click=lambda e: moves_white(e)
                        )
                    )
                    make_black_checkers_list([500 - 62.5 * i, 500 - 62.5 * (i2*2+1)])
        
    return checkers_list


def make_white_checkers_list(coordinates):
    global white_checkers_list
    white_checkers_list.append(coordinates)


def make_black_checkers_list(coordinates):
    global black_checkers_list
    black_checkers_list.append(coordinates)

def moves_white(e):
    print(e.control.data)

def moves_black(e):
    print(e.control.data)
    