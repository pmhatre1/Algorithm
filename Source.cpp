#include<iostream>
#include<algorithm>
using namespace std;
struct Point
{
	int x;
	int y;
};

//Check the orientation of the lines
// 0 -> p,q,r are collinear
// 1 -> Clockwise
// 2 -> Anti clockwise

int orientation(Point p, Point q, Point r)
{
	int val = (q.y - p.y) * (r.x - q.x) - (r.y - q.y) * (q.x - p.x);

	if (val == 0)return 0;

	return (val > 0) ? 1 : 2;
}

bool onSegment(Point p, Point q, Point r)
{
	if (q.x <= max(p.x, r.x) && q.x >= min(p.x, r.x) &&
		q.y <= max(p.y, r.y) && q.y >= min(p.y, r.y))
		return true;

	return false;
}


// doIntersect Function returns true if the line p1q1 and p2q2 intersect
bool doIntersect(Point p1, Point q1, Point p2, Point q2)
{

// Write all the possible orientation of the points

	int o1 = orientation(p1, q1, p2);
	int o2 = orientation(p1, q1, q2);
	int o3 = orientation(p2, q2, p1);
	int o4 = orientation(p2, q2, q1);

	if (o1 != o2 && o3 != o4)
		return true;

	if (o1 == 0 && onSegment(p1, p2, q1)) return true;

	// p1, q1 and q2 are colinear and q2 lies on segment p1q1
	if (o2 == 0 && onSegment(p1, q2, q1)) return true;

	// p2, q2 and p1 are colinear and p1 lies on segment p2q2
	if (o3 == 0 && onSegment(p2, p1, q2)) return true;

	// p2, q2 and q1 are colinear and q1 lies on segment p2q2
	if (o4 == 0 && onSegment(p2, q1, q2)) return true;

	return false; // Doesn't fall in any of the above cases

}

int main()
{
	struct Point p1 = { 1,1 }, q1 = { 10,1 };
	struct Point p2 = { 1,2 }, q2 = { 10,2 };

	doIntersect(p1, q1, p2, q2) ? cout << "Yes\n" : cout << "No\n";

}