#include <iostream>
using namespace std;

int ruijo(int n, int ans){
    if(n == 1){
        return ans + 1;
    }
    return ruijo(n - 1, ans + n);
}

int main(){
    int n, m;
    cin >> n >> m;

    int ans = 0;
    if (n != 1 && n != 0) ans += ruijo(n - 1, 0);
    if (m != 1 && m != 0) ans += ruijo(m - 1, 0);

    cout << ans << endl;

    return 0;
}
