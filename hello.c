#define PY_SSIZE_T_CLEAN
#include <Python.h>


static PyObject *SpamError;

void *hello_doc = 0;


hello_system(PyObject *self, PyObject *args)
{
    return PyLong_FromLong(1);
}

static PyMethodDef SpamMethods[] = {
    {"system", hello_system, METH_VARARGS, "Execute a shell command."},
    {NULL,     NULL,        0,            NULL}  /* Sentinel */
};

static struct PyModuleDef hellomodule = {
    PyModuleDef_HEAD_INIT,
    "hello",   /* name of module */
    0, /* module documentation, may be NULL */
    -1,       /* size of per-interpreter state of the module,
                 or -1 if the module keeps state in global variables. */
    SpamMethods
};


PyMODINIT_FUNC
PyInit_hello(void)
{
    PyObject *m;

    m = PyModule_Create(&hellomodule);
    if (m == NULL)
        return NULL;

    SpamError = PyErr_NewException("hello.error", NULL, NULL);
    Py_XINCREF(SpamError);
    if (PyModule_AddObject(m, "error", SpamError) < 0) {
        Py_XDECREF(SpamError);
        Py_CLEAR(SpamError);
        Py_DECREF(m);
        return NULL;
    }

    return m;
}
