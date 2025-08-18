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
