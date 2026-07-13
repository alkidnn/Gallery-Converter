from .common import create_fancybox_link


def convert(link):
    """
    Конвертация ссылки IMX.
    """

    img = link.find("img")

    if img is None:
        return None

    image_url = img.get("src", "")

    if "/u/t/" in image_url:

        image_url = image_url.replace("/u/t/", "/u/i/")

        if not image_url.startswith("https://image."):

            image_url = image_url.replace(
                "https://",
                "https://image."
            )

    # Добавляем перенос строки в самый конец сгенерированного HTML-кода
    return create_fancybox_link(image_url) + "\n"