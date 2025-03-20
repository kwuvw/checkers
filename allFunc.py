import flet as ft


def checkers_builder(desk):
    checkers_list = []
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
                            on_click=moves
                        )
                    )
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
                            on_click=moves
                        )
                    )
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
                            on_click=moves
                        )
                    )
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
                            on_click=moves
                        )
                    )
        
    return checkers_list


def moves(e):
    print(e.control.data)