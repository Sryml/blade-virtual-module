import types

def generate_pyi(module_name):
    m = __import__(module_name)
    f = open("../../%s.pyi" % module_name,"w")
    nonfuncs = []
    for i in dir(m):
        if hasattr(m,i):
            atrr = getattr(m,i)
            if type(atrr) in (types.FunctionType, types.MethodType, types.BuiltinFunctionType, types.BuiltinMethodType):
                f.write("def %s(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.todo:\n" % i)
                if hasattr(atrr,"__doc__") and atrr.__doc__:
                    f.write('    """%s"""\n' % atrr.__doc__)
                f.write("    pass\n\n")
            else:
                nonfuncs.append(i)
    
    nonfuncs.sort()
    for i in nonfuncs:
        atrr = getattr(m,i)
        if type(atrr) == types.IntType:
            f.write("%s = %d\n" % (i,atrr))
        elif type(atrr) == types.StringType:
            f.write("%s = '%s'\n" % (i,atrr))
        elif type(atrr) == types.ListType:
            f.write("%s = %s\n" % (i,str(atrr)))
        elif type(atrr) == types.TupleType:
            f.write("%s = %s\n" % (i,str(atrr)))
        elif type(atrr) == types.DictType:
            f.write("%s = %s\n" % (i,str(atrr)))
        elif type(atrr) == types.FloatType:
            f.write("%s = %f\n" % (i,atrr))
        elif type(atrr) == types.NoneType:
            f.write("%s = None\n" % i)
        else:
            f.write("# %s = %s\n" % (i,str(atrr)))
    f.close()


"""
['BuiltinFunctionType', 'BuiltinMethodType', 'ClassType', 'CodeType', 'ComplexType', 'DictType', 'DictionaryType', 'EllipsisType', 'FileType', 'FloatType', 'FrameType', 'FunctionType', 'InstanceType', 'IntType', 'LambdaType', 'ListType', 'LongType', 'MethodType', 'ModuleType', 'NoneType', 'SliceType', 'StringType', 'TracebackType', 'TupleType', 'TypeType', 'UnboundMethodType', 'XRangeType', '__builtins__', '__doc__', '__file__', '__name__
"""