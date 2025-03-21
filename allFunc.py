import flet as ft


class GreenMoves():
    height = 62.5,
    width = 62.5,
    bgcolor = 'Green',


white_checkers_list = []
black_checkers_list = []
desk_list = []

def desk_builder():
    global desk_list
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
                    alignment=ft.alignment.center
                )
            )
            if (i%2 == 0 and i2%2 == 1) or (i%2 == 1 and i2%2 == 0):
                if i in [7, 6, 5]:
                    white_checkers_list.append([62.5*i, 62.5*i2])
                elif i in [0, 1, 2]:
                    black_checkers_list.append([62.5*i, 62.5*i2])
    return (desk_list, white_checkers_list, black_checkers_list)
