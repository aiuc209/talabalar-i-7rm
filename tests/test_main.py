import pytest

def create_student_info(names, averages):
    return [f"Talaba: {name} | O‘rtacha ball: {average:.1f}" for name, average in zip(names, averages)]

def test_create_student_info():
    names = ["Ali", "Vali", "G‘ani"]
    averages = [4.5, 3.7, 4.2]
    expected_output = [
        "Talaba: Ali | O‘rtacha ball: 4.5",
        "Talaba: Vali | O‘rtacha ball: 3.7",
        "Talaba: G‘ani | O‘rtacha ball: 4.2"
    ]
    assert create_student_info(names, averages) == expected_output

def test_create_student_info_empty_lists():
    names = []
    averages = []
    expected_output = []
    assert create_student_info(names, averages) == expected_output

def test_create_student_info_unequal_list_lengths():
    names = ["Ali", "Vali"]
    averages = [4.5, 3.7, 4.2]
    with pytest.raises(ValueError):
        create_student_info(names, averages)

def test_create_student_info_non_numeric_averages():
    names = ["Ali", "Vali", "G‘ani"]
    averages = [4.5, "3.7", 4.2]
    with pytest.raises(TypeError):
        create_student_info(names, averages)
