#include <iostream>
#include <queue>

using namespace std;

int basket[1000][1000];
int rm[4] = { -1,1,0,0 };
int cm[4] = { 0,0,-1,1 };

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	int M, N, cnt = 0;
	queue<pair<int, int>> v;
	cin >> M >> N;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			cin >> basket[i][j];
			if (basket[i][j] == 1) v.push(make_pair(i, j));
			else if (basket[i][j] == 0) cnt++;
		}
	}
	int ans = 0;
	while (!v.empty()) {
		int size = v.size();
		for (int i = 0; i < size; i++) {
			int r = v.front().first;
			int c = v.front().second;
			v.pop();
			for (int j = 0; j < 4; j++) {
				if (r + rm[j] < 0 || r + rm[j] >= N || c + cm[j] < 0 || c + cm[j] >= M) continue;
				if (basket[r + rm[j]][c + cm[j]] == 0) {
					v.push(make_pair(r + rm[j], c + cm[j]));
					basket[r + rm[j]][c + cm[j]] = 1;
					cnt--;
				}
			}
		}
		ans++;
	}
	if (cnt == 0) cout << ans - 1;
	else cout << -1;
}