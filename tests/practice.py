class UserMainCode(object):
    @classmethod
    def first_duplicate(cls, input1):
        '''
        input1 : ArrayList[Integer]

        Expected return type : Integer
        '''
        # Read only region end
        import re
        word= re.sub(r'[]',"",)
        for i in input1:
            if i in s:
                return i
            else:
                s.add(i)
        if len(s) == len(input1):
            return -1


obj = UserMainCode()
obj.first_duplicate([8, 4, 6, 2, 6, 4, 7, 1, 5, 8])

