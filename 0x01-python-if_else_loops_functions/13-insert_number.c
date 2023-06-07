#include "lists.h"
#include <stdio.h>

/**
 * insert_node - insert number
 * @head: Head of linked list
 * @number: number to insert
 * Return: new node address or NULL if failure
 */

listint_t *insert_node(listint_t **head, int number)
{
	int flag = 0;
	listint_t *new = NULL, *temp = NULL, *new2 = NULL;

	if (head == NULL)
		return (NULL);
	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number, new->next = NULL;
	if (*head == NULL)
	{
		*head = new;
		return (*head);
	}
	temp = *head;
	if (number <= temp->n)
	{
		new->next = temp, *head = new;
		return (*head);
	}
	if (number > temp->n && !temp->next)
	{
		temp->next = new;
		return (new);
	}
	new2 = temp->next;
	while (temp)
	{
		if (!new2)
			temp->next = new, flag = 1;
		else if (new2->n == number)
			temp->next = new, new->next = new2, flag = 1;
		else if (new2->n > number && temp->n < number)
			temp->next = new, new->next = new2, flag = 1;
		if (flag)
			break;
		new2 = new2->next, temp = temp->next;
	}
	return (new);
}
