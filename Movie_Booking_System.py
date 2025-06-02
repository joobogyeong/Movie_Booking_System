# Singleton Pattern (Multi-user aware)
class MovieTicketSystem:
    _instance = None

    def __init__(self):
        self.active_sessions = {}

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = MovieTicketSystem()
        return cls._instance

    def login(self, user):
        user.authenticate()
        self.active_sessions[user.name] = user

    def get_user(self, name):
        return self.active_sessions.get(name)

# Factory Pattern with Abstract + Concrete Factories
# Factory 기본 구조
class MovieProduct:
    def play(self):
        raise NotImplementedError

class ActionMovie(MovieProduct):
    def __init__(self):
        self.title = "Top Gun"
        self.genre = "Action"

    def play(self):
        print("영화 \"Top Gun\" 선택!")

class RomanceMovie(MovieProduct):
    def __init__(self):
        self.title = "The Notebook"
        self.genre = "Romance"

    def play(self):
        print("영화 \"The Notebook\" 선택!")

class SFMovie(MovieProduct):
    def __init__(self):
        self.title = "Interstellar"
        self.genre = "SF"

    def play(self):
        print("영화 \"Interstellar\" 선택!")

class ComedyMovie(MovieProduct):
    def __init__(self):
        self.title = "3 Idiots"
        self.genre = "Comedy"

    def play(self):
        print("영화 \"3 Idiots\" 선택!")

class AbstractMovieFactory:
    def create_movie(self):
        raise NotImplementedError

class ActionMovieFactory(AbstractMovieFactory):
    def create_movie(self):
        return ActionMovie()

class RomanceMovieFactory(AbstractMovieFactory):
    def create_movie(self):
        return RomanceMovie()

class SFMovieFactory(AbstractMovieFactory):
    def create_movie(self):
        return SFMovie()

class ComedyMovieFactory(AbstractMovieFactory):
    def create_movie(self):
        return ComedyMovie()

# Builder Pattern 
# 복잡한 객체 생성과정을 분리.
class AbstractBookingBuilder:
    def set_date(self, date): raise NotImplementedError
    def set_time(self, time): raise NotImplementedError
    def set_seat(self, seat): raise NotImplementedError
    def set_payment_info(self, payment_info): raise NotImplementedError
    def build(self): raise NotImplementedError

class BookingBuilder(AbstractBookingBuilder):
    def __init__(self):
        self.date = None
        self.time = None
        self.seat = None
        self.payment_info = None

    def set_date(self, date):
        self.date = date
        return self

    def set_time(self, time):
        self.time = time
        return self

    def set_seat(self, seat):
        self.seat = seat
        return self

    def set_payment_info(self, payment_info):
        self.payment_info = payment_info
        return self

    def build(self):
        return Booking(self.date, self.time, self.seat, self.payment_info)
    
class Booking:
    def __init__(self, date, time, seat, payment_info):
        self.date = date
        self.time = time
        self.seat = seat
        self.payment_info = payment_info

    def book(self):
        print(f"{self.date} {self.time} {self.seat} 예매완료!")

# Prototype Pattern
# 정보 수정 용도로 사용.
class BookingPrototype(Booking):
    def clone(self, date=None, time=None, seat=None, payment_info=None):
        return Booking(
            date or self.date,
            time or self.time,
            seat or self.seat,
            payment_info or self.payment_info
        )

# Adapter Interface
# 외부 결제 시스템을 통합하기 위해 사용
class PaymentAdapter:
    def pay(self, amount):
        raise NotImplementedError

class KBBankAdapter(PaymentAdapter):
    def pay(self, amount):
        KBBankAPI().send_kb_payment(amount)

class TossBankAdapter(PaymentAdapter):
    def pay(self, amount):
        TossBankAPI().send_toss_payment(amount)

class KakaoBankAdapter(PaymentAdapter):
    def pay(self, amount):
        KakaoBankAPI().send_kakao_payment(amount)

# External Bank APIs (Adaptee)
class KBBankAPI:
    def send_kb_payment(self, amount):
        print(f"[KBBank 결제 시스템] Paid {amount} via KB Bank")

class TossBankAPI:
    def send_toss_payment(self, amount):
        print(f"[TossBank 결제 시스템] Paid {amount} via Toss Bank")

class KakaoBankAPI:
    def send_kakao_payment(self, amount):
        print(f"[KakaoBank 결제 시스템] Paid {amount} via Kakao Bank")

