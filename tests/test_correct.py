import poetry_pybind11 as py_fib
import fast_fib as cpp_fib

def test_py():
    assert py_fib.fib(5) == 8
    assert py_fib.fib(8) == 34
    print('POO!')

def test_cpp():
    assert cpp_fib.fib(5) == 8
    assert cpp_fib.fib(8) == 34

def test_cpp_nogil():
    assert cpp_fib.fib_nogil(5) == 8
    assert cpp_fib.fib_nogil(8) == 34