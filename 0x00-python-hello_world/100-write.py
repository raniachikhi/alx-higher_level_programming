#include "lists.h"

/**
 * check_cycle - checks if a linked list contains a cycle
 * @list: linked list to check
 *
 * Return: 1 if the list has a cycle, 0 if it doesn t
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	/* If the list is empty, there can t be a cycle, so return 0 */
	if (!list)
		return (0);

	/*
	 * Use the slow and fast pointer approach to detect a cycle:
	 * Move slow one step at a time and fast two steps at a time.
	 * If there is a cycle, the fast pointer will eventually catch up
	 * to the slow pointer.
	 */
	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;

		/* If the slow and fast pointers meet, a cycle is detected */
		if (slow == fast)
			return (1);
	}

	/* If the loop completes without detecting a cycle, return 0 */
	return (0);
}
