#include <stdio.h>
#include <Python.h>

void print_python_bytes(PyObject *p);
void print_python_list(PyObject *p);

/**
 * print_python_bytes - Prints bytes information
 *
 * @p: Python Object
 * Return: no return
 */
void print_python_bytes(PyObject *p)
{
Py_ssize_t size, i, limit;
char *string;

printf("[.] bytes object info\n");
if (!PyBytes_Check(p))
{
printf("  [ERROR] Invalid Bytes Object\n");
return;
}

size = PyBytes_Size(p);
string = PyBytes_AsString(p);

printf("  size: %zd\n", size);
printf("  trying string: %s\n", string);

limit = size < 10 ? size + 1 : 10;

printf("  first %zd bytes:", limit);

for (i = 0; i < limit; i++)
{
printf(" %02x", (unsigned char)string[i]);
}

printf("\n");
}

/**
 * print_python_list - Prints list information
 *
 * @p: Python Object
 * Return: no return
 */
void print_python_list(PyObject *p)
{
Py_ssize_t size, i;
PyObject *obj;

size = PyList_Size(p);

printf("[*] Python list info\n");
printf("[*] Size of the Python List = %zd\n", size);
printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);

for (i = 0; i < size; i++)
{
obj = PyList_GetItem(p, i);
printf("Element %zd: %s\n", i, Py_TYPE(obj)->tp_name);

if (PyBytes_Check(obj))
{
print_python_bytes(obj);
}
}
}
