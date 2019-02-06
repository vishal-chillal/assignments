#include<stdio.h>


int En(int *arr,int top,int start,int n,int val)
{
int  index=0
if(top==start)
{
	if(top!=-1)
	{
	printf("queue if full");i
		return -1;
	}	
}

if (start == -1) && (top == n-1){

	printf("queue if full");
		return -1;
}

if( top == -1){
	top = 0
}
index=top%n;
arr[index]=val;
top++;
return top;

}

int main()
{
int i,n,top=-1,start=-1,arr[10];
char optr[30];
scanf("%d",&n);
for(i=0;i<n;i++)
{
scanf("%s",optr);
if(optr=="En");
{
scanf("%d",&arr[i])
top=Enqueue(arr,top,start);
}
else if(optr=="De")
{
scanf("%d",&arr[i])
start=Dequeue(arr,start,top);
}
}
}



























