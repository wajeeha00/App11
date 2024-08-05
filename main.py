import pandas 

df = pandas.read_csv('hotels.csv')
   

class Hotel:
    def __init__(self,id):
        self.id = id
        self.name = df.loc[df['id'] == self.id,"name"].squeeze()
    def book(self):
        df.loc[df['id'] == self.id,"available"] = 'no'
        df.to_csv('hotels.csv',index=False)
    def available(self):
        availability = df.loc[df['id'] == self.id,"available"].squeeze()
        if availability == 'yes':
            return True
        else:
            return False


class ReseravtionTicket:
    def __init__(self,customer_name,hotel_object):
        self.customer_name = customer_name
        self.hotel_object = hotel_object
    def generate(self):
        content = f"""
        Hello {self.customer_name},
        Your reservation is confirmed at {self.hotel_object.name}
        """
        return content


print(df)
id = int(input('Enter hotel id: '))
hotel = Hotel(id)
if hotel.available():
    print('Hotel is available')
    hotel.book()
    name = input('Enter your name: ')
    reservation = ReseravtionTicket(name,hotel)
    print(reservation.generate())
else:
    print('Hotel is not available')