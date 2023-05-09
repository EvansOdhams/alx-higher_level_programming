#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
* struct listint_s - singly linked list
* @n: integer value stored in the node
* @next: pointer to the next node in the list
*
* Description: singly linked list node structure
* for Holberton project
*/
typedef struct listint_s
{
int n;
struct listint_s *next;
} listint_t;

/**
* print_listint - prints all the elements of a listint_t list
* @h: pointer to the head of the list
*
* Return: the number of nodes in the list
*/
size_t print_listint(const listint_t *h);

/**
* add_nodeint - adds a new node at the beginning of a listint_t list
* @head: pointer to a pointer to the first node of the list
* @n: integer value to be stored in the new node
*
* Return: the address of the new element, or NULL if it fails
*/
listint_t *add_nodeint(listint_t **head, const int n);

/**
* free_listint - frees a listint_t list
* @head: pointer to the head of the list
*
* Return: void
*/
void free_listint(listint_t *head);

/**
* check_cycle - checks if a linked list contains a cycle
* @list: pointer to the head of the list
*
* Return: 0 if there is no cycle, 1 if there is a cycle
*/
int check_cycle(listint_t *list);

#endif /* LISTS_H */

