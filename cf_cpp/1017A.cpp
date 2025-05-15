#include <bits/stdc++.h>
// run command
// g++ -std=c++14 -O2 -Wall test.cpp -o test

using namespace std;
//typedef long long ll
//#define PB push_back

int main() {
    //solution here
    int n;
    
    cin >> n;
    cin.ignore();
    
    while (n--){
        string str;
        getline(cin, str);

        stringstream ss(str);
        string word;
        vector<string> words;

        while (ss >> word) {
            words.push_back(word);
        }
        string res;
        for (string w: words) {
            res += w[0];
        }
        
        cout << res << endl;

    }
    return 0;

}