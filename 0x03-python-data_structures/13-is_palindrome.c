#include "lists.h"

/**
 * palindrome- check if a sublist is a palindrome using recursion
 * @left: pointer to the leftmost node of the sublist
 * @right: pointer to the rightmost node of the sublist
 *
 * Return: 1 if the sublist is a palindrome, 0 otherwise
 */
int palindrome(listint_t **left, listint_t *right)
{
	int response;

	if (right != NULL)
	{
		response = palindrome(left, right->next);

		if (response != 0)
		{
			response = ((right ->n == (*left)->n);
			*left = (*left)->next;
			return response;
		}

		return (0);
	}

	return (1);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the head of the linked list
 *
 * Return: 1 if the linked list is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
	{
		return (0);
	}

	return palindrome(head, *head);
}
