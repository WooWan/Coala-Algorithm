#include <iostream>

using namespace std;

int year[367];

int main() {
	int n;
	int maxdate = 0;
	cin >> n;
	for (int i = 0; i < n; i++) {
		int sd, ed;
		cin >> sd >> ed;
		maxdate = max(maxdate, ed);
		for (int j = sd; j <= ed; j++) {
			year[j]++;
		}
	}
	int ans = 0;
	int maxs = 0;
	int slength = 0;
	for (int i = 1; i <= maxdate + 1; i++) {
		if (year[i] == 0) {
			ans += maxs * slength;
			maxs = 0;
			slength = 0;
		}
		else {
			slength++;
			maxs = max(maxs, year[i]);
		}
	}
	cout << ans;
}