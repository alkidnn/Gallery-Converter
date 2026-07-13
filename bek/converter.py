from bs4 import BeautifulSoup

def convert_imgbox(html: str):
    soup = BeautifulSoup(html, "html.parser")
    image_count = 0

    for link in soup.find_all("a"):
        image = link.find("img")
        if image and image.has_attr("src"):
            image_url = image["src"]

            # Меняем ссылку на прямое изображение
            link["href"] = image_url
            
            # Удаляем лишний target="_blank"
            link.attrs.pop("target", None)
            
            # Добавляем атрибут для Fancybox лайтбокса
            link["data-fancybox"] = "gallery"
            
            image_count += 1

    return str(soup), image_count