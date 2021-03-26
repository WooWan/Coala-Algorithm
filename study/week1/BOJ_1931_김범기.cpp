#include <iostream>
#include <queue>

using namespace std;

struct meeting { int start; int end; };

struct compare {
	bool operator()(meeting& a, meeting& b) {
		if (a.end != b.end) return a.end > b.end;
		else return a.start > b.start;
	}
};

int main() {
	int n;
	cin >> n;
	priority_queue<meeting, vector<meeting>, compare> pq;
	for (int i = 0; i < n; i++) {
		int s, e;
		cin >> s >> e;
		pq.push({ s,e });
	}
	int now = 0;
	int ans = 0;
	while (!pq.empty()) {
		if (pq.top().start < now) pq.pop();
		else {
			now = pq.top().end;
			pq.pop();
			ans++;
		}
	}
	cout << ans;
}