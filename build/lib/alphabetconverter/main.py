class Converter:
    def __init__(self,strings):
        self.strings =strings

    def to_upper_case(self):
        string_checker = list()
        output = list()
        for item in self.strings:
            if ord(item)>=97 and ord(item)<=122:
                output.append(chr(ord(item)-32))
                string_checker.append(item)
            else:
                output.append(item)
        if not len(string_checker)==0:
            return "".join(output)
        else:
            return "Input must contain at least one alphabet"
    
    def to_lower_case(self):
        string_checker =list()
        output = list()
        for item in self.strings:
            if ord(item)>=65 and ord(item)<=90:
                output.append(chr(ord(item)+32))
                string_checker.append(item)
            else:
                output.append(item)
        if not len(string_checker)==0:
            return "".join(output)
        else:
            return "Input must contain at least one alphabet"