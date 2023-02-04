#include <iostream>
using namespace std;
int main(void)
{
	float a, b;
	char c;
	cout << "연산방법은?\n";
	cin >> c;
	cout << "숫자입력\n";
	cin >> a >> b;
	switch (c) //문자형변수 c에대해 검사
	{
	case '+': //세미콜론이 아닌 콜론으로 케이스를 부여해야한다
		cout << a + b;
		break; //switch-case문 탈출!
	case '-':
		cout << a - b;
		break;
	case '/':
		cout << a / b;
		break;
	case'*':
		cout << a * b;
		break;
	default: // 정의해준 case말고 이외의 경우 기본동작을 지정한다.
		cout << "뭐해이씨발럼아";
	}
}