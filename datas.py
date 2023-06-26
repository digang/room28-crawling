class donut_revenge:
    def __init__(self, datas):
        self.names = []
        self.prices = []
        self.imgs_url = []
        self.products_url = []
        self.products_sold_out = []
        
        for data in datas:
            self.names.append(data['name'])
            self.products_url.append(data['address'])
            self.imgs_url.append(data['thumbnails'][0])
            self.prices.append(data['price']['regularPrice'])
            self.products_sold_out.append(data['soldOut'])
    
    def get_names(self):
        return self.names
    
    def set_names(self, new_names):
        self.names = new_names
    
    def get_prices(self):
        return self.prices
    
    def set_prices(self, new_prices):
        self.prices = new_prices
    
    def get_imgs_url(self):
        return self.imgs_url
    
    def set_imgs_url(self, new_imgs_url):
        self.imgs_url = new_imgs_url
    
    def get_products_url(self):
        return self.products_url
    
    def set_products_url(self, new_products_url):
        self.products_url = new_products_url
    
    def get_products_sold_out(self):
        return self.products_sold_out
    
    def set_products_sold_out(self, new_products_sold_out):
        self.products_sold_out = new_products_sold_out
    
    def get_length(self):
        return len(self.names)
    
    def get_item_at_index(self, index):
        if index >= 0 and index < len(self.names):
            return {
                'name': self.names[index],
                'price': self.prices[index],
                'img_url': self.imgs_url[index],
                'product_url': self.products_url[index],
                'sold_out': self.products_sold_out[index]
            }
        else:
            return None
    
    def get_name_at_index(self, index):
        if index >= 0 and index < len(self.names):
            return self.names[index]
        else:
            return None
    
    def get_price_at_index(self, index):
        if index >= 0 and index < len(self.prices):
            return self.prices[index]
        else:
            return None
    
    def get_img_url_at_index(self, index):
        if index >= 0 and index < len(self.imgs_url):
            return self.imgs_url[index]
        else:
            return None
    
    def get_product_url_at_index(self, index):
        if index >= 0 and index < len(self.products_url):
            return self.products_url[index]
        else:
            return None
    
    def is_product_sold_out_at_index(self, index):
        if index >= 0 and index < len(self.products_sold_out):
            return self.products_sold_out[index]
        else:
            return None
