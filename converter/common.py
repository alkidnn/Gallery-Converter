IMAGE_STYLE = (
    "width: 100%; "
    "height: auto; "
    "max-width: 100%;"
)


def create_fancybox_link(image_url: str) -> str:
    """
    Создаёт HTML-код изображения для Fancybox.
    """

    return (
        f'<a href="{image_url}" data-fancybox="gallery">'
        f'<img src="{image_url}" style="{IMAGE_STYLE}"/>'
        f'</a>'
    )