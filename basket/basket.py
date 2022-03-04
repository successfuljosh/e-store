from decimal import Decimal
from store.models import Product


class Basket:
    '''
    A base Basket class, providing some default behaviours that can be inherited
    or overrided as necessary
    '''
    def __init__(self, request):
        self.session = request.session
        basket = self.session.get('skey')
        if 'skey' not in request.session:
            basket = self.session['skey'] = {}
        self.basket = basket
    
    def add(self, product, qty):   #update=true, then update basket dict or create update function as below
        '''
        adding and updating the user basket session data 
        '''
        product_id = str(product.id)
        if product_id not in self.basket:
            self.basket[product_id] = {'price':str(product.price), 'qty': qty}
        else:
            self.basket[product_id]['qty'] = qty

        
        self.save()

    def __len__(self):
        '''
        returns the total qty of products in the basket
        '''
        return sum(item['qty'] for item in self.basket.values())

    #making basket iterable
    def __iter__(self):
        '''
        query the database based on products if of the 
        session basket to get products
        '''
        product_ids = self.basket.keys()
        products = Product.products.filter(id__in=product_ids)
        basket = self.basket.copy()
        for product in products:
            basket[str(product.id)]['product'] = product
        
        #get the total price for each product
        for item in basket.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['qty']
            yield item
    
    def get_total_price(self):
        return sum(Decimal(item['price']) * item['qty'] for item in self.basket.values())

    def delete(self, productid):
        '''
        delete from the basket session data 
        '''
        product_id = str(productid)
        if product_id in self.basket:
            del self.basket[product_id]
            self.save()
    
    def update(self, productid, productqty):
        '''
        update basket session data 
        '''
        product_id = str(productid)
        if product_id in self.basket:
            self.basket[product_id]['qty'] = productqty

        self.save()


    def save(self):
        self.session.modified = True    #saves changes made to the session data