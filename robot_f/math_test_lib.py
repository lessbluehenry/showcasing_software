from robot.libraries.BuiltIn import assert_equal
from robot.api.deco import keyword


@keyword('I ensure ${summand1} plus ${summand2} equals ${sum}')
def test_math_plus(summand1, summand2, sum):
    assert_equal((int(summand1) + int(summand2)),
                 int(sum),
                 msg="assert error: there seems"
                     " to be a problem with math")


@keyword('I ensure ${minuend} minus ${subtrahend} equals ${defferenz}')
def test_math_minus(minuend, subtrahend, defferenz):
    assert_equal((int(minuend) - int(subtrahend)),
                 int(defferenz),
                 msg="assert error: there seems"
                     " to be a problem with math")
