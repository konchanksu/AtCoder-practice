#include <iostream>
#define rep(i, n) for(int(i)=(0); (i) < (n); (i)++)
using namespace std;

int main(){
    long long n, i;
    cin >> n;
    long long a[n];
    rep(i, n) cin >> a[i];
    
    if(n % 2 == 0){
        long long tmp1 = 0, tmp2 = 0;
        rep(i, n){
            if(i % 2 == 0) tmp1 += a[i];
            else tmp2 += a[i];
        }
        cout << max(tmp1, tmp2) << endl;
    }else{
        long long dp[n + 1][int(n / 2) + 1];
        dp[0][0] = 0;
        dp[1][0] = 0;
        dp[2][0] = 0;
        dp[1][1] = a[0];
        for(i = 2; i <= n; i++){
            for(int j = 0; j <= 1; j++){
                if(int((i - 1) / 2) + j > int(n / 2)) continue;
                if(int((i - 1) / 2) + j == 0){
                    dp[i][int((i - 1) / 2) + j] = 0;
                }else if((int((i - 1) / 2) + j) * 2 > i){
                    dp[i][int((i - 1) / 2) + j] = dp[i - 2][int((i - 1) / 2) + j - 1] + a[i];
                }
                else{
                    dp[i][int((i - 1) / 2) + j] = max(dp[i - 1][int((i - 1) / 2) + j], dp[i - 2][int((i - 1) / 2) + j - 1] + a[i - 1]);
                }
            }
        }
        cout << dp[n][int(n / 2)] << endl;
    }
    
    return 0;
}
