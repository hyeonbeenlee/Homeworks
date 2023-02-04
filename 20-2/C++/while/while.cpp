#include <iostream>
using namespace std;
int main(void)
{
	float a, b; //플로팅변수 ab 설정
	cout << defaultfloat; //출력 고정소수점 모드, scientific->지수표기
	cout.precision(3); // 소숫점 자릿수 3개
	a = 1;
	while (a < 10) // a가 증가하는 반복루프 설정
		{
			b = 1; //b의 초기화
			while (b < 10) //b가 증가하는 반복루프 설정
			{
				cout << a << "*" << b << "=" << a * b << "\n"; //구구단 결과 출력
				b++; //먼저 출력하고 그다음에 b를 더해야 b=1일때의 값도 출력된다
			}
			cout << "\n"; //b루프 끝나면 a 더하기 전에 엔터 입력
			a++; // a*b에서 b가 1~9까지 루프 끝나면 a에 플러스 1
		}
}