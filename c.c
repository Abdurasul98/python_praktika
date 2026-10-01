#include <stdio.h>

// int main() {

//     int boshlash = 1;
//     int tugash = 10;

//     for (boshlash; boshlash <= tugash; boshlash++) {
//         if ( boshlash % 2 == 0) {
//             printf("%d \n",boshlash);
//         }
//     }

//     return 0;
// }




// int main() {

//     int son;

//     printf("Son kiriting: ");
//     scanf("%d", &son);

//     for (int i = 1; i <= son; i++) {

//         if (i % 3 == 0 && i % 5 == 0) {
//             printf("%d - Bu son 3 ga va 5 ga bo'linadi\n", i);

//         } else if (i % 5 == 0) {
//             printf("%d - Bu son 5 ga bo'linadi\n", i);

//         } else if (i % 3 == 0) {
//             printf("%d - Bu son 3 ga bo'linadi\n", i);
//         }
//     }

//     return 0;
// }




// int main () {
//     int son;
//     printf("Son kiriting: ");
//     scanf("%d", &son);

//     for (int i = 1; i <= son ; i++) {
//         if ( i % 3 == 0 ) {
//             printf(" %d <- Bu son 3 ga bo'linadi \n",i);

//         } else if ( i % 2 == 0 ) {
//             printf(" %d <- Juft \n",i);

//         } else if ( i % 2 == 1 ) {
//             printf(" %d <- Toq \n",i);
//         }
//     }


//     return 0;
// }


int main () {

    int son;
    printf("Son kiriting: ");
    scanf("%d", &son);

    for (int i = 1; i <= son ;i++) {

        if (i % 2 == 0) {
            if ( i % 2 == 0 && i % 4 == 0) {
                printf("{%d}Juft va 4 ga bo'linadi", i);
            } else {
                printf("%d", i);
            }
        } else if (i % 2 == 1) {
            
        }
    }

    return 0;
}