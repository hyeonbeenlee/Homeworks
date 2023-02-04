#include <iostream>
using namespace std;
int main()
{
	for (char c = 'a'; c <= 'j'; c++) // 문자형c에 a를 초기값 부여, 알파벳순 j까지 증가시킨다
	{
		cout << c; //a부터j까지 출력한다
		for (int i = 0; i <= 5; i++) //a일때
			cout << i;//012345출력
		cout << "\n"; //a끝나면 한줄띄우기
	}
}