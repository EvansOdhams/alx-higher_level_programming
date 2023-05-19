#include <Python.h>

void print_python_bytes(PyObject *p);

/**
 * print_python_list - Prints basic information about a Python list
 * @p: The Python list object to print information about
 */
void print_python_list(PyObject *p)
{
Py_ssize_t size, i;
PyObject *obj;

printf("[*] Python list info\n");
size = PyList_Size(p);
printf("[*] Size of the Python List = %zd\n", size);
printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);
for (i = 0; i < size; i++)
{
obj = PyList_GetItem(p, i);
printf("Element %zd: %s\n", i, Py_TYPE(obj)->tp_name);
if (PyBytes_Check(obj))
print_python_bytes(obj);
}
}

/**
* print_python_bytes - Prints basic information about a Python bytes object
* @p: The Python bytes object to print information about
*/
void print_python_bytes(PyObject *p)
{
Py_ssize_t size, i;
char *str;

printf("[.] bytes object info\n");
if (!PyBytes_Check(p))
{
printf("  [ERROR] Invalid Bytes Object\n");
return;
}
size = PyBytes_Size(p);
str = PyBytes_AsString(p);
printf("  size: %zd\n", size);
printf("  trying string: %s\n", str);
printf("  first %zd bytes:", (size + 1 > 10) ? 10 : size + 1);
for (i = 0; i < size + 1 && i < 10; i++)
printf(" %02x", (unsigned char)str[i]);
printf("\n");
}
