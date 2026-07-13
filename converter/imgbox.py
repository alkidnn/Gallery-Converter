from .common import create_fancybox_link


def convert(link):
    """
    Конвертация ссылки Imgbox.
    """

    img = link.find("img")

    if img is None:
        return None

    image_url = img.get("src", "")

    # Добавляем перенос строки в самый конец сгенерированного HTML-кода
    return create_fancybox_link(image_url) + "\n"