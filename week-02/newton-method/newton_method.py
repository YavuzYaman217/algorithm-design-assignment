def newton_method(func,funcderiv,x,n):
    def f(x):
        f = eval(func)
        return f
    def fderiv(x):
        fderiv = eval(funcderiv)
        return fderiv
    for i in range(1,n):
        i = x - f(x) / fderiv(x)
        x = i
    print(f"The root at iteration {n} is: {x}")
    return x


def newton_method_wrapper(params):
    """Wrapper function for test_wrapper compatibility"""
    func, funcderiv, x, n = params
    return newton_method(func, funcderiv, x, n)


if __name__ == "__main__":
    import sys
    sys.path.insert(0, '../..')
    from test_wrapper import TestWrapper
    
    # Test mode
    wrapper = TestWrapper(
        function=newton_method_wrapper,
        test_file="test_cases.txt"
    )
    wrapper.run_all_tests()
    
    # Original test call
    newton_method("x**3 - x - 2","3*x**2 - 1",1.5,10)
