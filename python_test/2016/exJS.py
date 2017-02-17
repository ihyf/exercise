import execjs

ctx=execjs.compile('''
    function add(x,y){
        alert(111)
    }
''')
print ctx.call("add",1,2)

