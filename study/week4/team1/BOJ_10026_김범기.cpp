#include <iostream>
#include <queue>

using namespace std;

int N;
char picture[100][100];
bool visit[100][100];
char input[100];
int rm[4] = { 1,-1,0,0 };
int cm[4] = { 0,0,1,-1 };
int ans[2] = { 0,0 };

void dfs(int r, int c);

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	int ans[2] = { 0,0 };
	cin >> N;
	for (int i = 0; i < N; i++) {
		cin >> input;
		for (int j = 0; j < N; j++) {
			picture[i][j] = input[j];
			visit[i][j] = false;
		}
	}
	int t = 0;
	while (true) {
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				if (visit[i][j]) continue;
				dfs(i, j);
				ans[t]++;
			}
		}
		if (t == 1) break;
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				visit[i][j] = false;
				if (picture[i][j] == 'G') picture[i][j] = 'R';
			}
		}
		t++;
	}
	cout << ans[0] << " " << ans[1];
}

void dfs(int r, int c) {
	visit[r][c] = true;
	char color = picture[r][c];
	for (int k = 0; k < 4; k++) {
		int nr = r + rm[k];
		int nc = c + cm[k];
		if (nr < 0 || nr >= N || nc < 0 || nc >= N) continue;
		if (picture[nr][nc] == color && !visit[nr][nc]) dfs(nr, nc);
	}
}