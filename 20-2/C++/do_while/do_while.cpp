#include <iostream>
using namespace std;
int main(void)
{
	int choice;
	do
	{
		cout << "1\n2\n3\n";
		cin >> choice;
	} while (choice < 4);
		cout << "Your choice is " << choice << ".\n";
}