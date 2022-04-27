import numpy

##var = [1,2,3]
##print(var)
##print(type(var))

##var = numpy.array([1,2,3])
##print(var)
##print(type(var))

##var = numpy.array([[1,2,3,],[4,5,6,]])
##print(var)
##print(type(var))

##var = numpy.array([1,2,3],ndmin = 2)
##print(var)
##print(type(var))

##data_type = numpy.dtype(numpy.int32)
##print(data_type)

##data_type = numpy.dtype('i4')
##print(data_type)

##data = numpy.array([[2,3,4],[5,6,7]])
##print(data.shape)

##data = numpy.array([[2,3,4],[5,6,7]])
##print(data.shape)
##data1 = data.reshape(2,3)
##print(data1.shape)

##data = numpy.empty([2,2],dtype = int)
##print(data)

##data = numpy.zeros(5)
##print(data)

##data = numpy.zeros((5),dtype = numpy.int32)
##print(data)

##broadcasting

##data = numpy.array([[2,3,4]])
##data1 = numpy.array([10,20,30])
##print(data * data1)


##data = numpy.array([[2,3,4],[5,6,7]])
##data1 = numpy.array([10,20,40])
##print(data * data1)

##data = numpy.array([2,3,44])
##data1 = numpy.array([10,10,10])
##print(data * data1)
                   
import pandas
var = [[2,3,4],[5,6,7]]
data = pandas.DataFrame(var)
print(data)
print(data.sum(axis = 1))
print(data.prod()) 






























