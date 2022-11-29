def func1(arg1, arg2):
    var15 = func5()
    var40 = func6(arg2, var15)
    def func7(arg41, arg42):
        result = var40 + (arg2 & var15) & arg42 ^ var40 | var40
        return result
    var43 = func7(arg1, var40)
    var48 = func8(arg1, var15)
    var49 = var15 - var43 ^ arg1 ^ var40
    var50 = arg1 & arg1
    var51 = 30 | var49
    var52 = var51 - var43
    var53 = arg2 - arg2
    var54 = var53 & -663
    var55 = var50 + -1375586616
    var56 = var48 ^ arg1
    var57 = var40 ^ var52 | arg1 + var49
    var58 = (arg2 - var50 ^ 370) + var43
    var59 = var40 | (var55 - var43) | var52
    var60 = var49 + var40
    var61 = arg1 ^ arg1 + (arg1 & var52)
    var62 = var53 ^ (var51 & var58) + var54
    var63 = var58 - var15 & var43 - var50
    var64 = var55 & var56
    var65 = ((var50 + var48) - var50) + var54
    if var48 < var63:
        var66 = var58 + (var54 | -233 ^ var50)
    else:
        var66 = var61 & var53 & arg2 | var40
    result = var52 + var63 & var63 & var60
    return result
def func8(arg44, arg45):
    var46 = 0
    for var47 in xrange(45):
        var46 += -8 & -6 ^ arg44
    return var46
def func6(arg16, arg17):
    var18 = (arg16 ^ -284) + arg17 ^ arg17
    var19 = ((arg17 ^ arg16) ^ -1402209416) & arg17
    if arg17 < var18:
        var20 = arg17 ^ 446105585
    else:
        var20 = (1546483241 ^ arg17) - arg16
    var21 = ((var18 - var19) & 558133044) | arg16
    var22 = (arg17 & arg16) ^ var18 + -2085503732
    var23 = -945 & -933139807 - (var18 + 1352371039)
    var24 = (-596046818 + var18) ^ -225 + var22
    var25 = var21 + (var19 + var24)
    var26 = arg16 + (arg17 & -2126403524) ^ var22
    var27 = var23 & var24
    var28 = (var18 & var25 | var23) | var22
    var29 = var26 | var23
    var30 = var24 & var19
    var31 = arg16 ^ var25
    if var24 < var23:
        var32 = ((var30 + var22) - 1779868631) + var31
    else:
        var32 = arg17 & var21
    var33 = var18 | var18
    var34 = -586 & var25 | (var19 - var22)
    var35 = (var28 & var19 & var30) ^ arg17
    var36 = var22 - var19
    var37 = var28 + arg17 | var26 ^ var23
    var38 = (var31 - arg17 ^ var31) + var28
    var39 = (var37 ^ (var25 | var18)) & var23
    result = (((var22 + var38) - var30) | var25) + var23
    return result
def func5():
    func2()
    result = len(func4(-9, 8))
    func3()
    return result
def func4(arg3, arg4):
    var5 = 1562369891 | (-421 | arg3) & 506
    yield var5
    var6 = (566 & arg3 ^ var5) - arg3
    yield var6
    var7 = (907 + arg3) | arg3
    yield var7
    var8 = (var6 & (arg4 + arg4)) ^ 2034135163
    yield var8
    var9 = var8 - 305796286
    yield var9
    var10 = (var5 | var6) ^ var9 + var6
    yield var10
    var11 = var8 - var8 + var5 + var6
    yield var11
    var12 = 113 - arg3 | var11 & var5
    yield var12
    var13 = 1848961789 & (var11 - var9) ^ arg4
    yield var13
    var14 = (var6 ^ -906) - var7 ^ arg3
    yield var14
def func3():
    global len
    del len
def func2():
    global len
    len = lambda x : 0
if __name__ == "__main__":
    print 'prog_size: 5'
    print 'func_number: 9'
    print 'arg_number: 67'
    for i in xrange(25000):
        x = 5
        x = func1(x, i)
        print x,
