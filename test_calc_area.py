'''def test_calc_area_square():
    from calc_area import calc_area_square
    
      
    input_number =2

    output_number = calc_area_square(input_number)
    
    assert output_number == 4'''
'''    
    
    
def test_calc_area_square():
    from calc_area import calc_area_square
    
        
    input_numbers = [0, 1, 4, 100]

    output_numbers = [0,1,16,10000]
    
    assert len(input_numbers) == len(output_numbers)
    
    for input, output in zip (input_numbers, output_numbers):    
        assert calc_area_square(input) == output
        
        
    # option 2
    for i in range(len(input_numbers)):
        this_input = input_numbers[i]
        this_exp_out = output_numbers[i]

        assert calc_area_square(this_input) == this_exp_out
        
        
from pytest import approx, raises 
     
def test_calc_area_circle():
    from calc_area import calc_area_circle
    
    assert calc_area_circle(2) == approx(12.5663, abs = 1e-3)
    
def test_calc_area_circle_errors():
    from calc_area import calc_area_circle
    
    with raises(ValueError):
        calc_area_circle(-1.0)
        
    with raises(TypeError):
        calc_area_circle('this is not a number')'''
        
# you feed it the values that will trigger teh errors, 
# if errors occur, it means the test passes. 

from pytest import approx, raises


def test_calc_area_rectangle():
    from calc_area import calc_area_rectangle
    assert calc_area_rectangle(2, 2) == 4
    assert calc_area_rectangle(2, 1) == 2
    
    
def test_calc_area_circle():
    from calc_area import calc_area_circle

    assert calc_area_circle(2) == approx(12.5663, abs=1e-3)

def test_calc_area_circle_errors():
    from calc_area import calc_area_circle

    with raises(ValueError):
        calc_area_circle(-1.0)

    with raises(TypeError):
        calc_area_circle('this is not a number')