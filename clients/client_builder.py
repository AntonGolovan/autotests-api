from httpx import Client


def get_http_client_builder() -> Client:
    """
    Функция создаёт экземпляр httpx.Client с базовыми настройками.

    :return: Готовый к использованию объект httpx.Client.
    """
    return Client(timeout=5, base_url="https://qq.taxi.tst.yandex-team.ru/api-t/admin/crm_admin")
