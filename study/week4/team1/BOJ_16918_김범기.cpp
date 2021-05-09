#include <iostream>
#include <string>

using namespace std;

int map[200][200];
int rm[4] = { 1,-1,0,0 };
int cm[4] = { 0,0,1,-1 };

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	int R, C, N;
	cin >> R >> C >> N;
	for (int i = 0; i < R; i++) {
		string input;
		cin >> input;
		for (int j = 0; j < C; j++) {
			if (input.substr(j, 1) == "O") {
				map[i][j] = 3;
			}
			else {
				map[i][j] = -1;
			}
		}
	}
	for (int time = 2; time <= N; time++) {
		if (time % 2 == 0) {
			for (int i = 0; i < R; i++) {
				for (int j = 0; j < C; j++) {
					if (map[i][j] == -1) map[i][j] = time + 3;
				}
			}
		}
		else {
			for (int i = 0; i < R; i++) {
				for (int j = 0; j < C; j++) {
					if (map[i][j] == time) {
						map[i][j] = -1;
						for (int k = 0; k < 4; k++) {
							int r = i + rm[k];
							int c = j + cm[k];
							if (r < 0 || r >= R || c < 0 || c >= C || map[r][c] == time) continue;
							map[r][c] = -1;
						}
					}
				}
			}
		}
	}
	for (int i = 0; i < R; i++) {
		for (int j = 0; j < C; j++) {
			if (map[i][j] != -1) cout << 'O';
			else cout << '.';
		}
		cout << '\n';
	}
}