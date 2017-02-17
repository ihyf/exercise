#conding:utf-8

#one
class Singleton(object):
    @staticmethod
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls,'_instance'):
            o=super(Singleton,cls)
            cls._instance=o.__new__(cls)
        return cls._instance




class A(Singleton):
    a=1

if __name__=='__main__':
    s1=A()
    s2=A()
    s1.a=10
    s2.a
    print s2.a