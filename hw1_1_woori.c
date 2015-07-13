#include <stdio.h>
#include <stdlib.h>

typedef struct node *listptr;
typedef struct node{
	char data;
	listptr *link;
}node;

void push(listptr *top, char x){
	listptr temp;
	temp = (listptr)malloc(sizeof(node));
	if(!temp)
		printf("memory is full!\n");
	else{
		temp->data = x;
		temp->link = *top;
		*top = temp;
	}
}
char pop(listptr *top){
	char x;
	listptr temp =NULL;
	
	if(*top == NULL)
		return '$';
	else{
		temp = *top;
		x = temp->data;
		*top = temp->link;
		free(temp);
		return x;
	}
}

int main(void){
	node* top = NULL;
	//top = (listptr)malloc(sizeof(node));

	int t, check = 0;
	char x;

	while(check != -1){
		printf("어느 작업을 하시겠습니까? (1. push 2. pop 3. 종료) : ");
		scanf("%d", &t);
		fflush(stdin);
		switch(t){
			case 1:
				printf("어느 문자를 푸쉬하시겠습니까? :");
				scanf("%c", &x);
				fflush(stdin);
				push(&top, x);
				break;
			case 2:
				x = pop(&top);
				printf("다음 문자가 팝되었습니다 : %c", x);
				break;
			case 3:
				printf("프로그램을 종료합니다.");
				check = -1;
				break;
		}
		printf("\n");
	}
	return 0;	
}
