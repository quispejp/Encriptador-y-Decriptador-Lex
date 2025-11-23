import flet as ft
from flet import Page, Text, TextField, Column, Row, ElevatedButton, Container, Colors, padding, border
from encriptador import encriptar, desencriptar


def main(page: ft.Page):
    page.title = "Encriptador / Desencriptador"
    page.vertical_alignment = "start"
    page.horizontal_alignment = "center"
    page.scroll = "auto"
    page.padding = 20
    page.bgcolor = Colors.BLUE_GREY_50

    # -------------------------------
    # TÍTULO
    # -------------------------------
    titulo = Text(
        "Encriptador / Desencriptador",
        size=30,
        weight="bold",
        color=Colors.BLACK
    )

    # -------------------------------
    # TEXTAREA DE ENTRADA
    # -------------------------------
    txt_input_field = TextField(
        label="Ingresa tu texto aquí",
        multiline=True,
        width=600,
        height=180,
        color=Colors.BLACK
    )
    txt_input = Container(
        content=txt_input_field,
        bgcolor=Colors.WHITE,
        padding=padding.all(10),
        border=border.all(2, Colors.BLACK),
        border_radius=10
    )

    # -------------------------------
    # TEXTOS ENCRIPTADO / DESENCRIPTADO
    # -------------------------------
    txt_encriptado_text = Text(value="", selectable=True, color=Colors.BLACK)
    txt_encriptado = Container(
        content=txt_encriptado_text,
        bgcolor=Colors.WHITE,
        padding=padding.all(10),
        border=border.all(2, Colors.BLACK),
        border_radius=10,
        width=400,
        height=200
    )

    txt_desencriptado_text = Text(value="", selectable=True, color=Colors.BLACK)
    txt_desencriptado = Container(
        content=txt_desencriptado_text,
        bgcolor=Colors.WHITE,
        padding=padding.all(10),
        border=border.all(2, Colors.BLACK),
        border_radius=10,
        width=400,
        height=200
    )

    # =====================================================
    # FILE PICKER PARA ABRIR ARCHIVOS
    # =====================================================
    def archivo_seleccionado(e: ft.FilePickerResultEvent):
        if e.files:
            ruta = e.files[0].path
            try:
                with open(ruta, "r", encoding="utf-8") as f:
                    txt_input_field.value = f.read()
                page.update()
            except Exception as err:
                txt_input_field.value = f"Error al leer archivo: {err}"
                page.update()

    file_picker_abrir = ft.FilePicker(on_result=archivo_seleccionado)
    page.overlay.append(file_picker_abrir)

    def btn_seleccionar_click(e):
        file_picker_abrir.pick_files(
            allow_multiple=False,
            allowed_extensions=["txt"]
        )

    # =====================================================
    # FILE PICKER PARA GUARDAR ARCHIVOS
    # =====================================================
    # Usamos este dict para saber qué texto guardar
    contenido_a_guardar = {"texto": ""}

    def guardar_archivo_result(e: ft.FilePickerResultEvent):
        # Aquí e.path es la ruta elegida en el diálogo "Guardar como..."
        if e.path:
            try:
                with open(e.path, "w", encoding="utf-8") as f:
                    f.write(contenido_a_guardar["texto"])
            except Exception as err:
                print("Error al guardar:", err)

    file_picker_guardar = ft.FilePicker(on_result=guardar_archivo_result)
    page.overlay.append(file_picker_guardar)

    # =====================================================
    # FUNCIONES DE BOTONES (ENCRIPTAR / DESENCRIPTAR)
    # =====================================================
    def btn_encriptar_click(e):
        if txt_input_field.value.strip():
            txt_encriptado_text.value = encriptar(txt_input_field.value)
            txt_desencriptado_text.value = ""
            page.update()

    def btn_desencriptar_click(e):
        if txt_encriptado_text.value.strip():
            txt_desencriptado_text.value = desencriptar(txt_encriptado_text.value)
            page.update()

    # =====================================================
    # FUNCIONES DE GUARDADO
    # =====================================================
    def guardar_encriptado(e):
        contenido_a_guardar["texto"] = txt_encriptado_text.value
        # abre ventana "Guardar como..." con nombre sugerido
        file_picker_guardar.save_file(file_name="encriptado.txt")

    def guardar_desencriptado(e):
        contenido_a_guardar["texto"] = txt_desencriptado_text.value
        file_picker_guardar.save_file(file_name="desencriptado.txt")

    # -------------------------------
    # BOTONES
    # -------------------------------
    botones = Row(
        [
            ElevatedButton("Seleccionar archivo",
                           on_click=btn_seleccionar_click,
                           bgcolor=Colors.ORANGE_400,
                           color=Colors.WHITE),

            ElevatedButton("Encriptar",
                           on_click=btn_encriptar_click,
                           bgcolor=Colors.BLUE_400,
                           color=Colors.WHITE),

            ElevatedButton("Desencriptar",
                           on_click=btn_desencriptar_click,
                           bgcolor=Colors.GREEN_400,
                           color=Colors.WHITE),
        ],
        alignment="center",
        spacing=20
    )

    # -------------------------------
    # LAYOUT
    # -------------------------------
    page.add(
        Column(
            [
                titulo,
                txt_input,
                botones,
                Row(
                    [
                        Column(
                            [
                                Text("Texto Encriptado", weight="bold", color=Colors.BLACK),
                                txt_encriptado,
                                ElevatedButton(
                                    "Guardar",
                                    bgcolor=Colors.BLUE_GREY_300,
                                    color=Colors.BLACK,
                                    on_click=guardar_encriptado
                                )
                            ]),
                        Column(
                            [
                                Text("Texto Desencriptado", weight="bold", color=Colors.BLACK),
                                txt_desencriptado,
                                ElevatedButton(
                                    "Guardar",
                                    bgcolor=Colors.BLUE_GREY_300,
                                    color=Colors.BLACK,
                                    on_click=guardar_desencriptado
                                )
                            ]),
                    ],
                    alignment="center",
                    spacing=40
                )
            ],
            spacing=20,
            horizontal_alignment="center"
        )
    )


ft.app(main)
