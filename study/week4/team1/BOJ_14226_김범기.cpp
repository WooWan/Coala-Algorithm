#include <iostream>
#include <queue>

using namespace std;

struct s { int time; int num; int copy; };
int visit[2000][2000];

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	int S;
	cin >> S;
	for (int i = 0; i < S * 2; i++) {
		for (int j = 0; j < S * 2; j++) visit[i][j] = 3000;
	}
	visit[1][0] = 0;
	queue<s> q;
	q.push({ 0,1,0 });
	while (!q.empty()) {
		int t = q.front().time;
		int n = q.front().num;
		int c = q.front().copy;
		q.pop();
		if (n == S) {
			cout << t;
			break;
		}
		int nt, nn, nc;
		nt = t + 1;
		nn = n - 1;
		nc = c;
		if (nn >= 0 && nt < visit[nn][nc]) {
			visit[nn][nc] = nt;
			q.push({ nt,nn,nc });
		}
		nn = n;
		nc = n;
		if (nc < 2 * S && nt < visit[nn][nc]) {
			visit[nn][nc] = nt;
			q.push({ nt,nn,nc });
		}
		nn = n + c;
		nc = c;
		if (nn < 2 * S && nt < visit[nn][nc]) {
			visit[nn][nc] = nt;
			q.push({ nt,nn,nc });
		}
	}
}
