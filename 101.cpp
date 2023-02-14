#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>
/*
int main() {
	int num, digit;
	scanf("%d", &num);
	for (int i = 0; i < num; i++) { //第幾行 (第四行1331)
		for (int j = 1; j <= 3 * (num-i); j++) { //空格
			printf(" ");
		}
		for (int k = 0; k <= i; k++) {
			if (k == 0 || i == 0) { //第一行 和 每行第一個
				digit = 1;
				printf("%d", digit);
			}
			else {
				digit = digit * (i - k + 1) / k; //記得找規律(k-1和k的相連性)
				printf("%6d", digit);
			}
		}
		printf("\n");


	}
	return 0;
}*/
#include <stdio.h>
int main(void)
{
	int num1, denom1, num2, denom2, result_num, result_denom;
	printf("Enter first fraction: ");

	printf("Enter second fraction: ");
	scanf("%d/%d", &num2, &denom2);
	result_num = num1 * denom2 + num2 * denom1;
	result_denom = denom1 * denom2;
	printf("The sum is %d/%d\n", result_num, result_denom);
	return 0;
}