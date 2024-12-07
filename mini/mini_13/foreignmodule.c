#define PY_SSIZE_T_CLEAN
#include <Python.h>

void* nc_malloc(size_t size) {
  void* result = malloc(size);

  if (result == NULL) {
    printf("Out of memory\n");
    exit(1);
  }

  return result;
}

static void ptr_swap(double** a, double** b) {
    double* c = *b;
    *b = *a;
    *a = c;
}

static PyObject* foreign_matrix_power(PyObject* self, PyObject* args) {
  PyObject* matrix;
  size_t degree;
  size_t n;

  if (!PyArg_ParseTuple(args, "OK", &matrix, &degree))
    return NULL;

  n = PyObject_Length(matrix);


  double* a = nc_malloc(n * n * sizeof(double));
  double* b = nc_malloc(n * n * sizeof(double));
  double* buf = nc_malloc(n * n * sizeof(double));


  for (size_t i = 0; i < n; i++) {
    PyObject* list = PyList_GetItem(matrix, i);
    for (size_t j = 0; j < n; j++) {
      PyObject* item = PyList_GetItem(list, j);
      a[i * n + j] = PyFloat_AsDouble(item);
    }
  }

  memcpy(a, b, n * n * sizeof(double));

  for (size_t iteration = 0; iteration < n; iteration++) {
    double sum;

    for (size_t i = 0; i < n; i++) {
      for (size_t j = 0; j < n; j++) {
        sum = 0;

        for (size_t l = 0; l < n; l++)
          sum += a[i * n + l] * b[l * n + j];

        buf[i * n + j] = sum;
      }
    }

    ptr_swap(&a, &buf);
  }

  PyObject* result = PyList_New(n);

  for (size_t i = 0; i < n; i++) {
    PyObject* list = PyList_New(n);
    PyList_SetItem(result, i, list);
    for (size_t j = 0; j < n; j++) {
      double item = a[i * n + j];
      PyList_SetItem(list, j, PyFloat_FromDouble(item));
    }
  }

  free(a);
  free(b);
  free(buf);

  return result;
}

static PyMethodDef methods[] = {
    {
        .ml_name = "foreign_matrix_power",
        .ml_meth = foreign_matrix_power,
        .ml_flags = METH_VARARGS,
        .ml_doc = "",
    },
    {NULL, NULL, 0, NULL},
};

static struct PyModuleDef module = {
    PyModuleDef_HEAD_INIT, "foreign_matrix_power", NULL, -1, methods,
};

PyObject* PyInit_foreign(void) { return PyModule_Create(&module); }