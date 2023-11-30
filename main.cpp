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
	cout << endl;
	BinarySearchTreeOfInteger clone = tree.clone();
	lista = tree.positionsPre();
	for (list<int>::iterator it = lista.begin(); it != lista.end(); it++){
		cout << *it << " ";
	}
	cout << endl;
 	lista = tree.positionsPos();
	for (list<int>::iterator it = lista.begin(); it != lista.end(); it++){
		cout << *it << " ";
	}
	cout << endl;
	tree.clear();
	

	tree.add(110);
	tree.add(120);
	tree.add(150);//rotaçao esquerda
	tree.add(130);
	tree.add(200);
	tree.add(100);
	tree.add(80);//rotaçao direita
	tree.add(70);
	tree.add(75);//rotaçao dupla direita
	tree.add(250);
	tree.add(230);//rotaçao dupla esquerda


	return 0;
}
