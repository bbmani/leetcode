def longestCommonPrefix(strs):
  # Final Value returned to the program
  final = ""
  
  # Iteration
  indexer = 0
  
  # First to check whether the first word is repeated in all other words
  # example ["flower","flower","flower"]
  if strs.count(strs[0]) == len(strs):
    final = strs[0]
    return final
  
  # Infinte Loop
  while True:
    # Taking indexer-th letter from strs[0]
    tmp = strs[0][0:indexer+1]
    
    # Compare whether tmp is there in each word of strs, if not return final
    for i in range(0, len(strs)):
      if tmp != strs[i][0:indexer+1]:
        return final
      
    # If every word has tmp, then update final
    final = tmp
    
    # Update Indexer
    indexer = indexer + 1
         
    
        
if __name__ == "__main__":
  strs = ["flower","flow","flight"]
  x = longestCommonPrefix(strs)
  print(x)