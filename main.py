import flet as ft


def main(page: ft.Page):
    product_field = ft.TextField(label="Product", value="icecream")
    price_field = ft.TextField(label="Price", value="200")
    receipt_text = ft.Text()
    message_text = ft.Text()

    def generate_receipt():
        product = (product_field.value or "").strip()
        try:
            price = float(price_field.value or "")
            if not product or price < 0:
                raise ValueError
        except ValueError:
            receipt_text.value = ""
            message_text.value = "Enter a product and a valid, non-negative price."
            receipt_text.update()
            message_text.update()
            return

        message_text.value = ""
        receipt_text.value = f"The cost of {product} is: #{price:.2f}"
        message_text.update()
        receipt_text.update()

    page.add(
        ft.Column(
            controls=[
                ft.Text("Simple Receipt Generator"),
                product_field,
                price_field,
                ft.Button(
                    content="Generate receipt",
                    bgcolor=ft.Colors.TEAL,
                    color=ft.Colors.WHITE,
                    on_click=generate_receipt,
                ),
                message_text,
                receipt_text,
            ]
        )
    )


ft.run(main)
