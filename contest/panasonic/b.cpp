#include <iostream>
using namespace std;

int main(void){
    unsigned long a, b;
    cin >> a >> b;

    if(a == 1 || b == 1){
        cout << 1 << endl;
    }
    else if(a % 2 == 1 && b % 2 == 1){
        cout << (a * b / 2) + 1 << endl;
    }else{
        cout << a * b / 2 << endl;
    }
    return 0;
}
