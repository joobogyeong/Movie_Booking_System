from graphviz import Digraph

def create_movie_booking_system_uml():
    uml = Digraph('MovieBookingSystem', filename='movie_booking_system', format='png')

    # Global attributes
    uml.attr(rankdir='LR', fontsize='10', fontname='Arial')

    # Nodes with pattern annotations
    uml.node('MovieTicketSystem', 'MovieTicketSystem\n(Singleton)', shape='box')
    uml.node('User', 'User', shape='box')
    uml.node('MovieFactory', 'MovieFactory\n(Factory)', shape='box')
    uml.node('Movie', 'Movie', shape='box')
    uml.node('Booking', 'Booking\n(Prototype)', shape='box')
    uml.node('BookingBuilder', 'BookingBuilder\n(Builder)', shape='box')
    uml.node('PaymentAdapter', 'PaymentAdapter\n(Adapter)', shape='box')
    uml.node('PaymentProcessor', 'PaymentProcessor\n(Proxy)', shape='box')
    uml.node('Notifier', 'Notifier\n(Observer)', shape='box')
    uml.node('Strategy', 'RecommendationStrategy\n(Strategy)', shape='box')
    uml.node('PopularMovies', 'PopularMoviesStrategy', shape='ellipse')
    uml.node('NearestTheater', 'NearestTheaterStrategy', shape='ellipse')

    # Relationships
    uml.edge('User', 'MovieTicketSystem', label='logs in')
    uml.edge('MovieTicketSystem', 'MovieFactory', label='uses')
    uml.edge('MovieFactory', 'Movie', label='creates')
    uml.edge('User', 'BookingBuilder', label='builds')
    uml.edge('BookingBuilder', 'Booking', label='builds')
    uml.edge('Booking', 'Movie', label='refers to')
    uml.edge('User', 'PaymentProcessor', label='initiates')
    uml.edge('PaymentProcessor', 'PaymentAdapter', label='delegates')
    uml.edge('MovieTicketSystem', 'Notifier', label='notifies')
    uml.edge('User', 'Strategy', label='uses')
    uml.edge('Strategy', 'PopularMovies')
    uml.edge('Strategy', 'NearestTheater')

    uml.render(directory='.', cleanup=False)

if __name__ == '__main__':
    create_movie_booking_system_uml()
