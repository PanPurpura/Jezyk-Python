# Jezyk-Python
Zadania wykonwane w ramach przedmiotu język python

Jarosław Such

Projekt
==================================================
Dla ADT grafów z wykładu stworzyć implementację grafów opartą na macierzy sąsiedztwa (lista list). Wierzchołki są liczbami int od 0 do n-1. Zaimplementować BFS i DFS.

Macierz sąsiedztwa w tym wypadku może zwierać dwa elementy, które oznaczają następujące rzeczy:
- 0 - Wierzchołek istnieje, a w podanym miejscu nie ma krawędzi.
- 1 - Wierzchołek istnieje, a w podanym miejscu jest krawędź.

Implementacja grafu zawiera także proste menu, które pozwala na jej obsługę oraz testowanie odpowiednich funkcji. Zaimplementowane zostały następujące funkcje:
1. v() - Zwraca liczbę wierzchołków.
2. e() - Zwraca liczbę krawędzi.
3. is_directed() - Sprwadza czy graf jest skierowany czy też nie.
4. has_node(node) - Sprawdza czy wierzchołek należy do grafu.
5. del_node(node) - Usuwa podany wierzchołek z grafu
6. add_edge(edg) - Dodaje krawędź do grafu
7. has_edge(edge) - Sprwadza czy krawędź należy do grafu.
8. del_edge(edge) - Usuwa podaną krawędź z grafu.
9. neighbours(node) - Pomocnicza funkcja zwracająca sąsiadów podanego wierzchołka.
10. weight(edge_s, edge_t) - Zwraca wage krawędzi o podanym początku i końcu.
11. iternodes() - Zwraca iterator po wierzchołkach.
12. iteradjacent(node) - Zwraca iterator po wierzchołkach sąsiednich do podanego.
13. iteroutedges(node) - Zwraca iterator po krawędziach wychodzących od podanego wierzchołka.
14. iterinedges(node) - Zwraca iterator po krawędziach przychodzących do podanego wierzchołka.
15. iteredges() - Zwraca iterator po krawędziach grafu.
16. copy() - Zwraca kopię grafu.
17. transpose() - Zwraca transpozycję grafu.
18. complement() - Zwraca dopełnienie grafu.
19. subgraph(nodes) - Zwraca podgraf indukowany dla podanej listy wierzchołków.
20. show_matrix() - Funkcja wyświetlająca macierz sąsiedztwa.
21. show_list_of_nodes() - Funkcja wyświetlająca listę wierzchołków grafu.
22. show_list_of_edges() - Funkcja wyświetlająca listę krawędzi grafu.
23. DFS(node) - Przeszukiwanie w głąb od podanego wierzchołka.
24. BFS(node) - Przeszukiwanie wszerz od podanego wierzchołka.

Po uruchomieniu programu należy podać maksymalna wielkość naszego grafu oraz czy jest on skierowany czy też nie. Ważną uwagą jest iż w przypadku grafu nieskierowanego niektóre krawędzie mogą się powtórzyć np. dopuszczalne są krawędzie wierzchołka samego ze sobą, aby zobrazować iż jest to graf nieskierowany mogą wystąpić krawędzie typu: Edge(1, 1, 2), Edge(1, 1, 2). Druga z podanych krawędzi jest odwróconą wersją pierwszej jednak, ponieważ jest to krawędź wierzchołka samego ze sobą dlatego wyglądają one identycznie. 
