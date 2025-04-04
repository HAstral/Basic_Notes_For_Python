class Book:
    def __init__(self,title,author,num_pages):
        self.title=title
        self.author=author
        self.num_pages=num_pages

    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def __eq__(self, other):
        return self.title==other.title and self.author==other.author
    
    def __lt__(self,other):
        return self.num_pages < other.num_pages
    
    def __gt__(self,other):
        return self.num_pages > other.num_pages
    
    def __add__(self,other):
        return self.num_pages+other.num_pages
    
    def __contains__(self,keyword):
        return keyword in self.title or keyword in self.author

    def __getitem__(self,keyword):
        if keyword=="title":
            return self.title
        elif keyword=="author":
            return self.author
        elif keyword=="num_pages":
            return self.num_pages
        else:
            return f"keyword {keyword} not found"

book1=Book('The Hobbit','J.R.R Tolkien',310)
book2=Book("Harry Potter And The Philosopher's stone",'J.K Rowling',223)
book3=Book('The Lion, the Witch and the Wardrobe','C.S. Lewis',172)
# print(book2)
# print(book3<book2)
# print(book1+book2)
# print("The" in book1)
# print(book1['aura'])