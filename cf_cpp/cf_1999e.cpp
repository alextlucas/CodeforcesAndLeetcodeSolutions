#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

int inp() {
    int x;
    cin >> x;
    return x;
}

vector<int> inlt() {
    int n;
    vector<int> result;
    while (cin >> n) {
        result.push_back(n);
    }
    return result;
}

vector<char> insr() {
    string s;
    cin >> s;
    vector<char> result(s.begin(), s.end());
    return result;
}

vector<int> invr() {
    vector<int> result;
    int x;
    while (cin >> x) {
        result.push_back(x);
    }
    return result;
}

void solve() {
    const int N = 200007;
    int l, r;
    cin >> l >> r;
    
    vector<long long> pref(N, 0);
    vector<int> cnt(N, 0);
    
    for (int i = 1; i < N - 1; i++) {
        cnt[i] = cnt[i / 3] + 1;
        pref[i + 1] = pref[i] + cnt[i];
    }
    
    r += 1;
    long long sum = pref[r] - pref[l];
    int mn = cnt[l];
    
    cout << sum + mn << endl;
}

int main() {
    int t = inp();
    while (t--) {
        solve();
    }
    return 0;
}
