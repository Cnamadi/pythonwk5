from bookclass import FictionBook 

# Creating a classic fiction book
book1 = FictionBook("Crime and Punishment", "Fyodor Dostoevsky", 1866, "Psychological Fiction")
book2 = FictionBook("The Trial", "Franz Kafka", 1925, "Philosophical Fiction")

# Displaying book descriptions
print(book1.get_description())
print(f"Is '{book1.title}' a classic? {'Yes' if book1.is_classic() else 'No'}")

print(book2.get_description())
print(f"Is '{book2.title}' a classic? {'Yes' if book2.is_classic() else 'No'}")