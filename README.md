# Average, standard deviation and coefficient of variation

Ex. (195) - Average, standard deviation and coefficient of variation, is presented here in three programming languages: Python, MATLAB, and JavaScript. Although the implementations differ in syntax, the underlying concept remains identical across all three versions. Each code sample is reproduced from its respective volume of the series <i>Coding Examples from Simple to Complex</i> (Springer, 2024).
***

The above example performs statistical calculations on an array <i>a</i> and then calls the <i>stat</i> function with the array. The code starts by defining an array <i>a</i> with a list of numerical values. Then, the code initializes a variable <i>b</i> to 0 and another variable <i>e</i> to 0. Additionally, it creates an array <i>r</i> with three elements for storing statistical results, namely for the average (AV; mathematically denoted as <i>x̄</i>), standard deviation (SD; mathematically denoted as <i>σ</i>), and the coefficient of variation (CV; mathematically denoted as <i>C<sub>v</sub></i>).

## Example in Python:

```python
def stat(a):
    n = len(a)
    b = 0
    e = 0
    r = [0, 0, 0]  # AV, SD, CV

    for j in range(n):
        b += a[j]

    r[0] = b / n

    for j in range(n):
        e += (a[j] - r[0]) ** 2

    r[1] = (e / (n - 1)) ** 0.5
    r[2] = r[1] / r[0]

    return r

a = [5, 1, 8, 4, 6, 2, 8, 9]
b = stat(a)
print(b)
``` 

```text
Python output:
[5.375, 2.9246489410818914, 0.5441207332245379]
```

## Example in Javascript:

```javascript
let a = [5, 1, 8, 4, 6, 2, 8, 9];

let b = stat(a)
print(b)

function stat(a){

    let n = a.length;
    
    let b = 0;
    let e = 0;
    
    let r = [];
    r[0] = 0; // AV
    r[1] = 0; // SD
    r[2] = 0; // CV
    
    for(var j=0; j<n; j++){
        b += a[j];
    }
    
    r[0] = b/n;
    
    for(var j=0; j<n; j++){
        e += Math.pow((a[j] - r[0]), 2);
    }
    
    r[1] = Math.sqrt(e/(n-1));
    r[2] = r[1]/r[0];
    
    return r;
}
```

```text
Javascript output:
[5.375, 2.9246489410818914, 0.5441207332245379]
```

## Example in Matlab:

```matlab
a = [5, 1, 8, 4, 6, 2, 8, 9];

b = stat(a);
disp(b);

function r = stat(a)
    n = length(a);
    b = 0;
    e = 0;

    % Initialize the results array
    r = zeros(1, 3); % AV, SD, CV

    % Calculate the sum of 
    % the array elements.

    for j=1:n
        b = b + a(j);
    end

    % Calculate the arithmetic 
    % mean (AV).

    r(1) = b/n;

    % Calculate the standard 
    % deviation (SD).

    for j=1:n
        e = e + (a(j) - r(1))^2;
    end

    r(2) = sqrt(e/(n-1));

    % Calculate the coefficient 
    % of variation (CV).

    r(3) = r(2)/r(1);
end
```

```text
Matlab output:
[5.375, 2.9246489410818914, 0.5441207332245379]
```

## References

- <i>Paul A. Gagniuc. Coding Examples from Simple to Complex - Applications in Python, Springer, 2024, pp. 1-245.</i>
- <i>Paul A. Gagniuc. Coding Examples from Simple to Complex - Applications in MATLAB, Springer, 2024, pp. 1-255.</i>
- <i>Paul A. Gagniuc. Coding Examples from Simple to Complex - Applications in Javascript, Springer, 2024, pp. 1-240.</i>

***
