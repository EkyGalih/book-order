import flet as ft

def main(page: ft.Page):
    def check_item_clicked(e):
       page.horizontal_alignment = page.vertical_alignment = "center"
       
       page.floating_action_button = ft.FloatingActionButton(icon=ft.icons.ADD)
       page.floating_action_button_location = ft.FloatingActionButtonLocation.CENTER_DOCKED
       e.control.checked = not e.control.checked
       page.update()
       
    page.appbar = ft.AppBar(
        leading=ft.Icon(ft.icons.HOME),
        leading_width=40,
        title=ft.Text("Dapur Kumiku"),
        center_title=False,
        bgcolor=ft.colors.ORANGE_700,
    )
    # page.bottom_appbar = ft.BottomAppBar(
    #     bgcolor=ft.colors.ORANGE_700,
    #     shape=ft.NotchShape.CIRCULAR,
    #     content=ft.Row(
    #         controls=[
    #             ft.IconButton(icon=ft.icons.MENU, icon_color=ft.colors.WHITE),
    #             ft.Container(expand=True),
    #             ft.IconButton(icon=ft.icons.SEARCH, icon_color=ft.colors.WHITE),
    #             ft.IconButton(icon=ft.icons.FAVORITE, icon_color=ft.colors.WHITE),
    #         ]
    #     )
    # )
    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationDestination(icon=ft.icons.HOME, label="Beranda"),
            ft.NavigationDestination(
                icon_content=ft.Badge(
                    content=ft.Icon(ft.icons.BOOK),
                    small_size=10,
                    text="10",
                    ),
                label="Pesanan",
                ),
            ft.NavigationDestination(
                icon=ft.icons.BAR_CHART_OUTLINED,
                selected_icon=ft.icons.BAR_CHART,
                label="Laporan",
            ),
        ]
    )
    
    page.add(ft.Text("Body!"))

ft.app(target=main)
