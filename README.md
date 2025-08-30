# Average, standard deviation and coefficient of variation

Ex. (195) - <i>Average, standard deviation and coefficient of variation</i>, is presented here in three programming languages: Python, MATLAB, and JavaScript. Although the implementations differ in syntax, the underlying concept remains identical across all three versions. Each code sample is reproduced from its respective volume of the series <i>Coding Examples from Simple to Complex</i> (Springer, 2024).
***

The above example performs statistical calculations on an array <i>a</i> and then calls the <i>stat</i> function with the array. The code starts by defining an array <i>a</i> with a list of numerical values. Then, the code initializes a variable <i>b</i> to 0 and another variable <i>e</i> to 0. Additionally, it creates an array <i>r</i> with three elements for storing statistical results, namely for the average (AV; mathematically denoted as <i>x̄</i>), standard deviation (SD; mathematically denoted as <i>σ</i>), and the coefficient of variation (CV; mathematically denoted as <i>C<sub>v</sub></i>).

$$
\bar{x} = \frac{\sum_{i=1}^{n} x_i}{n} 
        = \frac{\sum_{i=0}^{n-1} a[i]}{n} 
        = \frac{b}{n} 
        = r[0]
$$

$$
\sigma = \sqrt{\frac{\sum_{i=1}^{n}(x_i - \bar{x})^2}{n-1}} 
       = \sqrt{\frac{\sum_{i=0}^{n-1}(a[i] - r[0])^2}{n-1}} 
       = \sqrt{\frac{e}{n-1}} 
       = \left(\frac{e}{n-1}\right)^{0.5} 
       = r[1]
$$

$$
C_v = \frac{\sigma}{\bar{x}} 
    = \frac{r[1]}{r[0]} 
    = r[2]
$$

For the expressions shown above, please observe the progressive replacement and correlation with the variables from the code. The <i>for</i>-loop iterates through each element in the array <i>a</i> to calculate the sum of all values, which is stored in variable <i>b</i>. Next, the average (AV) is calculated by dividing the sum <i>b</i> by the total number of elements in the array (<i>n</i>), and the result is stored in <i>r[0]</i>. The code then proceeds to calculate the sum of squared differences from the average (<i>e</i>) for each element in the array. This step is essential for calculating the standard deviation (SD). The standard deviation (SD) is calculated as the square root of the sum of squared differences from the average, divided by (<i>n</i> − 1). The result is stored in <i>r[1]</i>. The coefficient of variation (CV) is calculated as the ratio of the standard deviation to the average (<i>r[1]/r[0]</i>). The <i>r</i> array, which now contains the calculated statistical values, is returned by the <i>stat</i> function. Thus, the code prints the result, which is the <i>r</i> array returned by the <i>stat</i> function, to the console using the <i>print</i> function.

Note that the <i>stat</i> function is essentially used to compute and return statistical information about the input array <i>a</i>, including the average, standard deviation, and coefficient of variation. Although clearly described in Ex. 156, here, in order to avoid an unnecessary import for the <i>math</i> library and the <i>sqrt</i> function, we use pure mathematical knowledge to take the square root. Thus, note that variance: <i>e / (n − 1)</i>. The standard deviation is the square root of the variance. The expression <i>(e / (n − 1)) ** 0.5</i> calculates this square root. The use of “** 0.5” is equivalent to using the <i>math.sqrt()</i> function of the <i>math</i> library. An experimentation with both approaches yields the same results. Raising a <i>number</i> to the power of 0.5 is equivalent to taking its square root. The square root of a number is the inverse operation of squaring that number. Squaring a <i>number</i> means raising it to the power of 2, thus, the inverse operation is to raise it to the power of ½ or 0.5. One can notice further that q<sup>0.5</sup> × q<sup>0.5</sup> = q<sup>0.5+0.5</sup> = q<sup>1</sup> = q, where q is a number. Thus, q<sup>0.5</sup> is indeed the square root of q, because when it is multiplied by itself it gives back q.

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
