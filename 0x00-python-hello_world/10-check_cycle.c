#include "lists.h"

/**
 * check_cycle - Checks if linked list has a cycle
 * @list: A pointer to the head of the linked list
 * Return: 1 if the list has cycle, else 0
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
