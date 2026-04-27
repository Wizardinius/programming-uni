#include <stdio.h>
#include <math.h>

int main(void){

// 9 
// int Ar[5];

// // filling the array
// for (int i = 0; i < 5; i++){
//     printf("Please, enter the %d element of the array (only integers are required):\n", (i+1));
//     scanf("%d", &Ar[i]);
// }
// int *a = &Ar[0], *b = a+1, *c = b+1, *d = c+1, *e = d+1;

// // printing the whole array with pointers
// for(int k = 0; k < 5; k++)
//     {
//         void* address = Ar + k;  // получаем адрес k-го элемента массива.   Ar --- &Ar[0]
//         int value = *(Ar + k);   // получаем значение k-го элемента массива
//         printf("array[%d]: address=%p \t value=%d \n", k, address, value);
//     }

// // finding max 
// int max = *a;
// for (int j = 1; j < 5; j++){
//     if(*(Ar + j) > max)
//     max = *(Ar + j);
//     else
//     continue;
// }
// printf("maximum value of the array: %d\n", max);

// // changing the second element
// *b = *b + 100;

// // printing changed array with pointers
// for(int l = 0; l < 5; l++)
//     {
//         void* address = Ar + l;  // получаем адрес k-го элемента массива
//         int value = *(Ar + l);   // получаем значение k-го элемента массива
//         printf("array[%d]: address=%p \t value=%d \n", l, address, value);
//     }

// 10


float A, B, phi, pi = 3.1415926;
do{
    printf("Please, enter A triangle side: ");
    scanf("%f", &A);
}
while (A <= 0);

do{
    printf("Please, enter B triangle side: ");
    scanf("%f", &B);
}
while (B <= 0);

do{
    printf("Please, enter angle phi: ");
    scanf("%f", &phi);
}
while ((phi <= 0) || (phi > 180));

float S = 0.5 * A * B * sin(phi*(pi/180));

float C = sqrt(A*A + B*B - 2*A*B*cos(phi*(pi/180)));

printf("Area: %f, third side: %f", S, C);

}
