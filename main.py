import flet as ft

is_clicked_on_checker = False
clicked_checker_info: list
desk_list: list = []
white_checkers_list: list = []
black_checkers_list: list = []
white_checkers_coordinates_list: list = []
black_checkers_coordinates_list: list = []


def main(page: ft.Page):
    global desk_list, white_checkers_list, black_checkers_list, white_checkers_coordinates_list, black_checkers_coordinates_list
    page.title = "Шишички"
    page.window.width = 600
    page.window.height = 600
    page.window.center()
    page.window.full_screen = False
    page.window.resizable = False
    page.window.maximizable = False
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER


    def desk_builder():
        global desk_list, white_checkers_list, black_checkers_list, white_checkers_coordinates_list, black_checkers_coordinates_list
        index_in_desk_list = -1
        index_in_white_checkers_list = -1
        index_in_black_checkers_list = -1
        for i in range(0, 8):
            for i2 in range(0, 8):
                index_in_desk_list += 1
                desk_list.append(
                    ft.Container(
                        bgcolor="white" if i%2 == 0 and i2%2 == 0 else "white" if i%2 == 1 and i2%2 == 1 else "black",
                        height=62.5,
                        width=62.5,
                        top=62.5*i,
                        left=62.5*i2,
                        data=None if i%2 == 0 and i2%2 == 0 else None if i%2 == 1 and i2%2 == 1 else [index_in_desk_list, 62.5*i, 62.5*i2],
                        alignment=ft.alignment.center,
                        on_click=None if i%2 == 0 and i2%2 == 0 else None if i%2 == 1 and i2%2 == 1 else click_on_desk,
                    )
                )
                if (i%2 == 0 and i2%2 == 1) or (i%2 == 1 and i2%2 == 0):
                    if i in [7, 6, 5]:
                        index_in_white_checkers_list += 1
                        white_checkers_list.append(
                            ft.Container(
                                content=ft.Image(src='images/white_checker.png'),
                                height=62.5,
                                width=62.5,
                                top=62.5 * i,
                                left=62.5 * i2,
                                data=[index_in_white_checkers_list, 62.5*i, 62.5*i2, 'white'],
                                alignment=ft.alignment.center,
                                on_click=click_on_checker,
                                animate_position=ft.animation.Animation(150, ft.AnimationCurve.EASE_IN),
                            )
                        )
                        white_checkers_coordinates_list.append([62.5 * i, 62.5 * i2])
                    elif i in [0, 1, 2]:
                        index_in_black_checkers_list += 1
                        black_checkers_list.append(
                            ft.Container(
                                content=ft.Image(src='images/black_checker.png'),
                                height=62.5,
                                width=62.5,
                                top=62.5 * i,
                                left=62.5 * i2,
                                data=[index_in_black_checkers_list, 62.5*i, 62.5*i2, 'black'],
                                alignment=ft.alignment.center,
                                on_click=click_on_checker,
                                animate_position=ft.animation.Animation(150, ft.AnimationCurve.EASE_IN),
                            )
                        )
                        black_checkers_coordinates_list.append([62.5 * i, 62.5 * i2])


    def click_on_checker(e):
        global is_clicked_on_checker, clicked_checker_info
        if not is_clicked_on_checker:
            is_clicked_on_checker = True
        elif clicked_checker_info != e.control.data:
            is_clicked_on_checker = False
            check_is_clicked_on_checker()
            is_clicked_on_checker = True
        else:
            is_clicked_on_checker = False
        clicked_checker_info = e.control.data
        check_is_clicked_on_checker()

    def cancel_highlighting_moves():
        for i in range(0, len(desk_list)):
            if desk_list[i].bgcolor == "green":
                desk_list[i].bgcolor = "black"
                desk_list[i].update()

    def make_cell_green(i):
        desk_list[i].bgcolor = "green"
        desk_list[i].update()

    def check_is_clicked_on_checker():
        if is_clicked_on_checker:
            check_is_clicked_checker_white()
        else:
            cancel_highlighting_moves()

    def check_is_clicked_checker_white():
        if clicked_checker_info[3] == 'white':
            highlighting_moves_for_white_checkers()
        else:
            highlighting_moves_for_black_checkers()

    def highlighting_moves_for_white_checkers():
        for i in range(0, len(desk_list)):
            coordinates = [desk_list[i].top, desk_list[i].left]
            if coordinates[0] == clicked_checker_info[1] - 62.5 and coordinates[1] in [
                clicked_checker_info[2] + 62.5, clicked_checker_info[2] - 62.5]:
                if coordinates not in white_checkers_coordinates_list:
                    if coordinates not in black_checkers_coordinates_list:
                        make_cell_green(i)

    def highlighting_moves_for_black_checkers():
        for i in range(0, len(desk_list)):
            coordinates = [desk_list[i].top, desk_list[i].left]
            if coordinates[0] == clicked_checker_info[1] + 62.5 and coordinates[1] in [
                clicked_checker_info[2] + 62.5, clicked_checker_info[2] - 62.5]:
                if coordinates not in black_checkers_coordinates_list:
                    if coordinates not in white_checkers_coordinates_list:
                        make_cell_green(i)



    def range_is_normal(data):
        if clicked_checker_info[3] == 'white':
            if clicked_checker_info[1] - 62.5 == data[1] and clicked_checker_info[2] in [data[2] - 62.5, data[2] + 62.5]:
                return True
        else:
            if clicked_checker_info[1] + 62.5 == data[1] and clicked_checker_info[2] in [data[2] - 62.5, data[2] + 62.5]:
                return True


    def click_on_desk(e):
        global is_clicked_on_checker, clicked_checker_info, white_checkers_coordinates_list, black_checkers_coordinates_list
        if is_clicked_on_checker:
            is_clicked_on_checker = False
            if range_is_normal(e.control.data):
                if clicked_checker_info[3] == 'white':
                    check_is_clicked_on_checker()
                    checker = white_checkers_list[clicked_checker_info[0]]

                    checker.top = e.control.data[1]
                    checker.left = e.control.data[2]
                    checker.data = [clicked_checker_info[0], e.control.data[1], e.control.data[2], 'white']
                    checker.update()
                    white_checkers_coordinates_list[clicked_checker_info[0]] = [checker.top, checker.left]
                else:
                    check_is_clicked_on_checker()
                    checker = black_checkers_list[clicked_checker_info[0]]

                    checker.top = e.control.data[1]
                    checker.left = e.control.data[2]
                    checker.data = [clicked_checker_info[0], e.control.data[1], e.control.data[2], 'black']
                    checker.update()
                    black_checkers_coordinates_list[clicked_checker_info[0]] = [checker.top, checker.left]
            else:
                check_is_clicked_on_checker()

    desk_builder()
    page.add(
        ft.Container(
            content=ft.Stack(
                desk_list + white_checkers_list + black_checkers_list,
                width=500,
                height=500
            ),
            alignment=ft.alignment.center,
            expand=True
        )
    )


ft.app(main)
