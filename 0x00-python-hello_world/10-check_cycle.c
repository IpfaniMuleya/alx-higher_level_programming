#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle
 * @list: pointer to the head of the list
 * Return: 1 if there is a cycle, 0 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *current_node = list;
	listint_t *far_node = list;

	while (current_node != NULL && far_node != NULL && far_node->next != NULL)
	{
		current_node = current_node->next;
		far_node = far_node->next;

		if (current_node == far_node)
			return (1);
	}

	return (0);
}
