def div(a,b):
    print(a/b)

def smart_div(func):#ye hum ek tarah ka decorator he bna re hai or ye compulsory hota hai iske andar ye func pass karna
                    #iska basically matlab bas itna he hota hai ke hum ek tarah se div ko andar pass kar re hai
    def inner(a,b):# this part is also compulsary as  it will have the same number of argument as the div function is having
                   # here we will provide such code which we want to be there in the div function
        if(a<b):
            a,b=b,a
        return func(a,b)
    return inner
div1=smart_div(div)
div1(2,6)       

'''here basically what we have done is we have created a div function that takes two parameter but we have made a decoratoer down saying that it 
\should swap the value when it first value is greater than the second value since divison will be vary odd i that case so this is all what is done at here'''