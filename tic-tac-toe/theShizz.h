using namespace std;
char board[3][3] = {{'1', '2', '3'}, {'4', '5', '6'}, {'7', '8', '9'}};
char c_mark;
int current_player;
void displayBoard()
{
    cout<<board[0][0]<<" | "<<board[0][1]<<" | "<<board[0][2]<<endl;
    cout<<"----------"<<endl;
    cout<<board[1][0]<<" | "<<board[1][1]<<" | "<<board[1][2]<<endl;
    cout<<"---------- "<<endl;
    cout<<board[2][0]<<" | "<<board[2][1]<<" | "<<board[2][2]<<endl<<endl;

}

int cursor(int num)
{
    int row;
    if((num%3) ==0)
    {
       row = (num/3)-1;
    }
    else
    {
        row = num/3;
    }

    int colm;
    if((num%3)==0)
        colm = 2;
    else
    {
        colm = num%3 -1;
    }

    if(board[row][colm]!= 'x' && board[row][colm] != 'o')
    {
        board[row][colm] = c_mark;
        return 1;
    }
    else
        return 0;
}

int winner()
{
    for(int i=0; i<3; i++)
    {
        //checking row
        if(board[i][0]== board[i][1] && board[i][1] == board[i][2])
            return current_player;

        //checking column
        if(board[0][i]== board[1][i] && board[1][i] == board[2][i])
            return current_player;

    }
    if(board[0][0] == board[1][1] && board[1][1]== board[2][2])
        return current_player;

    if(board[2][0] == board[1][1] && board[1][1] == board[0][2])
        return current_player;

    //if no one wins
    return 0;

}
void swap_player()
{
    if(current_player == 1)
        current_player = 2;
    else
        current_player = 1;

    if(c_mark == 'x')
        c_mark = 'o';
    else
        c_mark = 'x';

}

void game()
{
    cout<<"Player 1: 'O' or 'X' ?";
    char marker_1;
    cin>>marker_1;

    current_player = 1;
    c_mark = marker_1;

    int game_over;

    for(int i=0; i<9; i++)
    {
        cout<< "Player "<< current_player <<": Enter your move"<<endl;
        int num;
        cin>>num;
        if(num<1 || num > 9)
        {
            cout<<"Please enter a valid number:";
            i--;
            continue;
        }

        if(!cursor(num))
        {
            cout<<"That slot is occupied, please enter another!"<<endl;
            i--;
            continue;
        }

        displayBoard();
        game_over = winner();
        if(game_over == 1)
        {
            cout<<"Congratulations, player 1 won!";
            break;
        }
        game_over = winner();
        if(game_over == 2)
        {
            cout<<"Congratulations, player 2 won!";
            break;
        }

        swap_player();
    }
    if(winner() == 0)
    {
        cout<<"It is a tie!";
    }

}
