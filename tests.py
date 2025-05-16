import pytest


class TestBooksCollector:

    def test_add_new_book_add_two_books(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    def test_add_new_book_not_add_book_if_name_too_long(self, collector):
        long_name = 'Очень длинное название книги, которое превышает сорок символов'
        collector.add_new_book(long_name)
        assert long_name not in collector.get_books_genre()

    def test_set_book_genre_sets_genre_if_book_exists_and_genre_valid(self, collector):
        collector.add_new_book('Ночной дозор')
        collector.set_book_genre('Ночной дозор', 'Фантастика')
        assert collector.get_book_genre('Ночной дозор') == 'Фантастика'

    def test_set_book_genre_does_not_set_genre_if_book_not_in_collection(self, collector):
        collector.set_book_genre('Невидимка', 'Фантастика')
        assert collector.get_book_genre('Невидимка') is None

    def test_get_books_with_specific_genre_returns_correct_books(self, collector):
        collector.add_new_book('1984')
        collector.set_book_genre('1984', 'Фантастика')
        collector.add_new_book('Шрек')
        collector.set_book_genre('Шрек', 'Мультфильмы')
        collector.add_new_book('Матрица')
        collector.set_book_genre('Матрица', 'Фантастика')
        books = collector.get_books_with_specific_genre('Фантастика')
        assert set(books) == {'1984', 'Матрица'}

    def test_get_book_genre_return_correct_genre(self, collector):
        collector.add_new_book('Маленький принц')
        collector.set_book_genre('Маленький принц', 'Фантастика')
        assert collector.get_book_genre('Маленький принц') == 'Фантастика'

    def test_add_book_in_favorites_adds_book_if_it_exists(self, collector):
        collector.add_new_book('Три товарища')
        collector.add_book_in_favorites('Три товарища')
        assert 'Три товарища' in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_does_not_add_if_book_not_exists(self, collector):
        collector.add_book_in_favorites('Неизвестная книга')
        assert 'Неизвестная книга' not in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_removes_book(self, collector):
        collector.add_new_book('451° по Фаренгейту')
        collector.add_book_in_favorites('451° по Фаренгейту')
        collector.delete_book_from_favorites('451° по Фаренгейту')
        assert '451° по Фаренгейту' not in collector.get_list_of_favorites_books()

    def test_get_books_for_children_excludes_books_with_age_restriction(self, collector):
        collector.add_new_book('Коралина')
        collector.set_book_genre('Коралина', 'Ужасы')
        collector.add_new_book('Шрек')
        collector.set_book_genre('Шрек', 'Мультфильмы')
        result = collector.get_books_for_children()
        assert 'Коралина' not in result and 'Шрек' in result

    @pytest.mark.parametrize('book_name, genre', [
        ('Ночной дозор', 'Фантастика'),
        ('Шрек', 'Мультфильмы'),
        ('Комедия ошибок', 'Комедии'),
    ])
    def test_get_book_genre_returns_correct_genre_for_multiple_books(self, collector, book_name, genre):
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre(book_name) == genre

    def test_get_books_genre_returns_correct_dict(self, collector):
        collector.add_new_book('Дюна')
        collector.set_book_genre('Дюна', 'Фантастика')

        expected = {'Дюна': 'Фантастика'}
        assert collector.get_books_genre() == expected
