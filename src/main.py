import random
import flet as ft

def main(page: ft.Page):

    page.title = 'Guessing Game'
    page.bgcolor = "#121212"
    page.padding = 20
    page.theme_mode = 'dark'

    random_number = random.randint(1,10)
    attempts = 0

    #Making tittle
    title = ft.Container(
        content=ft.Text(
            "Guessing Game",
            size=32,
            weight=ft.FontWeight.BOLD,
            color='#ffffff'
        ),
        padding=20,
    )

    guess = ft.Container(
        content=ft.Text(
            "Pick a number 1-10",
            size=15,
            weight=ft.FontWeight.BOLD,
            color='#ffffff'
        ),
        padding=20,
        alignment=ft.MainAxisAlignment.CENTER,
    )

    result = ft.Text(
        "Ready? Set! Guess!",
        size=15,
        color='#ffffff'
    )

    def reset():
        nonlocal random_number, attempts
        random_number = random.randint(1,10)
        result.value = "Reset!"
        result.color = "#ffffff"
        attempts = 0

    reset_button = ft.ElevatedButton("Reset", on_click=lambda e: reset())



    def check_guess(number):
        nonlocal random_number, attempts
        attempts += 1
        if random_number > number:
            result.value = "To low try again"
            result.color = "#00AEFF"
        elif random_number < number:
            result.value = "To high try again"
            result.color = "#FA4242"
        else:
            result.value = "Correct! It took you " + str(attempts) + " guesses"
            result.color = "#00ff00"
        result.update()  

    button_1 = ft.ElevatedButton("1", on_click=lambda e: check_guess(1))
    button_2 = ft.ElevatedButton("2", on_click=lambda e: check_guess(2))
    button_3 = ft.ElevatedButton("3", on_click=lambda e: check_guess(3))
    button_4 = ft.ElevatedButton("4", on_click=lambda e: check_guess(4))
    button_5 = ft.ElevatedButton("5", on_click=lambda e: check_guess(5))
    button_6 = ft.ElevatedButton("6", on_click=lambda e: check_guess(6))
    button_7 = ft.ElevatedButton("7", on_click=lambda e: check_guess(7))
    button_8 = ft.ElevatedButton("8", on_click=lambda e: check_guess(8))
    button_9 = ft.ElevatedButton("9", on_click=lambda e: check_guess(9))
    button_10 = ft.ElevatedButton("10", on_click=lambda e: check_guess(10))

    button_row = ft.Row(
        controls=[
            button_1, button_2, button_3, button_4, button_5, button_6,button_7, button_8, button_9, button_10
        ],
        alignment=ft.MainAxisAlignment.CENTER,
    )

    result_row = ft.Row(
        controls=[
            result,
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )

    reset_button_row = ft.Row(
        controls=[
            reset_button,
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )

    column = ft.Column(
        [title, guess, button_row, result_row, reset_button_row],
        alignment=ft.MainAxisAlignment.START,
        spacing=10
    )



    column.alignment = ft.Alignment.CENTER
    guess.alignment = ft.Alignment.CENTER
    title.alignment = ft.Alignment.TOP_CENTER
    result.alignment = ft.Alignment.TOP_CENTER
    page.add(
        ft.SafeArea(
            expand=True,
            content=ft.Container(
                content=column,
                alignment=ft.Alignment.CENTER,
            ),
        )
    )

ft.run(main)