# Proxy Pattern
# 민감한 정보, 결제를 대신 수행.
class PaymentProcessor:
    def __init__(self, user, method):
        self.user = user
        self.adapter = self.get_adapter(method)

    def get_adapter(self, method):
        if method == "KBBank":
            return KBBankAdapter()
        elif method == "TossBank":
            return TossBankAdapter()
        elif method == "KakaoBank":
            return KakaoBankAdapter()
        else:
            print(f"[Error] Payment method '{method}' is not supported.")
            return None

    def process_payment(self, amount):
        if self.user.is_authenticated() and self.adapter:
            self.adapter.pay(amount)
        elif not self.adapter:
            print("[Error] No valid payment adapter found.")
        else:
            print("User not authenticated. Payment denied.")

# Strategy Pattern
# 실시간으로 알고리즘 전략에 따라 작동하는 2가지 추천 시스템.
class RecommendationStrategy:
    def recommend(self, user):
        raise NotImplementedError

class NearestTheaterStrategy(RecommendationStrategy):
    def recommend(self, user):
        print("[가장 가까운 영화관 추천 시스템] 현재 위치를 분석 중입니다...")
        print("가장 가까운 영화관은 모현CGV입니다!")

class PopularMoviesStrategy(RecommendationStrategy):
    def recommend(self, user, genre="Action"):
        print("[인기 상영작 추천 시스템] 추천 영화 TOP 3")
        print(f"선택한 장르: {genre}")
        recommendations = {
            "Action": ["Top Gun: Maverick", "John Wick", "Mad Max: Fury Road"],
            "Drama": ["The Shawshank Redemption", "Forrest Gump", "The Pursuit of Happyness"],
            "SF": ["Interstellar", "Inception", "The Matrix"],
            "Comedy": ["The Hangover", "Superbad", "21 Jump Street"]
        }
        top_movies = recommendations.get(genre, ["기본 추천 영화 1", "기본 추천 영화 2", "기본 추천 영화 3"])
        for i, title in enumerate(top_movies, 1):
            print(f"{i}. {title}")

# Observer Pattern
# 실시간으로 상태를 확인하여 예매 완료 이벤트 시 알림을 받는 시스템.
# 간단한 print문으로 알림을 대신 구현.
class Notifier():
    def update(self, user, booking):
        if booking:
            msg = (f"{user.name}의 예매 정보\n"
                   f"- 영화: {booking.payment_info}\n"
                   f"- 날짜: {booking.date}\n"
                   f"- 시간: {booking.time}\n"
                   f"- 좌석: {booking.seat}")
            print(f"[예매 확인] {msg}")
        else:
            print(f"[예매 확인] {user.name}의 예매 정보를 찾을 수 없습니다.")

# User Class
class User:
    def __init__(self, name):
        self.name = name
        self.history = []
        self.authenticated = False

    def is_authenticated(self):
        return self.authenticated

    def authenticate(self):
        self.authenticated = True

    def logout(self):
        self.authenticated = False

    def get_booking_history(self):
        return self.history

    def add_booking(self, booking):
        self.history.append(booking)

# Example main function to demonstrate usage
def main():
    system = MovieTicketSystem.get_instance()

    # Users login
    alice = User("Alice")
    alex = User("Alex")
    system.login(alice)
    system.login(alex)
    
    # Strategy
    strategy = PopularMoviesStrategy()
    strategy.recommend(user=alice, genre="Action")

    strategy = NearestTheaterStrategy()
    strategy.recommend(alice)

    # Factory Usage
    action_factory = ActionMovieFactory()
    movie = action_factory.create_movie()
    movie.play()

    # Booking
    builder = BookingBuilder()
    booking = builder.set_date("2025-06-01").set_time("18:00").set_seat("K12").set_payment_info("KakaoBank").build()
    booking.book()
    alice.add_booking(booking)

    # Prototype Usage to modification and re-booking
    last_booking = alice.get_booking_history()[0]
    copied_booking = BookingPrototype(last_booking.date, last_booking.time, last_booking.seat, last_booking.payment_info)
    modified_booking = copied_booking.clone(seat="K13")
    modified_booking.book()
    alice.add_booking(modified_booking)

    # Proxy + Adapter
    processor = PaymentProcessor(alice, "KakaoBank")
    processor.process_payment(15000)

    # Observer
    notifier = Notifier()
    notifier.update(alice, modified_booking)

if __name__ == '__main__':
    main()
