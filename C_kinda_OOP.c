#include <stdio.h>

union user_permissions{
    struct {
        unsigned char read : 1;
        unsigned char write  : 1;
        unsigned char execute : 1;
        unsigned char delete : 1;
        unsigned char priority : 1;
    } bits;
    unsigned char Data;
};

void input_perms(union user_permissions *perm) {
    int temp;  // temp var for entering
    
    printf("Enter 0 or 1 to give or deny permission:\n");
    
    printf("Reading permission: ");
    scanf("%d", &temp);
    perm->bits.read = temp;  // Преобразуем в 0 или 1
    
    printf("Writing permission: ");
    scanf("%d", &temp);
    perm->bits.write = temp;
    
    printf("Execution permission: ");
    scanf("%d", &temp);
    perm->bits.execute = temp;
    
    printf("Deleting permission: ");
    scanf("%d", &temp);
    perm->bits.delete = temp;
    
    printf("Prioritising permission: ");
    scanf("%d", &temp);
    perm->bits.priority = temp;
    
    printf("Done\n\n");
}

int calc_cost(union user_permissions perm){
    int edinichki = 0;
    int cost = 0;
    
    edinichki = perm.bits.read + perm.bits.write + perm.bits.execute + perm.bits.delete;

    // total cost = perms*10 + 50 in case priority
    if (perm.bits.priority) {
        cost = edinichki * 10 + 50;
    }
    else{
        cost = edinichki * 10;
    }
    return cost;
}

void reset_perms(union user_permissions *perms) {
    perms->Data = 0; 
    printf("reset is done.\n\n");
}

void print_perms(union user_permissions perms) {
    printf("provided permissions:\n");
    printf("read: %d\n", perms.bits.read);
    printf("write: %d\n", perms.bits.write);
    printf("execute: %d\n", perms.bits.execute);
    printf("delete: %d\n", perms.bits.delete);
    printf("priority: %d\n", perms.bits.priority);
    
    // check up of 4 essential perms
    int allActive = perms.bits.read && perms.bits.write && perms.bits.execute && perms.bits.delete;
    printf("\nallActive: %d\n", allActive);
    
    // Data value
    printf("\nData: %d\n\n", perms.Data);
}

int main(void){
    union user_permissions perms; 
    
    input_perms(&perms); // 
    
    print_perms(perms);
    
    int cost = calc_cost(perms);
    printf("Permissions total cost: %d\n\n", cost);
    
    reset_perms(&perms);
    
    print_perms(perms);
    
    cost = calc_cost(perms);
    printf("Permissions total cost after reset: %d\n", cost);
    
    return 0;
}
