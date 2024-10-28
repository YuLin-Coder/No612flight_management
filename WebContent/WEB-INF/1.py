import math
 
def trim(f):
    fl, cl = math.floor(f), math.ceil(f)
    
    if f-fl < 1e-7: return int(fl)
    if cl-f < 1e-7: return int(cl)
    return f
    
class Complex:
    def __init__(self, real=0.0, image=0.0):
        self.real = trim(real)
        self.image= trim(image)
    
    def __nonzero__(self):
        return 1 if self.real or self.image else 0
    
    def __abs__(self):      # abs(cmpl)
        return math.sqrt(self.real**2+self.image**2)
    
    def __invert__(self):     #~cmpl 共轭复数
        return Complex(self.real, -self.image)
    
    def __add__(self, comp):   #a+b
        if type(comp) is type(self):
            return Complex(self.real+comp.real,
                           self.image+comp.image)
        else:
            return Complex(self.real-comp, self.image)
        
    def __sub__(self, comp):    #a-b
        if type(comp) is type(self):
            return Complex(self.real-comp.real,
                           self.image-comp.image)
        else:
            return Complex(self.real-comp, self.image)
        
    def __mul__(self, comp):        #a*b
        if type(comp) is type(self):
            return Complex(self.real*comp.real-self.image*comp.image, 
                           self.real*comp.image+self.image*comp.real)
        else:
            return Complex(self.real*comp, self.image*comp)
        
    def __div__(self, comp):      #a/b
        if not comp:
            raise Exception('Divided by zero.')
        if type(comp) is type(self):
            a, b, c, d = self.real, self.image, comp.real, comp.image
            return Complex(float(a*c+b*d)/(c*c+d*d), float(b*c-a*d)/(c*c+d*d))
        else:
            return Complex(float(self.real)/comp, float(self.image)/comp)
    
    def __pow__(self, comp):      #a**b   复数的指数运算
        leng = self.__abs__()
        angl = self.arg()
        if type(comp) is type(self):
            nleng= leng**comp.real
            nangl= (angl*comp.real)%(math.pi*2)
            rr = Complex()
            rr.setMA(nleng, nangl)
            zs = self.log()*comp.image
            xc = Complex(zs.cos(), zs.sin())
            return rr*xc
        else:
            mod = leng**comp
            ang = (angl*comp)%(math.pi*2)
            return Complex(mod*math.cos(ang), mod*math.sin(ang))
    
    def __and__(self, comp):     # a and b    判断a、b都不是零
        return self.__nonzero__() and bool(comp) 
    
    def __or__(self, comp):    #a or b  判断a、b不都为零
        return self.__nonzero__() or bool(comp)     
    
    def __repr__(self):      #str(cmpl)
        sreal = str(self.real) if self.real != 0 else ''
        if int(self.image) == self.image and int(self.image) in (0,1,-1):
            simage= {0:'',1:'i',-1:'-i'}[int(self.image)]
        else:
            simage= "%si"%self.image 
        
        if sreal and self.image > 0:
            return sreal +'+'+ simage
        elif sreal or simage:
            return sreal + simage
        else:
            return '0'
            
    
    def setMA(self, m, a):
        self.real, self.image = m*math.cos(a), m*math.sin(a)
    
    def arg(self):     #获取辐角（没有想好用什么运算符表示，所以只用arg函数来实现了）
        return math.atan2(self.image, self.real)
    
    def log(self):        #复数的自然对数
        if not self.__nonzero__():
            raise Exception('Zero is not logarithm for any.')
        ang, mod = self.arg(), self.__abs__()
        return Complex(math.log(mod), ang)
    
    def exp(self):       #复数的指数
        rr = math.exp(self.real)
        return Complex(rr*math.cos(self.image), rr*math.sin(self.image))
    
    def sin(self):        #正弦
        return math.sin(self.real) * math.cosh(self.image) + \
                math.sinh(self.image) * math.cos(self.real)
    
    def cos(self):       #余弦
        return math.cos(self.real) * math.cosh(self.image) - \
                math.sin(self.real) * math.sinh(self.image)
    
#还有用其它的函数，这里就不列出了
#其实就是得来复变函数的运算规则实现的复数运算
if __name__ == '__main__':
    a, b, o = Complex(5,3), Complex(2,-1), Complex()

    print(a+b)
    print(a-b)
    print(a*b)

    
#     a = complex(1,2)
#     print math.log(a)