#include <Python.h>

/**
* print_python_list_info - Returns the value of a bit at a given index.
* @p: The number to get the bit from.
* Return: The value of the bit at index, or -1 if an error occurs.
*/
void print_python_list_info(PyObject *p)
{
Py_ssize_t size, i;
PyObject *obj;

size = PyList_Size(p);
if (size < 0)
{
printf("Failed to get the size of the list\n");
return;
}

printf("[*] Size of the Python List = %ld\n", size);
printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

for (i = 0; i < size; i++)
{
printf("Element %ld: ", i);

obj = PyList_GetItem(p, i);
if (obj == NULL)
{
printf("Failed to get item at index %ld\n", i);
continue;
}

printf("%s\n", obj->ob_type->tp_name);
}
}
