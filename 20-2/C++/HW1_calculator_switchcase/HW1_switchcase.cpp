#include <iostream>
using namespace std;
double Plus(double x, double y) //덧셈함수 정의
{
	return x + y;
}

double Minus(double x, double y) //뺄셈함수 정의
{
	return x - y;
}

double Divide(double x, double y) //나눗셈함수 정의
{
	if (y != 0)
		return x / y;
	else
		cout << "0으로 나눌 수 없습니다" << endl; //0으로 나눠질 경우 경고문 출력
}

double Multiply(double x, double y) //곱셈함수 정의
{
	return x * y;
}

int main() //메인함수 정의, 계산기 코드 시작
{
	int type, fixednumber, lastchoice; // 선택지용 정수변수 선언
	double x, y; //계산 시 사용될 실수변수 선언
	char c; //계산 연산자용 문자변수 선언
	cout << "■■■■■■■■■■■■■■■■■■■■■■■■■■■■■" << endl;
	cout << "■                                                      ■" << endl;
	cout << "■  사칙연산 계산 프로그램 coded by. 2015100767 이현빈  ■" << endl;
	cout << "■                    switch-case ver.                  ■" << endl;// 직접 정성을 다해 만들었습니다.....
	cout << "■                                                      ■" << endl;
	cout << "■■■■■■■■■■■■■■■■■■■■■■■■■■■■■" << endl << endl;

	////////////////////////////////// 계산 시 출력 형식을 지정함 /////////////////////////////////////////
	do //반복계산을 위한 루프문 lastchoice==2
	{
		cout << "사용할 출력 형식을 선택해주세요" << endl << "1) 고정 소수점" << endl << "2) 지수표기" << endl << "3) 고정 유효숫자" << endl;

		do
		{
			cin >> type; //출력 형식을 입력받는다
		switch (type)
		{
		case 1:
			cout << fixed; //고정소수점 표기
			cout << "소수점 아래 몇 자리까지 표기할까요?" << endl;
			cin >> fixednumber;
			cout.precision(fixednumber);
			break;
		case 2:
			cout << scientific; //지수표기
			cout << "소수점 아래 몇 자리까지 표기할까요?" << endl;
			cin >> fixednumber;
			cout.precision(fixednumber); //fixed, scientific에서 이는 소수점 아래 숫자를 설정함
			break;
		case 3:
			cout << defaultfloat; //고정 유효숫자 표기
			cout << "유효숫자 몇 개를 사용할까요? (유효숫자 이하의 자릿수는 절삭됩니다.)" << endl;
			cin >> fixednumber; //자릿수를 입력받음
			cout.precision(fixednumber); // default 출력형식에서는 이는 유효숫자 수를 설정함
			break;
		default:
			cout << "숫자 1 2 3 중 하나를 입력해주세요" << endl;
			break;
		}
		} while (type != 1 && type != 2 && type != 3); //입력받은 type이 1,2,3이 아닐경우 루프 반복)

		////////////////////// 계산 입력 시작 //////////////////////////
		do // 재계산을 위한 루프문 lastchoice==1
		{
			do // 입력오류 시 계산과정 재시작 위한 루프문
			{
					cout << "수식을 입력하세요. 2개의 숫자항만 유효합니다" << endl;
					cin >> x >> c >> y; //숫자,연산자,숫자를 입력받는다.
					switch (c)
					{
					case '+':
						cout << x << c << y << " 는 " << Plus(x, y) << " 입니다." << endl;
						break;
					case '-':
						cout << x << c << y << " 는 " << Minus(x, y) << " 입니다." << endl;
						break;
					case '/':
						if (y != 0)
							cout << x << c << y << " 는 " << Divide(x, y) << " 입니다." << endl;
						else
							cout << Divide(x, y) << endl; //Divide함수에서 0으로 나눠질 때 경고문을 출력하도록 세팅하였기에 따로 경고문 입력 불필요.
						break;
					case '*':
						cout << x << c << y << " 는 " << Multiply(x, y) << " 입니다." << endl;
						break;
					default: //모든 case가 아닐 경우 진입
						cout << "올바른 식을 입력해주세요." << endl;
						break; // switch-case문 탈출한다
					}
			} while (c != '+' && c != '-' && c != '*' && c != '/'); // default에서 나왔을 때 c가 +-*/ 중 하나가 아니면 계속 반복

			cout << endl << "계산이 끝났습니다. 아래에서 원하는 작업을 선택해주세요." << endl;
			cout << "1) 계속 계산하기" << endl << "2) 출력형식 변경하고 계산하기" << endl << "3) 종료하기" << endl;
			cin >> lastchoice;
			cout << endl; //다음 반복계산 수행 시 한줄 띄운다
			while (lastchoice != 1 && lastchoice != 2 && lastchoice != 3) //선택지 입력 제대로 안됬을 때 루프로 진입
			{
				cout << "1 2 3 중에서 입력해주세요" << endl;
				cin >> lastchoice;
				if (lastchoice == 1 || lastchoice == 2 || lastchoice == 3) //1 2 3 중 하나가 입력되면 루프 탈출한다
					break;
			}
	} while (lastchoice == 1); //1일 경우 루프
	} while (lastchoice == 2); //2일 경우 루프
	if (lastchoice == 3) //3일 경우 메인함수에 0 반환 후 종료함
		return 0;
}