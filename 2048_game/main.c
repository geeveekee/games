#include<stdio.h>
#include<stdlib.h>

int board[5][5];
// directions respectively for up right down left
int dirLine[] = {1, 0, -1, 0};
int dirColumn[] = {0, 1, 0, -1};

struct pos
{
    int a;
    int b;
};

struct pos generateUnoccupiedPos()
{
    struct pos sus;
    sus.a = rand() % 5;
    sus.b = rand() % 5;

    return sus;
}

int check(int a, int b)
{
    if (board[a][b] != 0)
    {
        return 0;
    }
    else
    {
        return 1;
    }
}
void addPiece()
{
    int flag;
    struct pos theShixx;
    theShixx = generateUnoccupiedPos();
    printf("%d", theShixx.a);
    printf("%d", theShixx.b);
    flag = check(theShixx.a, theShixx.b);
    printf("%d", flag);
    if(flag)
    {
        board[theShixx.a][theShixx.b] = 2;
        //addPiece();
    }
    else
        addPiece();
}

void newGame()
{
    for(int i =0; i<5; i++){
        for(int j =0 ; j<5; j++)
            board[i][j] = 0;
    }
    addPiece();
}

void printGraphics()
{
    system("cls");
    char val = '.';
    for(int i =0; i<5; ++i)
        {
        for(int j = 0; j<5 ; ++j)
            if(board[i][j] == 0)
                printf("%3c", val);
            else
                printf("%3d", board[i][j]);
        printf("\n");
        }
    printf("n: new game, w: up, a: left, s: down, d: right, q: quit \n");
}

int canMove(int line, int col, int nextLine, int nextCol)
{
    if(nextLine < 0 || nextCol < 0 || nextLine >= 5 || nextCol >= 5 || (board[line][col] != board[nextLine][nextCol]) && (board[nextLine][nextCol] != 0))
    {
        return 0;
    }
    return 1;
}

void applyMove(int direction)
{
   int startLine = 0, startCol = 0, lineStep = 1, colStep = 1;
   if(direction == 0)
   {
       startLine = 4;
       lineStep = -1;
   }
   if(direction == 1)
   {
       startCol = 4;
       colStep = -1;
   }
   int movePossible = 0, canAddPiece = 0;
   do{
        movePossible = 0;
   for(int i = startLine; i>=0 && i <5; i+=lineStep)
    for(int j = startCol; j >= 0 && j<5; j += colStep){
    int nextI = i + dirLine[direction], nextJ = j + dirColumn[direction];
    if(board[i][j] && canMove(i, j, nextI, nextJ))
    {
        board[nextI][nextJ] += board[i][j];
        board[i][j] = 0;
        movePossible = canAddPiece = 1;
    }
   }
   }
   while(movePossible);
   if (canAddPiece)
    addPiece();

}


int main()
{
    char commandToDir[128];
    commandToDir['s'] = 0;
    commandToDir['d'] = 1;
    commandToDir['w'] = 2;
    commandToDir['a'] = 3;
    int currentDirection = 5;
    int gameOver = 0;
    char command;
    while(1)
    {
        printf("called \n");
        printf("%d \n", currentDirection);
        printGraphics();
        //genious
        scanf(" %c", &command);
        //genious
        if (command == 'q')
            //gameOver = 1;
            break;
        else if (command == 'n')
            newGame();
        else if (command == 'a' || command == 's' || command == 'd' || command == 'w'){
            currentDirection = commandToDir[command];
            printf("%d \n", currentDirection);

        applyMove(currentDirection);
        }
    }


    return 0;
}
