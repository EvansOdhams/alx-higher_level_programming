#include "lists.h"

/**
* insert_node - Inserts a number into a sorted singly linked list
* @head: Double pointer to head node of linked list
* @number: Number to insert
*
* Return: Address of new node or NULL if failed
*/
listint_t *insert_node(listint_t **head, int number)
{
listint_t *new_node = NULL, *prev_node = NULL, *current_node = *head;

if (!head)
return (NULL);

new_node = malloc(sizeof(*new_node));
if (!new_node)
return (NULL);

new_node->n = number;
new_node->next = NULL;

while (current_node && current_node->n < number)
{
prev_node = current_node;
current_node = current_node->next;
}

if (!prev_node)
{
new_node->next = *head;
*head = new_node;
}
else
{
new_node->next = prev_node->next;
prev_node->next = new_node;
}

return (new_node);
}
