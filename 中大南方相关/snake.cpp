#include<stdio.h>
#include<graphics.h>
#include<easyx.h>
#include<Windows.h>
#include<conio.h>
#include<time.h>


//储存每节蛇的坐标。
int snake[20][2] = { 0 };
//蛇有多少节
int len = 3;
//控制食物的坐标啦
int FoodX = 0;
int FoodY = 0;

//初始化
void init() {
	//第一节的XY坐标，即：（2,0）
	snake[0][0] = 2;
	snake[0][1] = 0;
	//第二节的XY坐标，即：（1,0）
	snake[1][0] = 1;
	snake[1][1] = 0;

	snake[2][0] = 0;
	snake[2][1] = 0;
}

//画背景~
void DrawBackground() {
	//画竖线
	for (int i = 0; i < 420; i += 20) {
		line(120 + i, 40, 120 + i, 440);
	}
	//画横线
	for (int i = 0; i < 420; i += 20) {
		line(120, 40 + i, 520, 40 + i);
	}
}

//画蛇
void DrawSnake() {
	setfillcolor(WHITE);
	int x1, y1, x2, y2;
	for (int i = 0; i < len; i++){
		x1 = 121 + 20 * snake[i][0];
		y1 = 41 + 20 * snake[i][1];
		x2 = x1 + 18;
		y2 = y1 + 18;
		solidrectangle(x1,y1,x2,y2);
	}
}

//让蛇动
void move(int where) {
	//当前蛇尾巴的坐标
	int TailX = snake[len - 1][0];
	int TailY = snake[len - 1][1];
	//先擦除上一条蛇的尾巴
	setfillcolor(BLACK);
	int x = 121 + 20 * snake[len - 1][0];
	int y = 41 + 20 * snake[len - 1][1];
	solidrectangle(x,y,x+18,y+18);
	setfillcolor(WHITE);
	//更新整条蛇的坐标
	int length =len;
	while(--length) {
		//倒数第二节的X坐标等于倒数第一节的坐标
		snake[length][0] = snake[length - 1][0];
		//Y坐标同上
		snake[length][1] = snake[length - 1][1];
	}
	//更新蛇头坐标
	//1234分别代表上下左右
	switch (where){
	case 1:snake[0][1]-=1; break;
	case 2:snake[0][1]+=1; break;
	case 3:snake[0][0]-=1; break;
	case 4:snake[0][0]+=1; break;
	}
	//画蛇头
	x = 121 + 20 * snake[0][0];
	y = 41 + 20 * snake[0][1];
	solidrectangle(x, y,x + 18, y + 18);
	//如果吃到食物
	if (snake[0][0] == FoodX & snake[0][1] == FoodY) {
		len++;
		snake[len - 1][0] = TailX;
		snake[len - 1][1] = TailY;
		solidrectangle(x, y, x + 18, y + 18);
		//生成新的食物
		srand((unsigned)time(NULL));
		FoodX = 3 + rand() % 17;
		FoodY = 3 + rand() % 17;
		setfillcolor(RED);
		solidrectangle(121 + 20 * FoodX, 41 + 20 * FoodY, 139 + 20 * FoodX, 59 + 20 * FoodY);
	}

}

//生成食物
void food() {
	srand((unsigned)time(NULL));
	FoodX = 3 + rand() % 17;
	FoodY = 3 + rand() % 17;
	setfillcolor(RED);
	solidrectangle(121+20*FoodX,41+20*FoodY, 139 + 20 * FoodX, 59 + 20 * FoodY);
}

//是否死亡，死亡返回0，while就会跳出循环，否则返回1
int die() {
	if (snake[0][0] < 0 || snake[0][0]>20)
		return 0;
	if (snake[0][1] < 0 || snake[0][1]>20)
		return 0;
	return 1;
}

int main() {
	initgraph(640, 480);
	init();
	DrawBackground();
	DrawSnake();
	food();
	char key = '0';
	int now = 4;
	while (die()) {
		for (; kbhit();)  key = getch();
		switch (key) {
		case 'w':move(1);  break;
		case 's':move(2);  break;
		case 'a':move(3);  break;
		case 'd':move(4);  break;
		default:move(4); break;
		}
		Sleep(1000);
	}
	//清空整个屏幕
	cleardevice();
	closegraph();
	return 0;
}