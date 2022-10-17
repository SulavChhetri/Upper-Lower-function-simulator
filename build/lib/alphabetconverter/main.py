class Converter:
    def __init__(self,strings):
        self.strings =strings

    #Added this function to check the strings
    def string_checker(self):
        for item in self.strings:
            if (ord(item)>=65 and ord(item)<=90) or (ord(item)>=97 and ord(item)<=122):
                return True
        return False

    def to_upper_case(self):
        if not Converter.string_checker(self):
            return "Should contain at least one alphabet character"
        else:
            output = list()
            for item in self.strings:
                if ord(item)>=97 and ord(item)<=122:
                    output.append(chr(ord(item)-32))
                else:
                    output.append(item)
            return ''.join(output)
           
    
    def to_lower_case(self):
        if not Converter.string_checker(self):
            return "Should contain at least one alphabet character"
        else:
            output = list()
            for item in self.strings:
                if ord(item)>=65 and ord(item)<=90:
                    output.append(chr(ord(item)+32))
                else:
                    output.append(item)
            return ''.join(output)