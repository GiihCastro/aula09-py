import flet as ft

def main(page:ft.Page):

  def clickButton(e):
    media = (float(nota1.value) + float(nota2.value)) / 2
    if media >= 7:
      result.value = "Aprovado."
    else:
      result.value = "Reprovado."
    page.update()

  page.title = "Checar Aprovação"
  text = ft.Text(value="Programa para calcular média e verificar aprovação", size=25)
  nota1 = ft.TextField(label="Primeira nota", keyboard_type=ft.KeyboardType.NUMBER)
  nota2 = ft.TextField(label="Segunda nota", keyboard_type=ft.KeyboardType.NUMBER)
  button = ft.ElevatedButton(text="Verificar", on_click=clickButton)
  result = ft.Text(value="")
  page.add(text, nota1, nota2, button, result)

ft.app(target=main)