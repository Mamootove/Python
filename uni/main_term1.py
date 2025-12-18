#funcs 1:
def is_palindrome(word):
    return word == word[::-1]  #[::-1]، reverses the string    
def count_palindromes(words):
    """
    Gets a list, count the palindromes.
    >>>count_palindrome(["Ali", "Mom", "Mahan"])
    1
    """
    counter = 0
    for word in words:
        if is_palindrome(word):
            counter += 1
    return counter

def longest_word(words):
    longest = words[0]  #we assume that the longest word is the first one
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest

words = ["level", "apple", "radar", "banana", "civic", "python"]
print()
print(f"There are -{count_palindromes(words)}- palindrome words")
print(f"the longest word is -{longest_word(words)}-")
print()




# __question 2__
#funcs 2:
def sell_items(item, amount, items):   #items is a dict that will define by user later 
    mojodi = items.get(item, "nadarim!")
    if mojodi == "nadarim!":   #error message for item
        return "kala namojod ast"
    elif mojodi["amount"] < amount:   #error message for stock
        return "mojodi kafi nist!"
    else:
        total_price = amount* mojodi["price"]
        mojodi["amount"] -= amount   #updates amount
        return f"total price of {item} is -{total_price}- soled"
    
def restock_item(item, amount, items):
    mojodi = items.get(item, "nadarim")
    
    if mojodi == "nadarim":
        items[item] = {"amount" : amount, "price": 0.0}
    else:
        mojodi["amount"] += amount  
    print(f"{item} add\nconfirmed")
    
items = {"apple": {"amount": 30, "price" : 10}} #we only have apple
print("Questoin 2")
print()
print(sell_items("apple", 10, items))
restock_item("banana", 20, items)
print(items)  
  