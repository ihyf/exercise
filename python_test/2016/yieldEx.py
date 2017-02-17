#coding:utf-8
# def h():
#     print 'Wen Chuan',
#     m = yield 1  # Fighting!
#     print m
#     d = yield 2
#     print 'We are together!'
#     z=yield 3
#     print d
#
# c = h()
# c.next()  #相当于c.send(None)
# c.send('1!')
# c.send('2!')
# c.send('3!')
def test_yield():
    print "test yeild"
    says = (yield)
    print
if __name__ == "__main__":
    client = test_yield()
    client.next()
    client.send("hello world")
