# Abstract class to generalize SVMs kernels
The `Kernel` abstract class is meant as a layout for kernels used by Support Vector Machines,
uncoupling the SVM code from the kernel used.
Defining your kernels by extending the `Kernel` abstract class will let you exchange them 
on demand without changing your SVM code, just pass to your SVM the concrete kernel class
of your choice.

##usage
The `Kernel` abstract class takes two optional parameters `vectors` and `kernel_matrix` 
which will initialize the `VECTORS` and `KERNEL_MATRIX` attributes:

`VECTORS` is by default a dictionary with some vectorizable as keys 
and the corresponding vector in DOK (Dictionary of keys) format as values, 
for example: `{'doc frankenstein': {10: 1, 13: 1, 37: 1, 64: 1, ...}, 
'doc drunkenstein': {80: 1, 98: 1, 116: 1, 121: 1, ...}}`, but you can 
redefine it to whatever you want as long as you don't call the default
`vectorize` implementation in your subclass; 

`KERNEL_MATRIX` is by default a dictionary that vectorizables as keys and another dictionary 
with vectorizables as keys and the kernel value between the two keys as values,  
for example `{'doc frankenstein': {'doc drunkenstein': 0.7500011542039571, 'doc nykterstein': 0.5041614599291009}}`, 
but you can redefine it to whatever you want as long as you don't call the default
`get_kernel` implementation in your subclass;

Note: if you define various kernels, everyone of those should be consistent with the 
attributes format.

The class defines the abstract methods `vectorize(x)` and `get_kernel(x1, x2)`:

`vectorize(x)` by default just checks if `VECTORS[x]` exists and returns it or 
`False` otherwise, in your own implementation it should vectorize the input `x` 
and maybe store it into the `VECTORS` attribute;

`get_kernel(x1, x2)` by default just check if `KERNEL_MATRIX[x1][x2]` or `KERNEL_MATRIX[x2][x1]` 
exists and returns it or `False` otherwise, in your own implementation it should compute the 
kernel value between inputs `x1` and `x2` and maybe store it into the `KERNEL_MATRIX` attribute.

### Example
The example below is taken from [mismatch-string-kernel][https://pypi.org/project/mismatch-string-kernel/].

```python
from abstract_kernel import Kernel

class MismatchKernel(Kernel):
    def __init__(self, param1, param2, mismatch_vectors=None, kernel_matrix=None):
        # other init stuff...
        super().__init__(mismatch_vectors, kernel_matrix)

    def vectorize(self, x):
        # if mismatch vector not already computed for an input
        # compute it and save it
        vector = super().vectorize(x)
        if not vector:
            vector =  # code to vectorize x...
            self.VECTORS[x] = vector
        return vector

    def get_kernel(self, x1, x2):
        # check if kernel has already been calculated
        kernel = super().get_kernel(x1, x2)
        if kernel:
            return kernel

        v1 = self.vectorize(x1)
        v2 = self.vectorize(x2)

        kernel =  # code to compute kernel between v1 and v2...

        if x1 not in self.KERNEL_MATRIX:
            self.KERNEL_MATRIX[x1] = {}
        self.KERNEL_MATRIX[x1][x2] = kernel

        return kernel
```

[https://pypi.org/project/mismatch-string-kernel/]: https://pypi.org/project/mismatch-string-kernel/