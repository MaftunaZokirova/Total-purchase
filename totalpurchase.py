# Maftuna Zokirova

class Totalpurchase:
    def __init__(self, num_of_items: int, price_per_item: float ) -> None:
        self.num_of_items = num_of_items
        self.price_per_item = price_per_item
        self.total_price = 0.0


    def PromptNumofItem(self) -> None:
        self.num_of_items = input("Enter the number of items purchased: ")
        
    def PromptpricePerItem(self) -> None:   
        self.price_per_item = input ("Enter the price per item: $")
        
    def TotalCost(self, num_of_items: float, price_per_item: float ) -> float:
        the_cost = 0.0
        subtotal = 0.0
        # Sales tax is 5% = 0.05
        subtotal = float(num_of_items) * float(price_per_item)
        the_cost = subtotal + subtotal * 0.05
        
        return the_cost
        
    def DisplayTotalCost(self) -> None:
        
        print("Total purchase price is :", self.total_price)

    def Run(self) -> None:
        
        self.total_price = self.TotalCost(self.num_of_items, self.price_per_item)
        self.DisplayTotalCost()

