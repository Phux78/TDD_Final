from function import validate_number, display_price
import pytest

def test_input_char_a():
    input_Espresso = "a"
    input_Cappuccino = 0
    input_Latte = 0
    input_Mocca = 0
    expected_result = "Please input an integer"
    actual_result = validate_number(input_Espresso, input_Cappuccino, input_Latte, input_Mocca)
    assert expected_result == actual_result

def test_input_char_O_point_one():
    input_Espresso = 0.1
    input_Cappuccino = 0
    input_Latte = 0
    input_Mocca = 0
    expected_result = "Please input an integer"
    actual_result = validate_number(input_Espresso, input_Cappuccino, input_Latte, input_Mocca)
    assert expected_result == actual_result

def test_input_char_minus_one():
    input_Espresso = -1
    input_Cappuccino = 0
    input_Latte = 0
    input_Mocca = 0
    expected_result = "Please input an integer"
    actual_result = validate_number(input_Espresso, input_Cappuccino, input_Latte, input_Mocca)
    assert expected_result == actual_result

def test_order_one_Espresso_discount_no():
    input_Espresso = 1
    input_Cappuccino = 0
    input_Latte = 0
    input_Mocca = 0
    discount = "n"
    expected_result = 55
    actual_result = display_price(input_Espresso, input_Cappuccino, input_Latte, input_Mocca, discount)
    assert expected_result == actual_result 

def test_order_one_Cappuccino_discount_no():
    input_Espresso = 0
    input_Cappuccino = 1
    input_Latte = 0
    input_Mocca = 0
    discount = "n"
    expected_result = 60
    actual_result = display_price(input_Espresso, input_Cappuccino, input_Latte, input_Mocca, discount)
    assert expected_result == actual_result 

def test_order_one_Latte_discount_no():
    input_Espresso = 0
    input_Cappuccino = 0
    input_Latte = 1
    input_Mocca = 0
    discount = "n"
    expected_result = 65
    actual_result = display_price(input_Espresso, input_Cappuccino, input_Latte, input_Mocca, discount)
    assert expected_result == actual_result 

def test_order_one_Mocca_discount_no():
    input_Espresso = 0
    input_Cappuccino = 0
    input_Latte = 0
    input_Mocca = 1
    discount = "n"
    expected_result = 70
    actual_result = display_price(input_Espresso, input_Cappuccino, input_Latte, input_Mocca, discount)
    assert expected_result == actual_result 

def test_multiple_order_discount_no():
    input_Espresso = 1
    input_Cappuccino = 1
    input_Latte = 1
    input_Mocca = 1
    discount = "n"
    expected_result = 250
    actual_result = display_price(input_Espresso, input_Cappuccino, input_Latte, input_Mocca, discount)
    assert expected_result == actual_result 

def test_order_one_Espresso_discount_yes():
    input_Espresso = 1
    input_Cappuccino = 0
    input_Latte = 0
    input_Mocca = 0
    discount = "y"
    expected_result = 50
    actual_result = display_price(input_Espresso, input_Cappuccino, input_Latte, input_Mocca, discount)
    assert expected_result == actual_result 

def test_order_one_Cappuccino_discount_yes():
    input_Espresso = 0
    input_Cappuccino = 1
    input_Latte = 0
    input_Mocca = 0
    discount = "y"
    expected_result = 55
    actual_result = display_price(input_Espresso, input_Cappuccino, input_Latte, input_Mocca, discount)
    assert expected_result == actual_result 

def test_order_one_Latte_discount_yes():
    input_Espresso = 0
    input_Cappuccino = 0
    input_Latte = 1
    input_Mocca = 0
    discount = "y"
    expected_result = 60
    actual_result = display_price(input_Espresso, input_Cappuccino, input_Latte, input_Mocca, discount)
    assert expected_result == actual_result 

def test_order_one_Mocca_discount_yes():
    input_Espresso = 0
    input_Cappuccino = 0
    input_Latte = 0
    input_Mocca = 1
    discount = "y"
    expected_result = 65
    actual_result = display_price(input_Espresso, input_Cappuccino, input_Latte, input_Mocca, discount)
    assert expected_result == actual_result 

def test_multiple_order_discount_yes():
    input_Espresso = 1
    input_Cappuccino = 1
    input_Latte = 1
    input_Mocca = 1
    discount = "y"
    expected_result = 230
    actual_result = display_price(input_Espresso, input_Cappuccino, input_Latte, input_Mocca, discount)
    assert expected_result == actual_result

def test_validate_discount_input_char_e():
    input_Espresso = 0
    input_Cappuccino = 0
    input_Latte = 0
    input_Mocca = 1
    discount = "e"
    expected_result = "Please in put y or n"
    actual_result = display_price(input_Espresso, input_Cappuccino, input_Latte, input_Mocca, discount)
    assert expected_result == actual_result 

def test_validate_discount_input_O_point_one():
    input_Espresso = 0
    input_Cappuccino = 0
    input_Latte = 0
    input_Mocca = 1
    discount = 0.1
    expected_result = "Please in put y or n"
    actual_result = display_price(input_Espresso, input_Cappuccino, input_Latte, input_Mocca, discount)
    assert expected_result == actual_result 

def test_validate_discount_input_minus_one():
    input_Espresso = 0
    input_Cappuccino = 0
    input_Latte = 0
    input_Mocca = 1
    discount = -1
    expected_result = "Please in put y or n"
    actual_result = display_price(input_Espresso, input_Cappuccino, input_Latte, input_Mocca, discount)
    assert expected_result == actual_result 

def test_validate_discount_input_integer():
    input_Espresso = 0
    input_Cappuccino = 0
    input_Latte = 0
    input_Mocca = 1
    discount = 1
    expected_result = "Please in put y or n"
    actual_result = display_price(input_Espresso, input_Cappuccino, input_Latte, input_Mocca, discount)
    assert expected_result == actual_result 