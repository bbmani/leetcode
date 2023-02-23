class Codec:
    def encode(self, strs) -> str:
        """Encodes a list of strings to a single string.
        """

        final_string = ""
        for str_custom in strs:
            final_string += str(len(str_custom)) + "$" + str_custom
        
        return final_string
        

    def decode(self, s: str):
        """Decodes a single string to a list of strings.
        """

        final_list, i = list(), 0

        while i < len(s):
            j = i

            while s[j] != "$":
                j += 1
            
            length = int(s[i:j])

            final_list.append(s[j+1:j+1+length])
            i = j+1+length
        
        return final_list