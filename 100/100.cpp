#include <iostream>

using namespace std;


int findLength(int n){
    int count = 1;
    while(n != 1){
        if(n % 2 == 0){
            n /= 2;
        }
        else{
            n = 3*n + 1;
        }
        count++;
    }
    return count;
}

int main(){

    int start;
    int end;
    while(cin >> start >> end){
        int real_start = start;
        int real_end = end;
        if(start > end){
            int temp = start;
            start = end;
            end = temp;
        }

        int max = findLength(start);
        for(int i = start+1; i <= end; i++){
            int l = findLength(i);
            if(l > max){
                max = l;
            }
        }
        cout << real_start << ' ' << real_end << ' ' << max << endl;
    }

    return 0;
}
