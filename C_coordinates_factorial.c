#include <stdio.h>
#include <math.h>

int factorial(int n){
    int one = 1;
    if (n == 0)
        return one;
    else if (n == 1)
        return one;
    return (factorial(n - 1)*n);
    }

float intrvl(float s1[3], float s2[3]){
    return sqrt((s2[0]-s1[0])*(s2[0]-s1[0]) + (s2[1]-s1[1])*(s2[1]-s1[1])  + (s2[2]-s1[2])*(s2[2]-s1[2]) );
}

int main(void){

    // 11

    int fac_val;
    do{
    printf("Please, enter the number which factorial you want to obtain: ");
    scanf("%d", &fac_val);
    }
    while(fac_val < 0);
    printf("factorial of %d equals %d: ", fac_val, factorial(fac_val));


    // 12

    // int A[3] = {1,1,1}, B[3] = {2,7,5}, C[3] = {4,6,8}, D[3] = {0,-2,-4}, E[3] = {-3,-3,-3}, F[3] = {7, 10, -2};
    // float spots[6][3] = {{1,1,1}, {2,7,5}, {4,6,8}, {0,-2,-4}, {-3,-3,-3}, {7, 10, -2}};
    // char spot[6] = {'A', 'B', 'C', 'D', 'E', 'F'};

    // // using binomial koef we know that there are 15 non-repeatable combinations of spot-couples
    // // so 
    // for (int i = 0; i < 6; i++){
    //     for (int j = 0; j < 6; j++){
    //             if ((i >= j)) // avoiding dublicates
    //                 continue;
    //             else
    //                 printf("%c-%c: %f\n", spot[i], spot[j], intrvl(spots[i],spots[j]));
    //         }
    //     }


    return 0;
}