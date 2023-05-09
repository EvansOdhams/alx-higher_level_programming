#include "lists.h"

/**
* check_cycle - checks if a singly linked list has a cycle in it
* @list: pointer to the head of the linked list
*
* Return: 0 if there is no cycle, 1 if there is a cycle
*/
int check_cycle(listint_t *list)
{
listint_t *ptr1 = list; /* Slow pointer */
listint_t *ptr2 = list; /* Fast pointer */

/* If the list is empty, there is no cycle */
if (list == NULL)
return (0);

/* Traverse the linked list with the two pointers */
while (ptr1 != NULL && ptr2 != NULL && ptr2->next != NULL)
{
ptr1 = ptr1->next; /* Move slow pointer one step */
ptr2 = ptr2->next->next; /* Move fast pointer two steps */

/* If the two pointers meet, there is a cycle */
if (ptr1 == ptr2)
return (1);
}

/* If the end of the list is reached, there is no cycle */
return (0);
}
