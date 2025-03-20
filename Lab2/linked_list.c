#include <stdio.h>
#include <stdlib.h>

typedef struct list_el {
    double data;
    struct list_el *next;
    struct list_el *prev;
} list_el;

list_el *create_list_el(double data) {
    list_el *new_list_el = (list_el *)malloc(sizeof(list_el));
    new_list_el->data = data;
    new_list_el->next = NULL;
    new_list_el->prev = NULL;
    return new_list_el;
}

void insert_list_el(list_el **head, double data) {
    list_el *new_list_el = create_list_el(data);
    new_list_el->next = *head;
    new_list_el->prev = NULL;
    if (*head != NULL) {
        (*head)->prev = new_list_el;
    }
    *head = new_list_el;
}

list_el *get_last_list_el(list_el *head) {
    list_el *current = head;
    while (current != NULL && current->next != NULL) {
        current = current->next;
    }
    return current;
}

list_el *get_first_list_el(list_el *head) {
    list_el *current = head;
    while (current != NULL && current->prev != NULL) {
        current = current->prev;
    }
    return current;
}

//Calculate A1*An + A2*A(n-1) + ... + An*A1
double calculate(list_el *head, list_el *last, double S)
{
    if (head == NULL || last == NULL) return S;

    double head_data = head->data;
    double last_data = last->data;

    S += head_data * last_data;
    printf("a: %lf, b: %lf, S:%lf\n", head_data, last_data, S);
    return calculate(head->next, last->prev, S);
}

int main() {
    double S = 0;
    int n;
    printf("Enter the number of list_el: ");
    scanf("%d", &n);

    list_el *linked_list = NULL;
    
    printf("Enter the values of the list_els: ");
    for (int i = 0; i < n; i++) {
        double data;
        scanf("%lf", &data);
        insert_list_el(&linked_list, data);
    }
    
    list_el *head = get_first_list_el(linked_list);
    // Print created linked list
    printf("Linked list: ");
    while(head != NULL) {
        printf("%lf->", head->data);
        head = head->next;
    }
    printf("NULL\n");

    list_el *first_list_el = get_first_list_el(linked_list);
    list_el *last_list_el = get_last_list_el(linked_list);

    printf("Sum: %lf\n", calculate(first_list_el, last_list_el, S));

    while (linked_list != NULL) {
        list_el *current = linked_list;
        linked_list = linked_list->next;
        free(current);
    }
    return 0;
}