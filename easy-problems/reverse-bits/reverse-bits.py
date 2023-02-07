def reverseBits(self, n):
    # formatted_string = '{0:032b}'.format(n)
    # formatted_string_reverse = formatted_string[::-1]
    # return int(formatted_string_reverse, 2)
    return int(('{0:032b}'.format(n)),2)
    
    
if __name__ == "__main__" :
    print("Hello")