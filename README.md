# Jezyk-Python
Zadania wykonwane w ramach przedmiotu język python

Jarosław Such

Projekt
==================================================
Dla ADT grafów z wykładu stworzyć implementację grafów opartą na macierzy sąsiedztwa (lista list). Wierzchołki są liczbami int od 0 do n-1. Zaimplementować BFS i DFS.

Macierz sąsiedztwa w tym wypadku może zwierać trzy elementy, które oznaczają następujące rzeczy:
- n - None, dany wierzcholek nie istnieje i nie może mieć żadnej krawędzi.
- 0 - Wierzchołek istnieje a w podanym miejscu nie ma krawędzi.
- e - Pomiędzy dwoma wierzchołkami istnieje krawędź e

Warto zaznaczyć że w tej implementacji możemy dodać krawędź wtedy i tylko wtedy gdy dla dwóch wierzchołków, dla których chcemy utworzyć krawędź muszą w macierzy sąsiedztwa w odpowiednich wierszach zawierać 0. Oznacza to że dane dwa wierzchołki zostały utworzone. Nie możemy stworzyć krawędzi jeśli w rzędzie któregoś wierzchołka znajdują się "n", ponieważ nie został on wtedy dodany do grafu. 

Implementacja grafu zawiera także proste menu, które pozwala na jej obsługę oraz testowanie odpowiednich funkcji. Zaimplementowane zostały następujące funkcje:
1. v() - Zwraca liczbę wierzchołków.
2. e() - Zwraca liczbę krawędzi.
3. is_directed() - Sprwadza czy graf jest skierowany czy też nie.
4. add_node(node) - Dodaje wierzchołek do grafu.
5. has_node(node) - Sprawdza czy wierzchołek należy do grafu.
6. del_node(node) - Usuwa podany wierzchołek z grafu
7. add_edge(edg) - Dodaje krawędź do grafu
8. has_edge(edge) - Sprwadza czy krawędź należy do grafu.
9. del_edge(edge) - Usuwa podaną krawędź z grafu.
10. neighbours(node) - Pomocnicza funkcja zwracająca sąsiadów podanego wierzchołka.
11. weight(edge_s, edge_t) - Zwraca wage krawędzi o podanym początku i końcu.
12. iternodes() - Zwraca iterator po wierzchołkach.
13. iteradjacent(node) - Zwraca iterator po wierzchołkach sąsiednich do podanego.
14. iteroutedges(node) - Zwraca iterator po krawędziach wychodzących od podanego wierzchołka.
15. iterinedges(node) - Zwraca iterator po krawędziach przychodzących do podanego wierzchołka.
16. iteredges() - Zwraca iterator po krawędziach grafu.
17. copy() - Zwraca kopię grafu.
18. transpose() - Zwraca transpozycję grafu.
19. complement() - Zwraca dopełnienie grafu.
20. subgraph(nodes) - Zwraca podgraf indukowany dla podanej listy wierzchołków.
21. show_matrix() - Funkcja wyświetlająca macierz sąsiedztwa.
22. show_list_of_nodes() - Funkcja wyświetlająca listę wierzchołków grafu.
23. show_list_of_edges() - Funkcja wyświetlająca listę krawędzi grafu.
24. DFS(node) - Przeszukiwanie wgłąb od podanego wierzchołka.
25. BFS(node) - Przeszukiwanie wszerz od podanego wierzchołka.

Powyższa implementacja zawiera także dwie dodatkowe listy do przechowywania wszystkich wierzchołków oraz krawędzi znajdujących się w grafie.

Po uruchomieniu programu należy podać maksymalna wielkość naszego grafu oraz czy jest on skierowany czy też nie. Ważną uwagą jest iż w przypadku grafu nieskierowanego niektóre krawędzi mogą się powtórzyć np. dopuszczalne są krawędzie wierzchołka samego ze sobą, aby zobrazować iż jest to graf nieskierowany mogą wystąpić krawędzie typu: Edge(1, 1, 2), Edge(1, 1, 2). Druga z podanych krawędzi jest odwróconą wersją pierwszej jednak, ponieważ jest to krawędź wierzchołka samego ze sobą dlatego wyglądają one identycznie. 
