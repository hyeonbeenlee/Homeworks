#include <iostream>

double Max(double x[10][1])
{
	double maximum;
	for (int i = 0; i < 9; i++)
	{
			maximum = x[i][0];
			if (x[i][0] < x[i+1][0])
			{
				maximum = x[i+1][0];
			}
			else
				maximum = maximum;
	}
	return maximum;
}

int main() {
	using namespace std;
	double x[10][1] = { {18},{2},{800},{12},{2},{2},{10},{15},{1},{0} };
	cout << Max(x);
	int i = 0;
	i++;
	return 0;
}