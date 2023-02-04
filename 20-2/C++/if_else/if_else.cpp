#include <iostream>
using namespace std;
int main()
{
	int a = 0, b = 0;
	char c;
	cout << "플마?\n";
	cin >> c;
	cout << "숫자 두개?\n";
	cin >> a >> b;
	if (c == '+') // ;를 입력하지 않는다!! 주의, 구문에서 괄호()는 필수이다.
		cout << "정답은 " << a + b;
	else if (c == '-') // 마찬가지로 ;를 입력안함!!
		cout << "정답은" << a - b;
	else
		cout << "ㄲㅈ";
	return 0;
}