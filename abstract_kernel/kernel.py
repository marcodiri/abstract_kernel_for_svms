from abc import ABC, abstractmethod


class Kernel(ABC):
    def __init__(self, vectors=None, kernel_matrix=None):
        if vectors is None:
            vectors = {}
        if kernel_matrix is None:
            kernel_matrix = {}
        self.VECTORS = vectors
        self.KERNEL_MATRIX = kernel_matrix

    @property
    def VECTORS(self):
        return self.VECTORS

    @VECTORS.setter
    def VECTORS(self, vectors):
        self.VECTORS = vectors

    @property
    def KERNEL_MATRIX(self):
        return self.VECTORS

    @KERNEL_MATRIX.setter
    def KERNEL_MATRIX(self, kernel_matrix):
        self.KERNEL_MATRIX = kernel_matrix

    @abstractmethod
    def vectorize(self, x):
        return self.VECTORS[x] if x in self.VECTORS else False

    @abstractmethod
    def get_kernel(self, x1, x2):
        # look up matrix for already computed kernel
        if x1 in self.KERNEL_MATRIX and x2 in self.KERNEL_MATRIX[x1]:
            return self.KERNEL_MATRIX[x1][x2]
        elif x2 in self.KERNEL_MATRIX and x1 in self.KERNEL_MATRIX[x2]:
            return self.KERNEL_MATRIX[x2][x1]
        return False
