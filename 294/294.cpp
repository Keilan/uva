#include<iostream>

using namespace std;

//Store the first 6000 primes - 6000th prime is 59359, which is less than math.sqrt(1e9)
int PRIMES[6000];
int NUM_PRIMES;

int sieve(){
    int NUM_PRIMES = 0;

    //Initialize a ray to 50000
    bool numbers[50000];
    for(int p=0; p<50000; p++){
        numbers[p] = true;
    }

    int total = 0;
    for(int i=2; i<50000; i++){
        if(numbers[i]){
            PRIMES[NUM_PRIMES++] = i;
            for(int j=2*i; j<=50000; j+=i){
                numbers[j] = false;
            }
        }
    }

    return NUM_PRIMES;
}

int countDivisors(int n, int NUM_PRIMES){
    //If n has prime factorization p^a * q^b, the number of divisors is (a+1) * (b+1), using this
    // fact we can determine the number of divisors based on the prime divisors
    int divisors = 1;
    for(int p = 0; p < NUM_PRIMES && n != 1; p++){
        int divides = 0;
        while(n % PRIMES[p] == 0){
            n /= PRIMES[p];
            divides++;
        }

        //Multiply divisors by the times it divides it + 1
        divisors *= (divides+1);
    }

    return divisors;
}


int main(){
    int NUM_PRIMES = sieve();

    int n,l,u;
    cin >> n;
    while(n--){
        //Read low and high values
        cin >> l >> u;

        int max = 0;
        int max_num = -1;
        for(int i = l; i <= u; i++){
            int val = countDivisors(i, NUM_PRIMES);
            if(val > max){
                max = val;
                max_num = i;
            }
        }
        cout << "Between " << l << " and " << u << ", " << max_num
             << " has a maximum of " << max << " divisors." << endl;
    }
    return 0;
}
