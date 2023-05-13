#include "lists.h"

listint_t *reverse_listint(listint_t **head);
int is_palindrome(listint_t **head);

/**
* reverse_listint - Reverses a singly-linked list.
* @head: A pointer to the starting node of the list to reverse.
* Return: A pointer to the head of the reversed list.
*/
listint_t *reverse_listint(listint_t **head)
{
listint_t *current_node = *head, *previous_node = NULL, *next_node;

while (current_node != NULL)
{
next_node = current_node->next;
current_node->next = previous_node;
previous_node = current_node;
current_node = next_node;
}

*head = previous_node;
return (*head);
}

/**
* is_palindrome - Checks if a singly linked list is a palindrome.
* @head: A pointer to the head of the linked list.
*
* Return: If the linked list is not a palindrome - 0.
*         If the linked list is a palindrome - 1.
*/
int is_palindrome(listint_t **head)
{
listint_t *slow = *head, *fast = *head, *prev = NULL, *tmp;

/* Traverse the linked list to find thefirst half of the list */
while (fast && fast->next)
{
fast = fast->next->next;
tmp = slow->next;
slow->next = prev;
prev = slow;
slow = tmp;
}
/* If the linked list has an odd number of nodes,to the next node */
if (fast)
slow = slow->next;

/* Compare the first half of the list with the second half of the list */
while (slow)
{
if (prev->n != slow->n)
return (0);
prev = prev->next;
slow = slow->next;
}

return (1);
}
