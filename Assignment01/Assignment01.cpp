#include<stdio.h>
int main(void){
	double NUM[100];
	double temp;
	int i,k,n;
	
	printf("Please input how many numbers would you like to sort.\n");
	scanf("%d",&n);
	
	printf("Please input the numbers you would like to sort.\n");
	for(i=0;i<n;i++)
		scanf("%lf",&NUM[i]);
	
	for(k=0;k<n;k++){
		for(i=0;i<n-k-1;i++){
			if(NUM[i]>NUM[i+1]){
				temp=NUM[i];
				NUM[i]=NUM[i+1];
				NUM[i+1]=temp;
			}
		}
	}
	
	for(i=0;i<n;i++)
		printf("%6.2f\n",NUM[i]);
		
	return 0;
}
