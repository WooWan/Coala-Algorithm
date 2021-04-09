#include <iostream>

using namespace std;

int dp[10001] = { 1, };

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	int t, k;
	cin >> t >> k;
	for (int i = 1; i <= k; i++) {
		int p, n;
		cin >> p >> n;
		for (int j = t; j >= 0; j--) {
			for (int k = 1; k <= n; k++) {
				int tp = p * k;
				if (j - tp >= 0) dp[j] += dp[j - tp];
			}
		}
	}
	cout << dp[t];
}