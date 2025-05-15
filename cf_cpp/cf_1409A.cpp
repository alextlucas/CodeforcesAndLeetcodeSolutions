#include <bits/stdc++.h>

// run command
// g++ -O2 -Wall cf_1409A.cpp -o test
// /Users/alexlucas/Documents/codeforces/cpp/cf_1409A.cpp


using namespace std;
//typedef long long ll
//#define PB push_back



int main() {
    int n;
    cin >> n;

    while (n--){
        int a, b;
        cin >> a >> b;
        
        if (a > b) {
            int temp = a;
            a = b;
            b = temp;
;        }
        int answer = (b - a + 9)/ 10;
        cout << answer << endl;
        
    }
    
    return 0;
}

