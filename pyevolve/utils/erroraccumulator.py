from math import sqrt as math_sqrt

class ErrorAccumulator:
   """ An accumulator for the Root Mean Square Error (RMSE) and the
   Mean Square Error (MSE)
   """
   def __init__(self):
      self.acc        = 0.0
      self.acc_square = 0.0
      self.acc_len    = 0

   def reset(self):
      """ Reset the accumulator """
      self.acc_square = 0.0
      self.acc        = 0.0
      self.acc_len    = 0

   def append(self, target, evaluated):
      """ Add value to the accumulator
      
      :param target: the target value
      :param evaluated: the evaluated value
      """
      self.acc_square += (target - evaluated)**2
      self.acc        += abs(target - evaluated)
      self.acc_len    +=1
      
   def __iadd__(self, value):
      """ The same as append, but you must pass a tuple """
      self.append(*value)
      return self

   def getMean(self):
      """ Return the mean of the non-squared accumulator """
      return self.acc / self.acc_len

   def getSquared(self):
      """ Returns the squared accumulator """
      return self.acc_square

   def getNonSquared(self):
      """ Returns the non-squared accumulator """
      return self.acc

   def getAdjusted(self):
      """ Returns the adjusted fitness
      This fitness is calculated as 1 / (1 + standardized fitness)
      """
      return 1.0/(1.0 + self.acc)

   def getRMSE(self):
      """ Return the root mean square error
      
      :rtype: float RMSE
      """
      return math_sqrt(self.acc_square / float(self.acc_len))

   def getMSE(self):
      """ Return the mean square error

      :rtype: float MSE
      """
      return (self.acc_square / float(self.acc_len))
