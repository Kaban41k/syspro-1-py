#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <stdlib.h>

void* nc_malloc(size_t size) {
  void* result = malloc(size);

  if (result == NULL) {
    printf("Out of memory\n");
    exit(1);
  }

  return result;
}

static PyObject* matrix_power(PyObject* self, PyObject* args) {
  PyObject* matrix;
  size_t degree;
  size_t n;

  if (!PyArg_ParseTuple(args, "Ol", &matrix, &degree)) {
    return NULL;
  }

  n = PyObject_Length(matrix);

  double* a = (double*) nc_malloc(n * n * sizeof(double));
  double* b = (double*) nc_malloc(n * n * sizeof(double));
  double* buf = (double*) nc_malloc(n * n * sizeof(double));

  for (size_t i = 0; i < n; i++) {
    PyObject* list = PyList_GetItem(matrix, i);

    for (size_t j = 0; j < n; j++) {
      a[i * n + j] = PyFloat_AsDouble(PyList_GetItem(list, j));
    }
  }

  for (size_t i = 0; i < n; i++) {
    for (size_t j = 0; j < n; j++) {
      b[i * n + j] = a[i * n + j];
    }
  }

  for (size_t iteration = 1; iteration < degree; iteration++) {
    double sum;

    for (size_t i = 0; i < n; i++) {
      for (size_t j = 0; j < n; j++) {
        sum = 0;

        for (size_t l = 0; l < n; l++)
          sum += a[i * n + l] * b[l * n + j];

        buf[i * n + j] = sum;
      }
    }

    double* c = buf;
    buf = a;
    a = c;
  }

  PyObject* result = PyList_New(n);

  for (size_t i = 0; i < n; i++) {
    PyObject* list = PyList_New(n);

    for (size_t j = 0; j < n; j++) {
      PyList_SetItem(list, j, PyFloat_FromDouble(a[i * n + j]));
    }

    PyList_SetItem(result, i, list);
  }

  free(a);
  free(b);
  free(buf);

  return result;

}

static PyMethodDef methods[] = {
    {"matrix_power", matrix_power, METH_VARARGS, ""},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef module = {
    PyModuleDef_HEAD_INIT, "matrix_power", NULL, -1, methods,
};

PyObject* PyInit_foreign(void) { return PyModule_Create(&module); }