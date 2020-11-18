#import doc as d
#d.test(10)
import timeit as t

cy = t.timeit('doc.test(10)',setup= 'import doc', number =10000)

py = t.timeit('docpy.test(10)',setup= 'import docpy', number =10000)

print(cy,py)
print(py/cy)

