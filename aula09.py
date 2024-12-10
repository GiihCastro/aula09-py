import flet as ft

def main(page:ft.Page):

  def clickButton(e):
    if int(entrada.value) >= 18:
      result.value = "Maior de idade."
    else:
      result.value = "Menor de idade."
    page.update()

  page.title = "Checar Idades"
  text = ft.Text(value="Programa para checar idades", size=30)
  entrada = ft.TextField(label="Idade", keyboard_type=ft.KeyboardType.NUMBER)
  button = ft.ElevatedButton(text="Clique aqui!", on_click=clickButton)
  result = ft.Text(value="")
  page.add(text, entrada, button, result)

ft.app(target=main)