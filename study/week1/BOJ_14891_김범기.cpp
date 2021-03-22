#include <iostream>
#include <string>
#include <cmath>

using namespace std;

string t[4];
void turn(int index, int direction, int call);

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	for (int i = 0; i < 4; i++) cin >> t[i];
	int k;
	cin >> k;
	for (int i = 0; i < k; i++) {
		int n, d;
		cin >> n >> d;
		turn(n - 1, d, -1);
	}
	int score = 0;
	for (int i = 0; i < 4; i++) if (t[i][0] == '1') score += pow(2, i);
	cout << score;
}

void turn(int index, int direction, int call) {
	string temp = t[index];
	if (direction == 1) t[index] = temp[7] + temp.substr(0, 7);

	else t[index] = temp.substr(1, 7) + temp[0];
	if (index - 1 >= 0 && index - 1 != call && temp[6] != t[index - 1][2]) turn(index - 1, direction * -1, index);
	if (index + 1 <= 3 && index + 1 != call && temp[2] != t[index + 1][6]) turn(index + 1, direction * -1, index);
}