"""
Testing challenge with test input.

"""

from day_01 import import_list, count_elf_calories

test_input = import_list("test-input")
total_calories_list = count_elf_calories(test_input)


def test_get_max_calories():
    from day_01 import get_max_calories

    result = get_max_calories(total_calories_list)
    assert result == 24000


def test_get_combined_backup_calories():
    from day_01 import get_combined_backup_calories

    result = get_combined_backup_calories(total_calories_list)
    assert result == 45000
