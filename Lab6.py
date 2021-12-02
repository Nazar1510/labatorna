import requests
from bs4 import BeautifulSoup


def main() -> None:
    def GetTagCount(bs: BeautifulSoup, tag) -> int:
        return len(bs.find_all(tag))

    link: str = "https://www.ukr.net/"
    page: BeautifulSoup = BeautifulSoup(requests.get(link).text, 'html.parser')
    images_count: int = GetTagCount(page, "img")
    links_count: int = GetTagCount(page, "a")
    tags_count: int = GetTagCount(page, True)
    print(f"Page: {link}\n"
          f"Image tags count: {images_count}\n"
          f"Link tags count: {links_count}\n"
          f"HTML Tags count: {tags_count}")


if __name__ == "__main__":
    main()
