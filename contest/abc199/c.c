#include <stdio.h>

int main(void) {
    int N, Q;
    
    scanf("%d", &N);
    char S[N];
    
    scanf("%s", S);
    scanf("%d", &Q);
    
    int T, A, B;
    int reverse = 0; // 前後ろが入れ替わっているかどうか
    
    for(int i = 0; i < Q; i++) {
        scanf("%d %d %d", &T, &A, &B);
        
        A--;
        B--;
        
        if(T == 2) {
            reverse = reverse == 0 ? 1 : 0;
        }
        
        if(reverse) {
            if(A < N) { A += N; }
            else { A -= N; }
            
            if(B < N) { B += N; }
            else { B -= N; }
        }
        
        char tmp = S[A];
        S[A] = S[B];
        S[B] = tmp;
    }
    
    if(reverse) {
        for(int i = N; i < N*2; i++) {
            printf("%c", S[i]);
        }
        
        for (int i = 0; i < N; i++) {
            printf("%c", S[i]);
        }
    } else {
        for(int i = 0; i < N*2; i++) {
            printf("%c", S[i]);
        }
    }
    
    printf("\n");
    
    return 0;
}
