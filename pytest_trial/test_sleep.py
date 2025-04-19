# Импортируем новую функцию.
import pytest
from time import sleep


@pytest.mark.sloww  # Отмечаем маркером тест.
def test_type():
    """Тестируем тип данных, возвращаемых из get_sort_list()."""
    sleep(3)  # Трёхсекундная пауза.


def test_simple():
    """Простой тест."""
    assert 1 + 1 == 2
