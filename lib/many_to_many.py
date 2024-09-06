class Author:

    all =[]

    def __init__(self,name):
        self.name = name
        Author.all.append(self)

    # method returns a list of all contracts associated with the current author.
    def contracts(self):
        return[contract for contract in Contract.all if contract.author == self] 

    # method returns a list of all books associated with the contracts signed by the current author.
    def books(self):
        return[contract.book for contract in self.contracts()]
    
    # method creates a new contract between the current author and the given book
    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)
    
    # method calculates the total royalties earned by the author across all their contracts.
    def total_royalties(self):
        return sum([contract.royalties for contract in self.contracts()])



class Book:

    all =[]

    def __init__(self,title):
        self.title = title
        Book.all.append(self)


    # method returns a list of all contracts associated with the current book.
    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]

    # method should return a list of authors associated that signed the book
    def authors(self):
        return [contract.author for contract in self.contracts()]
    


class Contract:

    all =[]

    def __init__(self,author,book,date,royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    
    # author property should be an instance of the Author class
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self,value):
        if not isinstance(value,Author):
            raise Exception("invalid author")
        self._author =value


    # book property should be an instance of the Book class.
    @property
    def book(self):
        return self._book
    
    @book.setter
    def book(self,value):
        if not isinstance(value,Book):
            raise Exception("invalid book")
        self._book =value    


    # date property should be a string that represents the date when 
    # the contract was signed
    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self,value):
        if not isinstance(value,str):
            raise Exception("invalid date")
        self._date =value    

    # royalties property should be a number that represents the percentage 
    # of royalties that the author will receive for the book.
    @property
    def royalties(self):
        return self._royalties
    
    @royalties.setter
    def royalties(self,value):
        if not isinstance(value,int):
            raise Exception("invalid royalties")
        self._royalties =value


    # method should return all contracts that have 
    # the same date as the date passed into the method.
    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]   


# output
author1 =Author("Sabina Sabina")
book1= Book("Kifo Kisimani")
contract1 = author1.sign_contract(book1, "01/01/2023", 10000)

# Display authors
print("\nAuthors:")
for author in Author.all:
    print(author.name)

# Display books
print("\nBooks:")
for book in Book.all:
    print(book.title)

# Display contracts
print("\nContracts:")
for contract in Contract.all:
    print(f"Author: {contract.author.name}, Book: {contract.book.title}, Date: {contract.date}, Royalties: {contract.royalties}")

# Get contracts for author1
print("\nAuthor1's contracts:")
for contract in author1.contracts():
    print(f"Book: {contract.book.title}, Date: {contract.date}")

# Get books written by author1
print("\nBooks written by Author1:")
for book in author1.books():
    print(book.title)

# Calculate total royalties for author1
print(f"\nTotal royalties for Author1: {author1.total_royalties()}")

# Get authors for book1
print("\nAuthors who wrote Book1:")
for author in book1.authors():
    print(author.name)

# Get contracts signed on a specific date
print("\nContracts signed on 01/01/2023:")
for contract in Contract.contracts_by_date("01/01/2023"):
    print(f"Author: {contract.author.name}, Book: {contract.book.title}")
