#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;

// Method 1: Using built-in sqrt() function
double builtinSqrt(double number) {
    return sqrt(number);
}

// Method 2: Newton-Raphson method (iterative approximation)
double newtonRaphsonSqrt(double number, double precision = 0.000001) {
    if (number < 0) {
        cout << "Error: Cannot find square root of negative number!" << endl;
        return -1;
    }
    
    if (number == 0 || number == 1) {
        return number;
    }
    
    double x = number / 2.0; // Initial guess
    double prev_x;
    
    do {
        prev_x = x;
        x = (prev_x + number / prev_x) / 2.0; // Newton-Raphson formula
    } while (abs(x - prev_x) > precision);
    
    return x;
}

// Method 3: Binary search method
double binarySearchSqrt(double number, double precision = 0.000001) {
    if (number < 0) {
        cout << "Error: Cannot find square root of negative number!" << endl;
        return -1;
    }
    
    if (number == 0 || number == 1) {
        return number;
    }
    
    double start, end;
    
    // Set search range based on number size
    if (number < 1) {
        start = number;
        end = 1;
    } else {
        start = 1;
        end = number;
    }
    
    double mid;
    while (end - start > precision) {
        mid = (start + end) / 2.0;
        double square = mid * mid;
        
        if (square == number) {
            return mid;
        } else if (square < number) {
            start = mid;
        } else {
            end = mid;
        }
    }
    
    return (start + end) / 2.0;
}

// Method 4: Babylonian method (same as Newton-Raphson but with different presentation)
double babylonianSqrt(double number, int iterations = 10) {
    if (number < 0) {
        cout << "Error: Cannot find square root of negative number!" << endl;
        return -1;
    }
    
    if (number == 0 || number == 1) {
        return number;
    }
    
    double x = number; // Initial guess
    
    for (int i = 0; i < iterations; i++) {
        x = (x + number / x) / 2.0;
    }
    
    return x;
}

int main() {
    double number;
    
    cout << "Square Root Calculator" << endl;
    cout << "=====================" << endl;
    cout << "Enter a number: ";
    cin >> number;
    
    if (number < 0) {
        cout << "Error: Cannot calculate square root of negative numbers!" << endl;
        return 1;
    }
    
    cout << fixed << setprecision(6);
    cout << "\nResults for √" << number << ":" << endl;
    cout << "--------------------------------" << endl;
    
    // Method 1: Built-in function
    double result1 = builtinSqrt(number);
    cout << "1. Built-in sqrt():     " << result1 << endl;
    
    // Method 2: Newton-Raphson
    double result2 = newtonRaphsonSqrt(number);
    cout << "2. Newton-Raphson:      " << result2 << endl;
    
    // Method 3: Binary Search
    double result3 = binarySearchSqrt(number);
    cout << "3. Binary Search:       " << result3 << endl;
    
    // Method 4: Babylonian
    double result4 = babylonianSqrt(number);
    cout << "4. Babylonian Method:   " << result4 << endl;
    
    // Verification
    cout << "\nVerification:" << endl;
    cout << "(" << result1 << ")² = " << result1 * result1 << endl;
    
    return 0;
}