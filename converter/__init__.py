from bs4 import BeautifulSoup

from . import imgbox
from . import imx


def convert_gallery(html_data: str):
    """
    Конвертирует HTML галереи в формат Fancybox.
    """

    soup = BeautifulSoup(html_data, "html.parser")

    converted_links = []

    for link in soup.find_all("a"):

        href = link.get("href", "")

        html = None

        # Imgbox
        if "imgbox.com" in href:
            html = imgbox.convert(link)

        # IMX
        elif "imx.to" in href:
            html = imx.convert(link)

        if html:
            converted_links.append(html)

    result = "".join(converted_links)

    return result, len(converted_links)