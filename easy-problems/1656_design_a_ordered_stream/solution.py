class OrderedStream(object):

    def __init__(self, n):
        """
        :type n: int
        """
        self.customOrderStream = [None for i in range(n)]
        self.pointer = 0
        

    def insert(self, idKey, value):
        """
        :type idKey: int
        :type value: str
        :rtype: List[str]
        """
        
        self.customOrderStream[idKey-1] = value
        final_list = list()

        if self.pointer == idKey - 1:
            while self.pointer < len(self.customOrderStream) and self.customOrderStream[self.pointer] != None:
                final_list.append(self.customOrderStream[self.pointer])
                self.pointer += 1
        
        return final_list