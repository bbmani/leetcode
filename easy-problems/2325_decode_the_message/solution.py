# CONVERT ASCII TO LETTERS

# for i in range(97, 123):
#     print("{}".format(chr(i)))

def decodeMessage(key, message) -> str:
    encoder = dict()
    ascii_value = 97
    final_string = ""
    
    for x in key:
        if x not in encoder and ascii_value < 123 and x != " ":
            encoder[x] = chr(ascii_value)
            ascii_value += 1
            
    for x in message:
        if x == " ":
            final_string += " "
        else:
            final_string = final_string + "".join(encoder[x])
            
        
    return final_string
               
def main():
    testcases = [["the quick brown fox jumps over the lazy dog", "vkbs bs t suepuv"], ["eljuxhpwnyrdgtqkviszcfmabo", "zwx hnfx lqantp mnoeius ycgk vcnjrdb"]]
    for testcase in testcases:
        returnValue = decodeMessage(testcase[0], testcase[1])
        print(returnValue)

if __name__ == "__main__":
    main()