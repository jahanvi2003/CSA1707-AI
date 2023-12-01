% Facts
sentence("This is my first Degree in Saveetha School of Engineering.").

% Rules
vowel_count(Count) :-
    sentence(S),
    string_chars(S, CharList),
    count_vowels(CharList, Count).

count_vowels([], 0).
count_vowels([H | T], Count) :-
    (   is_vowel(H)
    ->  count_vowels(T, RestCount),
        Count is RestCount + 1
    ;   count_vowels(T, Count)
    ).

is_vowel(X) :- member(X, ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']).

% Query example
% To find the number of vowels:
% ?- vowel_count(Count).
