#include<iostream>
#include<algorithm>
#include<vector>

using namespace std;

int segmentUnionLength(const vector<pair<int, int>>& seg)
{
	int n = seg.size();

	vector<pair<int, bool>> points(n * 2);
	for (int i = 0; i < n; i++)
	{
		points[i * 2] = make_pair(seg[i].first, false);
		points[i * 2 + 1] = make_pair(seg[i].second, true);
	}
		sort(points.begin(), points.end());
		int res = 0;
		int counter = 0;

		for (int i = 0; i <2* n; i++)
		{
			if (counter)
				res += (points[i].first) - (points[i - 1].first);

			(points[i].second) ? counter-- : counter++;

		}
		return res;
}

int main()
{

	vector<pair<int, int>> segments;
	segments.push_back(make_pair(2, 5));
	segments.push_back(make_pair(4, 8));
	segments.push_back(make_pair(9, 12));

	cout << segmentUnionLength(segments) << endl;
}