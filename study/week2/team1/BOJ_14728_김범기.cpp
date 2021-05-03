#include <iostream>

using namespace std;

pair<int,int> arr[101];
int dp[101][10001];

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	int N, T;
	cin >> N >> T;
	for (int i = 1; i <= N; i++) {
		cin >> arr[i].first >> arr[i].second;
	}
	for (int i = 1; i <= N; i++) {
		for (int j = 0; j <= T; j++) {
			if (j >= arr[i].first) dp[i][j] = max(dp[i - 1][j - arr[i].first] + arr[i].second, dp[i-1][j]);
			else dp[i][j] = dp[i - 1][j];
		}
	}
	cout << dp[N][T];
}
