#include <string>
#include <iostream>
using namespace std;

int main(){
    int n, i;
    string s;
    cin >> n;
    cin >> s;
    int count = 0;
    for(i = 0; i < n - 2; i++){
        if(s.substr(i, 3) == "ABC") count++;
    }
    cout << count << endl;

    return 0;
}
