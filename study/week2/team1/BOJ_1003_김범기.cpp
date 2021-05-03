#include <iostream>

#include <iostream>

using namespace std;

int dp[41];
int T, N;

int fibo(int n);

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	cin >> T;
	for (int i = 0; i < T; i++) {
		cin >> N;
		if (N == 0) cout << 1 << ' ' << 0 << '\n';
		else cout << fibo(N - 1) << ' ' << fibo(N) << '\n';
	}
}

int fibo(int n) {
	if (n <= 0) return dp[0];
	else if (n == 1) return dp[1] = 1;
	else {
		if (dp[n] != 0 && n > 0) return dp[n];
		else return dp[n] = fibo(n - 1) + fibo(n - 2);
	}
}
