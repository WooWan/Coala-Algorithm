#include <iostream>
#include <queue>

using namespace std;

int h, w;
int map[50][50];
bool visit[50][50];
int rm[8] = { -1,-1,-1,0,0,1,1,1 };
int cm[8] = { -1,0,1,-1,1,-1,0,1 };

void dfs(int r, int c);

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	queue<pair<int, int>> q;
	while (true) {
		cin >> w >> h;
		if (w == 0 && h == 0) break;
		for (int i = 0; i < h; i++) {
			for (int j = 0; j < w; j++) {
				cin >> map[i][j];
				visit[i][j] = false;
			}
		}
		int island = 0;
		for (int i = 0; i < h; i++) {
			for (int j = 0; j < w; j++) {
				if (map[i][j] == 0 || visit[i][j]) continue;
				dfs(i, j);
				island++;
			}
		}
		cout << island << '\n';
	}
}

void dfs(int r, int c) {
	visit[r][c] = true;
	for (int i = 0; i < 8; i++) {
		if (r + rm[i] < 0 || r + rm[i] >= h || c + cm[i] < 0 || c + cm[i] >= w) continue;
		if (map[r + rm[i]][c + cm[i]] == 1 && !visit[r + rm[i]][c + cm[i]]) dfs(r + rm[i], c + cm[i]);
	}
}