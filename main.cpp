#include <iostream>
#include "BinarySearchTreeOfInteger.h"

using namespace std;

int main (){
	BinarySearchTreeOfInteger tree;
	tree.add(1);
	tree.add(2);
	tree.add(3);
	tree.add(4);
	tree.add(5);
	tree.add(6);
	tree.add(7);
	tree.add(8);
	tree.add(9);
	cout << tree.height() << endl;
	tree.clear();
	tree.add(9);
	tree.add(8);
	tree.add(7);
	tree.add(6);
	tree.add(5);
	tree.add(4);
	tree.add(3);
	tree.add(2);
	tree.add(1);
	list <int> lista = tree.positionsCentral();
	for (list<int>::iterator it = lista.begin(); it != lista.end(); it++){
		cout << *it << " ";
	}
	BinarySearchTreeOfInteger clone = tree.clone();
	lista = tree.positionsPre();
	for (list<int>::iterator it = lista.begin(); it != lista.end(); it++){
		cout << *it << " ";
	}
 	lista = tree.positionsPos();
	for (list<int>::iterator it = lista.begin(); it != lista.end(); it++){
		cout << *it << " ";
	}
	tree.clear();
	/**
	 * Adicionar na tree numeros que gerem as 4 rotacoes previstas, boa sorte!!!!!!!!!
	*/
	return 0;
}