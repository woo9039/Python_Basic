from collect.collect_daum_movie_review import review_collector


def main():
    print("=" * 100)
    print("== 영화 리뷰 수집기 ver 1.0 ==")
    print("=" * 100)
    movie_code = input("== 영화코드: ")  # 169328
    print('== MSG: "낮 12시마다 수집됩니다."')
    review_collector(movie_code)

if __name__ == "__main__":
    main()