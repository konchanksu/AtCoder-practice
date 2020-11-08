#include <stdio.h>

double aaa(double a){
    return (a + 1.0) / 2.0;
}

int main(void){
    int n, k, i;
    scanf("%d %d", &n, &k);
    double p[n];
    double ans = 0.0, tmp = 0.0;
    for(i = 0; i < n; i++){
        scanf("%lf", &p[i]);
        p[i] = aaa(p[i]);
    }

    for(i = 0; i < k; i++){
        ans += p[i];
    }
    tmp = ans;

    for(i = k; i < n; i++){
        tmp += (p[i] - p[i - k]);
        if(ans < tmp) ans = tmp;
    }

    printf("%.8f\n", ans);
    return 0;
}
