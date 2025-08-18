##  *🤔 The Probleme :*  

- A complex number can be represented as a string on the form
    
    `"real+imaginaryi"` where:

- real is the real part and is an integer in the range `[-100, 100]`.
- imaginary is the imaginary part and is an integer in the range `[-100, 100]`.
- `i2 == -1`.
- Given two complex numbers `num1` and `num2` as strings, return a string of the complex number that represents their `multiplications`.  
##  *Explaining ⛓️‍💥*   

-  complex number  is an element of a number system that extends the `real` numbers with a specific element denoted `i`, called the `imaginary` unit and satisfying the equation :   


![Complex-Number-1-ezgif.com-webp-to-png-converter.png](https://assets.leetcode.com/users/images/fc9132b0-7887-48fd-b7ce-2ab1ca9c9305_1750769665.9509716.png)

- for more informations :  [https://en.wikipedia.org/wiki/Complex_number]()
-  After we know the complix number   we need to know how we calculate the multiplication   

-  The multiplication  in complex number have a steps :   

![Screenshot 2025-06-24 151440.png](https://assets.leetcode.com/users/images/650373f5-bf7b-46d0-9a8b-ff8aac030d04_1750774501.1979253.png)



- First Thing we do is Split num1 and num2 :   
    - and i take the number imaginary with `i` . 
    - like   `imaginary =  '23i' `   
    - i take `23` from  `23i` using :` imaginary1[:len(imaginary1)-1] ` 

```java 
num1_splite = num1.split('+')   
num2_splite = num2.split('+')
imaginary1 = num1_splite[1]     
imaginary1 =  imaginary1[:len(imaginary1)-1]  
```      

- ###   Befor we calcualte anything we need to know we have a `Three` operation before the last operation sum :   

    - `Real` * `Real`   
    - `Real` * `Imaginary`   
    - `Imaginary`  *  `Imaginary`     

###  *Real * Real*  
---
```py   
num1_splite[0] = int(num1_splite[0])   
num2_splite[0] = int(num2_splite[0])
first = (num1_splite[0] * num2_splite[0])   
```
### *Real   *  Imaginary*:
---
  
  - we have a two  operations here :   

   ```py 
            num1_real * num2_imaginary 
            num1_imaginary * num2_real
  ```

- First we need to take the imaginary number without `i` .   
- `secend_imaginary = int(num2_splite[1][:len(num2_splite[1])-1]  )`    
    
     ```py
      str (secend_imaginary * num1[0]) + 'i'
     ```

```py 
secend_imaginary = int(num2_splite[1][:len(num2_splite[1])-1]  )   
secend =  str(secend_imaginary * num1_splite[0]) + 'i'
```

```py 
thired_imaginary = int(num1_splite[1][:len(num1_splite[1])-1]  )  
thired =  str (thired_imaginary * num2_splite[0]) + 'i'
```
### **imaginary *  imaginary**  
--- 

    - we know `i2 == -1`  that mean  : ` i * i `    
    - soo all the cases when` num1_imaginary != i` 
    -  and `num2_imaginary != i `we gonna calcualt  normally . 
    - we take the imaginary number of num1 and num2 and we take the nombre only without `i `  


```py 
num1_image =  num1_splite[1]   
num2_image =  num2_splite[1]

if num1_image != 'i'  and num2_image  != 'i'  :  
    imaginar1 =  int(num1_image[:len(num1_image)-1])   
    imaginar2 =  int(num2_image[:len(num2_image)-1]) 

result  =  imaginar1 * imaginar2 * (-1)   
if num1_image == 'i'  and num2_image == 'i'  :   
    result  =  -1 

```

- After that we calculate the sum  :    
    - `real sum ` 

            real  =  str (first +  result)
    - `imaginary sum` 

```py 
            final_secend =  int(secend[:len(secend)-1])   
            final_thired = int (thired[:len(thired)-1])   
            imaginary = str(final_secend + final_thired) + 'i'
```
-  in final i creat a list to stock  `real sum` and `imaginary sum`. 


```py 
liste___ = [real , imaginary] 
return '+'.join(liste___)
```
## *Complexity ⌛*  

- Time complexity: $$O(1)$$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: $$O(1)$$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

## *The Solution ✅*  
```python3 []
class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        num1_splite = num1.split('+')   
        num2_splite = num2.split('+')  

        imaginary1 = num1_splite[1]     
        imaginary1 =  imaginary1[:len(imaginary1)-1]   

        num1_splite[0] = int(num1_splite[0])   
        num2_splite[0] = int(num2_splite[0])

        first = (num1_splite[0] * num2_splite[0])   

        secend_imaginary = int(num2_splite[1][:len(num2_splite[1])-1]  )   
        secend =  str(secend_imaginary * num1_splite[0]) + 'i'   

        thired_imaginary = int(num1_splite[1][:len(num1_splite[1])-1]  )  
        thired =  str (thired_imaginary * num2_splite[0]) + 'i' 

        num1_image =  num1_splite[1]   
        num2_image =  num2_splite[1]

        if num1_image != 'i'  and num2_image  != 'i'  :  
            imaginar1 =  int(num1_image[:len(num1_image)-1])   
            imaginar2 =  int(num2_image[:len(num2_image)-1]) 

        result  =  imaginar1 * imaginar2 * (-1)   
        if num1_image == 'i'  and num2_image == 'i'  :   
            result  =  -1 

        real = str(first + result)

        final_secend =  int(secend[:len(secend)-1])   
        final_thired = int (thired[:len(thired)-1])   

        imaginary = str(final_secend + final_thired) + 'i'

        liste___ = [real , imaginary] 
        return '+'.join(liste___)


``` 

![monkey-d-luffy-leetcode.jpg](https://assets.leetcode.com/users/images/2bf26951-96da-4234-b0dd-fe0c8edab82a_1750776385.060064.jpeg)
