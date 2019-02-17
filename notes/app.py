import requests


class Test:
    pass


def main():
    response = requests.get("https://velotio.com
    ")
    print(response.status_code)


def test(a: int, b: str) -> str:
    """[summary]

    Args:
        a (int): [description]
        b (str): [description]

    Returns:
        str: [description]
    """
    return b ** a


if __name__ == "__main__":
    main()
